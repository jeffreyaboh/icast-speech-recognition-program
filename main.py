# import library

# Converts text to speech
import gtts
# Timeout Timer
import threading
# Plays the audio
from playsound import playsound
# Random string generator
from strgen import StringGenerator as SG
# Recognize audio input
import speech_recognition as sr

r = sr.Recognizer()
# Audio path
audio_path = "audio_logs/"


# Introduction
def introduction():
    intro_text = "Welcome To the International College of Arts, Science and Technology's Speech Recognition Program"
    print(intro_text)
    intro_audio = gtts.gTTS(intro_text)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    intro_audio.save(audio_file)
    playsound(audio_file)
    setup()


# Setup
def setup():
    setup_text = "What would you like to call me? "
    setup_audio = gtts.gTTS(setup_text)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    setup_audio.save(audio_file)
    playsound(audio_file)
    program_name = input(setup_text)

    confirmation_text = 'Thank you. My name has been set to '
    print(program_name + ': ' + confirmation_text + program_name)
    setup_audio = gtts.gTTS(confirmation_text + program_name)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    setup_audio.save(audio_file)
    playsound(audio_file)

    set_user_name = 'What would you like me to call you? '
    set_user_name_audio = gtts.gTTS(set_user_name)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    set_user_name_audio.save(audio_file)
    playsound(audio_file)

    set_user_name_input = input(set_user_name)
    set_user_name_confirmation = 'Awesome! I would call you ' + set_user_name_input + ' '
    print(program_name + ': ' + set_user_name_confirmation)
    set_user_name_audio = gtts.gTTS(set_user_name_confirmation)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    set_user_name_audio.save(audio_file)
    playsound(audio_file)

    menu(program_name, set_user_name_input)


# Menu
def menu(program_name, user_name_input):
    menu_text = 'What would you like to do today ' + user_name_input + '?'
    print(program_name + ': ' + menu_text)
    menu_audio = gtts.gTTS(menu_text)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    menu_audio.save(audio_file)
    playsound(audio_file)
    list_menu(program_name, user_name_input)


# List menu
def list_menu(program_name, user_name_input):
    menu_one = 'Convert a speech to text'
    menu_two = 'Convert a text to speech'
    print('A. ' + menu_one + '\nB. ' + menu_two)
    list_menu_audio_text_one = 'One ' + menu_one
    list_menu_audio_text_two = 'Two ' + menu_two

    list_menu_audio = gtts.gTTS(list_menu_audio_text_one)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    list_menu_audio.save(audio_file)
    playsound(audio_file)

    list_menu_audio = gtts.gTTS(list_menu_audio_text_two)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    list_menu_audio.save(audio_file)
    playsound(audio_file)

    response = input(program_name + ': Enter your response  i.e A or B ')
    task(program_name, user_name_input, response, menu_one, menu_two)


# Return menu prompt
def return_menu_prompt(program_name, user_name_input):
    return_prompt = 'Press 1 to go back to the main menu or Press 0 to exit this program '
    return_prompt_audio = gtts.gTTS(return_prompt)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    return_prompt_audio.save(audio_file)
    playsound(audio_file)

    event = int(input(program_name + ': ' + return_prompt))
    if event == 1:
        menu(program_name, user_name_input)

    if event == 0:
        return;


# Task
def task(program_name, user_name_input, response, menu_one, menu_two):
    if response.lower() == 'a':
        speech_to_text(program_name, user_name_input, response, menu_one, menu_two)

    if response.lower() == 'b':
        text_to_speech(program_name, user_name_input, response, menu_one, menu_two)


# Run speech to text conversion
def speech_to_text(program_name, user_name_input, response, menu_one, menu_two):
    with sr.Microphone() as source:
        task_text = 'For how many milli seconds would you like to record your voice note? '
        task_menu_audio = gtts.gTTS(task_text)
        string = SG(r"[\w]{30}").render()
        audio_file = audio_path + string + ".mp3"
        task_menu_audio.save(audio_file)
        playsound(audio_file)

        delay = int(input(program_name + ': ' + task_text))
        print(program_name + ': Recording...')
        audio_text = r.listen(source, timeout=delay, phrase_time_limit=delay)

        try:
            confirmation = 'Your audio translation is displayed on the screen'
            print(program_name + ': Your audio translation is: ' + r.recognize_google(audio_text))
            confirmation_audio = gtts.gTTS(confirmation)
            string = SG(r"[\w]{30}").render()
            audio_file = audio_path + string + ".mp3"
            confirmation_audio.save(audio_file)
            playsound(audio_file)

            # Return menu
            return_menu_prompt(program_name, user_name_input)

        except:
            exception = "Sorry, I didn't get that"
            print(program_name + ': ' + exception)
            exception_audio = gtts.gTTS(exception)
            string = SG(r"[\w]{30}").render()
            audio_file = audio_path + string + ".mp3"
            exception_audio.save(audio_file)
            playsound(audio_file)

            # Restart speech_to_text
            speech_to_text(program_name, response, menu_one, menu_two)


# Run text to speech conversion
def text_to_speech(program_name, user_name_input, response, menu_one, menu_two):
    task_text = 'Input the text you would like to convert to a voice note '
    task_menu_audio = gtts.gTTS(task_text)
    string = SG(r"[\w]{30}").render()
    audio_file = audio_path + string + ".mp3"
    task_menu_audio.save(audio_file)
    playsound(audio_file)
    message = input(program_name + ': ' + task_text)

    try:
        confirmation = 'Your conversion from text to speech is as follows '
        print(program_name + ': ' + confirmation)
        confirmation_audio = gtts.gTTS(confirmation)
        string = SG(r"[\w]{30}").render()
        audio_file = audio_path + string + ".mp3"
        confirmation_audio.save(audio_file)
        playsound(audio_file)

        print(program_name + ': Playing voice note... ')
        message_audio = gtts.gTTS(message)
        string = SG(r"[\w]{30}").render()
        audio_file = audio_path + string + ".mp3"
        message_audio.save(audio_file)
        playsound(audio_file)

        # Return menu
        return_menu_prompt(program_name, user_name_input)

    except:
        exception = "Sorry, I didn't get that"
        print(program_name + ': ' + exception)
        exception_audio = gtts.gTTS(exception)
        string = SG(r"[\w]{30}").render()
        audio_file = audio_path + string + ".mp3"
        exception_audio.save(audio_file)
        playsound(audio_file)

        # Restart text_to_speech
        text_to_speech(program_name, response, menu_one, menu_two)


# Initialize introduction
introduction()

#https://docs.google.com/presentation/d/1hwv5ohDXDWUrGl8ujxFNi5ND3U_9kqQM/edit?usp=sharing&ouid=108425278559405572561&rtpof=true&sd=true
