from constructs import (
    Construct
)
from aws_cdk import (
    App,
    Stack,
    SecretValue,
    Environment,
    )
from aws_cdk import aws_s3,aws_s3_deployment as s3,s3deploy



class CdkTestStack(
    Stack
    ):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        waterBucket = s3.Bucket(
                             self,
                             'MyFirstBucket',
                             bucket_name=waterBucket,
                             versioned=True,
                             public_read_access=True)
        
        waterBucketDeploy = s3deploy.BucketDeployment(
                                                self, 
                                                'DeployBucket',
                                                sources =[s3.Source.asset('/Users/poulamyghosal/python_ML/MyPlot.png')])
        
    
       #  #                    __path__='/Users/poulamyghosal/python_ML/MyPlot.png')

