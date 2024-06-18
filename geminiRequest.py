from dotenv import load_dotenv
import os
#So this imports the dotenv file...

load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
#Just make sure you have the key in a .env file on your working directory.

#This will initialize the model!
genai.configure(api_key=GEMINI_API_KEY)

#Here's the actual code that handles whatever you put into the text...
#You can see there is also a maxtoken attribute. Adjust that to your liking!
def gemrequest(prompt, maxtoken = 8000, model = 'gemini-1.5-flash-latest'):
    model = genai.GenerativeModel(model)

    response =  model.generate_content(prompt, generation_config=genai.types.GenerationConfig(max_output_tokens=maxtoken))

    if not (response.prompt_feedback.block_reason == response.prompt_feedback.BlockReason(0)):
        #This means it was blocked from responding due to some reason...
        print("Response blocked. See following for reason:")
        print()
        return (False, response.prompt_feedback)
    else:
        return (True, response.text)

if __name__ == "__main__":
    #An even simpler test to see this script works at all. Run this file directly to execute this, as it won't run when imported!
    print(gemrequest(input("Text to send: ")))