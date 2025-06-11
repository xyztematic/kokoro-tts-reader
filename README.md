# kokoro-tts-reader

Written and tested on Windows 10 with Python 3.10.4.
May work with Windows 11.


## Dependecies

espeak-ng has to be installed on your machine. The following installation instruction is a excerpt from the [kokoro github](https://github.com/hexgrad/kokoro):

---
1. Go to [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases)
2. Click on **Latest release** 
3. Download the appropriate `*.msi` file (e.g. **espeak-ng-20191129-b702b03-x64.msi**)
4. Run the downloaded installer
---
All other dependencies will be installed with the provided setup script:
1. Run the setup script `setup.bat`
2. Wait for the command prompt window to close. It may take a few minutes to install all dependecies

## Starting and using the app
1. Run the start script `start.bat` _(You may run this script via a link from your desktop, if you like)_
2. Paste your desired text into the text field
3. Click `Read` and wait for the audio to be generated
4. Once the audio generation is finished, the text will be narrated by Kokoro TTS
