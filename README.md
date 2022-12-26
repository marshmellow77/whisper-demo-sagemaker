# whisper-demo-sagemaker
A demo with OpenAI's Whisper model deployed to a SageMaker endpoint

## Steps to set up the demo
1. Run the notebook in the sagemaker folder which will deploy the Whisper model to a SM endpoint
2. Run the Cloudformation template in the ec2 folder, either via AWS CLI or in the AWS console (AWS CLI Command: `aws cloudformation create-stack --stack-name whisper-demo-stack --template-body file://cf_template.yaml`)
3. Once the EC2 instance is spun up, find the IP Address. The app will be available on <IP_ADDRESS>:8501. (Note: The microphone input won't work as it uses http protocol. More info: https://github.com/gradio-app/gradio/issues/2551) 
