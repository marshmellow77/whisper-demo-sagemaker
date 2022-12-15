wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
sudo apt-get update
sudo apt install python3-pip
pip3 install gradio
pip3 install boto3
pip3 install iso-639
sudo apt install ffmpeg
python3 whisper-demo-sagemaker/ec2/gradio-app.py
