#You could just copy the code here, too!
#Think of this as a demo for importing from your own Python files.
#Erroring out? Make sure your working directory is correct...
from geminiRequest import gemrequest

#These are the list of models available... it might change as this code ages. Replace with what you'd like after looking at the documentation for Gemini!
models = ["gemini-1.5-flash-latest", "gemini-1.5-pro-latest", "gemini-1.0-pro"]

#The below lets you choose an arbitrary model from the above list! THe first one (0th index) will be default.
print("(Default) ", end="")

for i in range(len(models)):
    print(str(i), ":", models[i])

modelChoose = input("select model #")

if modelChoose == "":
    modelChoose = 0

modelChoose = int(modelChoose)

txtmodel = models[modelChoose]

#What would you like to ask the AI? The API doesn't remember what you said to it... so this will be a one-turn conversation.
#Useful if you just want a single task done. 
result = gemrequest(input("Text to send: "), model=txtmodel)

if result[0]:
    #The request succeded! Yay!
    print(result[1])
else:
    #Uh... it failed. Let's see what went wrong...
    print("The prompt was blocked! See below for reason:")
    print(result[1])