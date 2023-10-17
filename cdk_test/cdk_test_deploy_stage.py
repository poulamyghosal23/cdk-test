from constructs import Construct
from aws_cdk import (
    Stage,
    Environment
)

from .cdk_test_stack import CdkTestStack

class CdkTestDeployStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        CdkTestStack(self, "CdkTestStack", env=Environment(account=self.account, region=self.region))