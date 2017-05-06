#!/usr/bin/env bash

# This will setup the pip, nodeJS, and apt requirements for the project.
# Make sure to run this in the top level directory of the project.

# Set-up environments
sudo apt install python python-pyaudio python-numpy python-pip \
 sox libsox-fmt-all
# Installs nodejs and npm
sudo apt install -f npm

# Amazon Polly
# Replace "taylor" with your user namea
sudo apt install awscli
aws configure
sudo pip install awscli --upgrade
sudo pip install boto boto3

# API.AI Python API
sudo pip install apiai

# Google Cloud Client Library
sudo pip install --upgrade google-cloud-speech

# Google Cloud SDK
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install google-cloud-sdk
sudo apt-get install google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-java
gcloud init

# Phillips Hue
sudo pip install phue

# Sonus
sudo apt install sox libsox-fmt-all
sudo apt install libatlas-base-dev
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt install nodejs
cd Sonus
sudo npm install npm --global
npm install --save sonus
npm install node-aplay
npm install net-socket
cd ../