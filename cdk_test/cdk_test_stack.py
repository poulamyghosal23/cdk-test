from constructs import (
    Construct
)
from aws_cdk import (
    App,
    Stack,
    SecretValue,
    Environment,
    )
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_iam as iam
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_lambda_event_sources as lambda_event_sources
from aws_cdk import aws_s3_deployment as s3deploy



class CdkTestStack(
    Stack
    ):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        waterBucket = s3.Bucket(
                             self,
                             'MyFirstBucket',
                             bucket_name="waterbucket",
                             versioned=True,
                             public_read_access=True)
        
        waterBucketDeploy = s3deploy.BucketDeployment(
                                                self, 
                                                'DeployBucket',
                                                sources =[s3deploy.Source.asset('/Users/poulamyghosal/python_ML/MyPlot.png')],
                                                destination_bucket=waterBucket)
        
    
       #  #                    __path__='/Users/poulamyghosal/python_ML/MyPlot.png')

