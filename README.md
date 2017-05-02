## GALA
#### Google Automated Language Assistant

Goal: To build a voice controlled personal assistant using [API.AI](https://api.ai)

#### Setup
1) Install [API.AI](https://api.ai)
```
$ sudo apt install python-pyaudio python-numpy
$ sudo pip install apiai

TODO: Add step to place client key
```
2) Install [phue](https://github.com/studioimaginaire/phue/blob/master/phue.py)
```
$ sudo pip install phue
```
3) Install [Google Cloud client library](https://cloud.google.com/speech/)
```
$ sudo pip install --upgrade google-cloud-speech
```
4) Install [Sonus](https://github.com/evancohen/sonus)
```
$ sudo apt install sox libsox-fmt-all
$ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
$ sudo apt install nodejs
$ sudo npm install npm --global
$ npm install --save sonus
```
5) Install [Google Cloud SDK](https://console.cloud.google.com/)
```
$ export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
$ echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
$ curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ sudo apt-get update && sudo apt-get install google-cloud-sdk
$ sudo apt-get install google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-java
$ gcloud init
```