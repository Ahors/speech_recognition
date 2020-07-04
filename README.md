# speech_recognition
Personal helper with speech recognition

## Installation
Install pipenv and all of the dependencies from pipenv file. You also need to install .whl file from the root of the repository for pyaudio.
```shell
pip pipenv
pipenv install
pipenv install *pyaudio file_name*
```
Change the API key to your Google API key
```python
GOOGLE_API_KEY = *Your API key* # Remember to change the API key
```

## Usage
You can run the project in virtual environment with
```shell
pipenv run main.py
```
