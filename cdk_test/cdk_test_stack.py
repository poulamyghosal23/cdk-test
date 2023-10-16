from constructs import (
    Construct
)
from aws_cdk.core import (
    App,
    Stack,
    SecretValue,
    Environment,
    )
from aws_cdk import aws_s3 as s3
from aws_cdk import core as core
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_s3_assets as s3_assets
from aws_cdk import aws_codepipepine


class CdkTestStack(
    Stack
    ):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        waterBucket = s3.Bucket(self,
                             'MyFirstBucket',
                             bucket_name=core.PhysicalName.GENERATE_IF_NEEDED,
                             versioned=True)
        waterBucket.grant_public_access()
        
        waterAsset = s3_assets.Asset(self,
                                     'MyFirstAsset',
                                     path='/Users/poulamyghosal/python_ML/MyPlot.png')
         #                    __path__='/Users/poulamyghosal/python_ML/MyPlot.png')

        
        #waterLambda = lambda_.Function(self, "waterlambda", environment=dict(BUCKET_NAME=waterBucket.bucket_name))
        #pipeline = pipelines.CodePipeLine(
        #    self,
        #    "Pipeline",
        #    synth=pipelines.ShellStep(
        #        "Synth",
        #        input=pipelines.CodePipelineSource.git_hub('poulamyghosal23/cdk-test', 'main', authentication=SecretValue.secrets_manager('aws-access-punditry-account')),
        #        commands=[
        #            "npm install -g aws-cdk",
        #            "pip install -r requirements.txt",
        #            "cdk synth",
        #        ]
        #),
        #)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkTestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
