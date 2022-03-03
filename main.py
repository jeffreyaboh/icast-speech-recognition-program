# import library

# Converts text to speech
import gtts
# Timeout Timer
import threading
# Plays the audio
from playsound import playsound
# Recognize audio input
import speech_recognition as sr

r = sr.Recognizer()


# Introduction
def introduction():
    intro_text = "Welcome To the International College of Arts, Science and Technology's Speech Recognition Program"
    print(intro_text)
    intro_audio = gtts.gTTS(intro_text)
    intro_audio.save("audio.mp3")
    playsound("audio.mp3")
    setup()


# Setup
def setup():
    setup_text = "What would you like to call me? "
    setup_audio = gtts.gTTS(setup_text)
    setup_audio.save("audio.mp3")
    playsound("audio.mp3")
    program_name = input(setup_text)

    confirmation_text = 'Thank you. My name has been set to '
    print(program_name + ': ' + confirmation_text + program_name)
    setup_audio = gtts.gTTS(confirmation_text + program_name)
    setup_audio.save("audio.mp3")
    playsound("audio.mp3")

    set_user_name = 'What would you like me to call you? '
    set_user_name_audio = gtts.gTTS(set_user_name)
    set_user_name_audio.save("audio.mp3")
    playsound("audio.mp3")

    set_user_name_input = input(set_user_name)
    set_user_name_confirmation = 'Awesome! I would call you' + set_user_name_input + ' '
    print(program_name + ': ' + set_user_name_confirmation)
    set_user_name_audio = gtts.gTTS(set_user_name_confirmation)
    set_user_name_audio.save("audio.mp3")
    playsound("audio.mp3")

    menu(program_name)


# Menu
def menu(program_name):
    menu_text = 'What would you like to do today? '
    print(program_name + ': ' + menu_text)
    menu_audio = gtts.gTTS(menu_text)
    menu_audio.save("audio.mp3")
    playsound("audio.mp3")
    list_menu(program_name)


# List menu
def list_menu(program_name):
    menu_one = 'Convert a speech to text'
    menu_two = 'Convert a text to speech'
    print('A. ' + menu_one + '\nB. ' + menu_two)
    list_menu_audio_text_one = 'One ' + menu_one
    list_menu_audio_text_two = 'Two ' + menu_two
    list_menu_audio = gtts.gTTS(list_menu_audio_text_one)
    list_menu_audio.save("audio.mp3")
    playsound("audio.mp3")
    list_menu_audio = gtts.gTTS(list_menu_audio_text_two)
    list_menu_audio.save("audio.mp3")
    playsound("audio.mp3")

    response = input(program_name + ': Enter your response  i.e A or B')
    task(program_name, response, menu_one, menu_two)


# Task
def task(program_name, response, menu_one, menu_two):
    if response == 'a':
        with sr.Microphone() as source:
            task_text = 'For how many seconds would you like to record your voice note'
            task_menu_audio = gtts.gTTS(task_text)
            task_menu_audio.save("audio.mp3")
            playsound("audio.mp3")
            delay = int(input(program_name + ': ' + task_text))
            # print("Recording...")
            # audio_text = r.listen(source, timeout=delay, phrase_time_limit=delay)


    if response == 'b':
        print('B has been selected')


# Initialize introduction
introduction()

# with sr.Microphone() as source:
#     print("Welcome, My name is Javis!")
#     delay = int(input("Javis: Enter the length of your voice note in seconds: "))
#     print("Recording...")
#     audio_text = r.listen(source, timeout=delay, phrase_time_limit=delay)
#     print("Javis: Time's up! Thanks, Please wait while i processing your voice note...")
#
#     try:
#         print("Javis: Your audio translation is: " + r.recognize_google(audio_text))
#         t1 = gtts.gTTS(audio_text)
#         t1.save("welcome.mp3")
#         playsound("welcome.mp3")
#     except:
#         print("Javis: Sorry, I did not get that")
