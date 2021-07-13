"""
contador de palabras de un fichero o de una frase.
Al final debe sacar la palabra que más veces aparezca.
Se modifican todas las palabras para que estén en minúsculas, por lo tanto False y false seran la misma palabra
"""
import sys
import re
# Si salta alguna excepcion devolvera None.
def ReadFile(file):
    id = 0
    try:
        with open(file,'r') as myFile:
            file_content = myFile.read()
            return file_content
    except FileNotFoundError:
        print("File Not Found")
    except:
        print("Unexpected error:" + str(sys.exc_info()))
    
#guarda en una lista todas las palabras separando por diferentes signos de puntuación
def mySplit(text):
    b = re.split('[\[\].;,\-_()!?\s\n]',text) #Todos los simbolos de puntuacion
    b[:] = (w.lower() for w in b) #convierte a minusculas cada palabra
    filtered_words = filter(None,b)
    return filtered_words

def addWord(word):
    if (word in my_words):
        my_words[word] +=1
    else:
        my_words[word] =1

def processText(text):
    words = mySplit(text) 
    for p in words:
        addWord(p)

#Encuentra las palabras con la mayor frecuencia    
def maxWords(dict):
    maxDetect = max(my_words.values())
    for word, freq in dict.items():
        if (freq == maxDetect):
            print(word + " -- " + str(freq))

#Main
# leo el archivo
my_text = ReadFile("archivo.txt")
#my_text = "hóla hola Fálse Falsé, falsè )) fàlse flse "
if(my_text):
    my_words={} 
    processText(my_text)
    maxWords(my_words)
else:
    print ("NO elements")
