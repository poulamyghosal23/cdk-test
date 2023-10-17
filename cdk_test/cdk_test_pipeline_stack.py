from constructs import (
    Construct
)
from aws_cdk import (
    App,
    Stack,
    SecretValue,
    Environment,
    )

from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, CodeBuildStep
from .cdk_test_deploy_stage import CdkTestDeployStage

class CdkTestPipelineStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        waterPipeline = CodePipeline(
            self,
            "WaterPipeline",
            pipeline_name="WaterPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub('poulamyghosal23/cdk-test', 'main', authentication=SecretValue.secrets_manager('aws-access-punditry-account')),
                commands=[
                    "npm install -g aws-cdk",
                    "pip install -r requirements.txt",
                    "cdk synth",
                ]
        ),
        )
        deploy_dev = CdkTestDeployStage(
            self,
            "DeployDev",
            env=Environment(account="431549854911", 
            region="us-east-1"))
        
        waterPipeline.add_stage(deploy_dev)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkTestQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
