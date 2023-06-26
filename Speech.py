# !pip install gTTS 
from gtts import gTTS

def text_to_speech(text, filename, lang='en', voice='default'):
    tts = gTTS(text=text, lang=lang, slow=False, tld=voice)  # Create gTTS object with the text, language, and voice options
    tts.save(filename)  # Save the speech audio to a file


# Read Text file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Example usage
file_path = 'test.txt' # Enter text file path which you wants to select
text = read_text_from_file(file_path)
filename = "output.mp3" # Enter output save location

# Replace 'en'  with ur desired language code found from "https://developers.google.com/admin-sdk/directory/v1/languages"

text_to_speech(text, filename, lang='en', voice='com.au')  # Change language to English and voice to 'com.au'

