import wikipedia
from sys import argv
from google.cloud import texttospeech
import urllib.request

def synthesize_text(text):
    client = texttospeech.TextToSpeechClient()
    input = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-GB',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input, voice, audio_config)

    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

while True:
    topic = input("\nEnter topic to be summarized: ")
    try:
        article = wikipedia.summary(topic)
        print("\n" + article)
        synthesize_text(article)
        images = wikipedia.WikipediaPage(topic).images
        for i in range (len(images)):
            if ((images[i][-3:] == "jpg") or (images[i][-3:] == "png")):
                urllib.request.urlretrieve(images[i], "0000000" + str(i) + ".jpg")

    except Exception as e: print(e)
