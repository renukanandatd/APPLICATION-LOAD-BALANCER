import aws_cdk as core
import aws_cdk.assertions as assertions

from alb_lambda_project.alb_lambda_project_stack import AlbLambdaProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in alb_lambda_project/alb_lambda_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AlbLambdaProjectStack(app, "alb-lambda-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
