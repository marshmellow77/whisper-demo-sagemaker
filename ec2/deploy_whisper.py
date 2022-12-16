from sagemaker.huggingface.model import HuggingFaceModel
from sagemaker.serializers import DataSerializer

huggingface_model = HuggingFaceModel(
   model_data="s3://sagemaker-us-east-1-905847418383/whisper/model/model.tar.gz",
   role='arn:aws:iam::905847418383:role/service-role/AmazonSageMaker-ExecutionRole-20210804T091905',
   transformers_version="4.17",
   pytorch_version="1.10",
   py_version='py38',
)

endpoint_name = "whisper-large-v2"
audio_serializer = DataSerializer(content_type='audio/x-audio')

predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g4dn.xlarge",
    endpoint_name=endpoint_name,
    serializer=audio_serializer,
)