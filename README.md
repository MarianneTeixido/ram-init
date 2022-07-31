# R. A. M. [Redes Autónomas de Memoria] 
Compartición en el Encuentro Transhackfeminista 22 (THF22)
Calafou, Catalonia. 


![sistema](https://github.com/MarianneTeixido/ram-init/blob/main/img/RAM-init.jpg)

# Tejiendo redes de pensamiento colectivo

Este repositorio es el proyecto inicial de una serie de ejercicios vinculantes que buscan explorar las posibilidades de tecnologías como la voz y el machine learning, por medio de la exploración colectiva de algoritmos  tecnosociales, para tejer redes neuronales capaces de conjurar estratégias de cuidado y autocuidado colectivo. 

Este ejercicio es una constante pregunta, no excepta de error, glitch, fallo y contradicción. El cual más que intentar evitarlo, se promueve como metodología contrapedagógica para que dejar de lado el aprender para hacer sino hacer para aprender. Reponde también a una duda colectiva sobre si ¿puede la inteligencia artificial ser una herramienta para los feminismos y transfeminismos? 

Es por ello que este proyecto tiene como premisa fundamental el crear una narrativa híbrida en el cual la máquina como agencia, pueda coadyuvar a la lucha y resistencia contra las violencias que como cuerpas feminizadas, trans y no binarias vivimos día con día, en lugar de abonar a la opresiones, discriminación y de ser una herramienta que agudiza las relaciones de poder. 

El objetivo de R.A.M. es socializar, desmitificar, descoser los algortimos, explorar, cuestionar y crear críticamente con sonido y voz desde una perspectiva decolonial sobre las herramientas que nos permiten entrenar cadenas lógicas de probabilidad estadística que hacen que una máquina "aprenda". 

# Can the machines speak?

¿Qué es inteligencia? ¿Cómo es que una máquina aprender? ¿Puede una máquina aprender? ¿Qué es aprender? Preguntas guía para una respuesta que más que técnica puede ser incluso filosófica. 

Reconocimiento, patrones, estadística y probabilidad. 

## Speech-to-text

[Librería Speech Recognition](https://pypi.org/project/SpeechRecognition/)

Pasos para usar

Ingresar a la carpeta  
Para compilar en tiempo real usar 

```python
python speech.py
```

Para compilar en desde un archivo de audio

```python 
python speechaudio.py
```

Crear un archivo txt para guardar el texto. 

```python 
def write_to_file(text):
    with open('/home/unyxt/github/ram-stt/textosave.txt', 'a') as f:
        f.write(text + "\n")
        f.close()
```

Para cambiar el idioma a español

```python 
MyText = r.recognize_google(audio2, language='es-MX')
```

## Cadenas de markov para texto 

[Libería Markovify](https://github.com/jsvine/markovify)

## Texto to speech

[Festival](https://www.cstr.ed.ac.uk/projects/festival/)




