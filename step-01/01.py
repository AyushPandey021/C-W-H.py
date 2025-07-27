import pyjokes

joke = pyjokes.get_joke()
print(joke)
# hey i am pyhtonista


# pratice capter -01

print(
    """😭😭bda
 samgaya tujhe smjh na aaya ye dil kya kenda h """
)


# for text  to voice in python  use pyttsx3
import pyttsx3

engine = pyttsx3.init()
engine.say("i am ayush and i am pythonista ")

engine.runAndWait()

# for os directory find  and see directorys
import os

directory_path = "/"
contents = os.listdir(directory_path)
for item in contents:
    print(item)
