#!/usr/bin/env python3

import speech_recognition as sr
#import time
import os
import markovify
import re
import numpy as np

def generate_frase():
    text_array = []
    files = [f for f in os.listdir('./textos/') if os.path.isfile(os.path.join("./textos/", f))]
    for f in files:
        print(f)
#Get raw text as string.
        with open("./textos/"+f) as g:
            text_g = g.read()
            text_array.append(markovify.Text(text_g))
    # Si hay más archivos txt, no olvidar modificar pesos de markovify.combine
#    model_combo = markovify.combine(text_array, [0.2, 1.0, 0.8, 0.4,0.3])
    model_combo = markovify.combine(text_array)
    frase = model_combo.make_short_sentence(280)
    if(frase is not None):
        return frase
    else:
        return("No tengo nada que decir")
    #print(text_array)


    #with open("test.txt", 'a+') as file:
    #    for line in result:
    #        print(line)
    #        file.write(line)
    #        file.write('\n')


#utility function for text cleaning
def text_cleaner(text):
  text = re.sub(r'--', ' ', text)
  text = re.sub('[\[].*?[\]]', '', text)
  text = re.sub(r'(\b|\s+\-?|^\-?)(\d+|\d*\.\d+)\b','', text)
  text = ' '.join(text.split())
  return text

# Write text to file
def write_to_file(text):
    with open('./textos/textosave.txt', 'a') as f:
        f.write(text + "\n")
        f.close()


# Initialize the recognizer
r = sr.Recognizer()


# Loop for listening and speaking

while(True):
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            #listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2, language="es-MX")
            #MyText = MyText.lower()
            #MyText = text_cleaner(MyText)
            print("You said:  "+MyText)
            #time.sleep(0.5)
            write_to_file(MyText)


            new_frase = generate_frase()
            print("Computadora dice: " +new_frase)
            os.system("echo "+new_frase+" |iconv -f utf-8 -t iso-8859-15 | festival --tts")

    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
            print("unknown error occured")
