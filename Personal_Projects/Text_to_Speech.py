
# Import the required module for text 1
# to speech conversion
import gtts
from playsound import playsound
import os

def text_to_speech(input_text):
    
    # make request to google to get synthesis
    tts = gtts.gTTS(input_text, lang='en')

    path_folder = os.path.dirname(__file__) + '/Audios/'
    file_name = 'Text_to_Speech.mp3' 
    path_file = path_folder + file_name
    #print("Path and File: ",path_file)

    # save the audio file
    tts.save(file_name)

    # play the audio file
    playsound(file_name)
    main()


def load_file():

    print("Please enter the complete file path:")
    input_path = input()
    try:
        path_file = input_path.replace('\\','\\\\')

        path_file = open(path_file, 'r')
        text_speech = path_file.read()
        path_file.close()

        return text_speech

    except ValueError:
        print ('File not found: ',path_file)
        return None

def main():

    print("Please choose one option by entering the number: \n 1 - Enter Text\n 2 - File Path")
    input_type = input()

    if input_type == '1':
        print('Enter the text:"')
        text = input()
        text_to_speech(text)
    
    elif input_type == '2':
        text_from_file = load_file()
        print(text_from_file)
        text_to_speech(text_from_file)

    else:
        print('Choose one option by entering the numbers 1 or 2.')
        main()

if __name__ == "__main__":
    main()