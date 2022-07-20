# R. A. M. [Redes Autónomas de Memoria] 

![sistema](https://github.com/MarianneTeixido/ram-init/blob/main/img/RAM-init.jpg)

English below


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




