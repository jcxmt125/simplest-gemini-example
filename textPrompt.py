from geminiRequest import gemrequest

models = ["gemini-1.5-flash-latest", "gemini-1.5-pro-latest", "gemini-1.0-pro"]

print("(Default) ", end="")

for i in range(len(models)):
    print(str(i), ":", models[i])

modelChoose = int(input("select model #"))

if modelChoose == "":
    modelChoose = 0

txtmodel = models[modelChoose]

result = gemrequest(input("Text to send: "), model=txtmodel)

if result[0]:
    print(result[1])
else:
    print("The prompt was blocked! See below for reason:")
    print(result[1])