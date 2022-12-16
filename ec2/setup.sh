wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda
echo "PATH=$PATH:$HOME/miniconda/bin" >> ~/.bashrc
sudo apt-get update -y
sudo apt install python3-pip -y
pip3 install gradio
pip3 install boto3
pip3 install iso-639
sudo apt install ffmpeg -y
screen -d -m python3 whisper-demo-sagemaker/ec2/gradio-app.py
