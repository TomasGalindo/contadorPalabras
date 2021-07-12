"""
contador de palabras de un fichero o de una frase.
Al final debe sacar la palabra que más veces aparezca.
"""
import re

#guarda en una lista todas las palabras separando por diferentes signos de puntuación
def mySplit(text):
    b = re.split('[\[\].;,\-_()!?\s\n]',text) #Todos los simbolos de puntuacion
    filtered_words = filter(None,b)
    return filtered_words

def addWord(word):
    if (word in my_words):
        my_words[word] +=1
    else:
        my_words[word] =1

def processLine(text):
    #
    words = mySplit(text) 
    #Recorro la lista de palabras
    for p in b:
        print(p)
        addWord(p)

#Encuentra las palabras con la mayor frecuencia    
def maxWords(dict):
    maxDetect = max(my_words.values())
    for word, freq in dict.items():
        #print(word + " -- " + str(freq))
        if (freq == maxDetect):
            print(word + " -- " + str(freq))



#Main
my_words={} #diccionario donde voy a guardar mis palabras
a= "hola qu]e tal    tabulo False.     hago de zz todo. 1,2,3,4,5, Hay que (quitar \n todos los simbolos) de puntuacion; para que solo queden las palabras"
b= mySplit(a)

#Recorro la lista de palabras
for p in b:
    #print(p)
    addWord(p)


maxWords(my_words)
