import io
import os


def run_quickstart(__file__):
    # Imports the Google Cloud client library
    from google.cloud import speech

    # Instantiates a client
    speech_client = speech.Client()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        'resources',
        'audio.raw')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        sample = speech_client.sample(
            content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate_hertz=16000)

    # Detects speech in the audio file
    alternatives = sample.recognize('en-US')

    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))

if __name__=='__main__':
    run_quickstart()