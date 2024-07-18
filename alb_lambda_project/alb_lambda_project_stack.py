from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_elasticloadbalancingv2 as elbv2,
    aws_elasticloadbalancingv2_targets as elbv2_targets,
    aws_ec2 as ec2  # Import VPC
)
from constructs import Construct

class AlbLambdaProjectStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a simple VPC with default configuration
        vpc = ec2.Vpc(self, "VPC")

        # Create the Lambda function
        hello_lambda = _lambda.Function(
            self, 'HelloFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello.handler',
            code=_lambda.Code.from_asset('lambda')
        )

        # Create an ALB
        alb = elbv2.ApplicationLoadBalancer(
            self, 'ALB',
            vpc=vpc,  # Assign the VPC here
            internet_facing=True
        )

        # Create an ALB listener
        listener = alb.add_listener(
            'Listener',
            port=80,
            open=True
        )

        # Add a target group with the Lambda function
        listener.add_targets(
            'LambdaTarget',
            targets=[elbv2_targets.LambdaTarget(hello_lambda)]
        )
