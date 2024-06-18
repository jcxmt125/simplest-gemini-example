# Really simple Gemini API usage in Python

## So, what is this?

This is possibly the simplest example I could create for Google's Gemini API, using API keys from their AI Studio. The project was made to experiment with some concepts, like a *requirements.txt* file for listing out required packages, and a *.env* file to store my API keys... without it being published on Github as a public repository. (Really, keep your keys private!)

## How can I use this?

First, pull this Github repo, download it, or... well, since this really is a small project, you could just copy the code from my Python files! 

You'll need an API Key from Google's [AI studio](https://aistudio.google.com). Get one, and put it in a .env file in your working directory with the variable name GEMINI_API_KEY. It's free up to a certain amount of requests per day, and you can even create one without billing attached! Though, the free tier varies with model... the 1.5 flash model should have more than enough requests for yourself.

After you're done with that, go ahead and install the dependancies... there are only two, google-generativeai and python-dotenv! I've still created a requirements.txt file, but... you probably won't even need that. Just run "pip install -U google-generaticeai python-dotenv" (or, pip install -r requirements.txt) and you should be good to go! When ready, run the "textPrompt.py" in your terminal. If you double-click to run on windows, it'll close as soon as you get a response... which isn't great!

## It's throwing an error!

Is it a dependancy error? Then, look at the error message itself for clues...
Did you make the .env file, by the way? It isn't something like ".env.txt", the file name itself should be ".env". Windows' default setting hides extensions... Please check that. 
If even that isn't working, you might be experiencing a rate limit (especially if you're using the 1.5 Pro varient), or the API might just... be down. That sometimes happens... In either case, try waiting a few minutes then trying again!
If you can't install dependancies, make sure your platform supports the google-generativeai package. For example, I couldn't get it to run under a Termux environment on android...

## Why did you make this?

Before this I didn't know how to deal with .env files... and put them in plaintext into my code. *If you haven't noticed, that's a bad idea.* So, this was created to experiment with doing just that, making a .env file! Oh, and it's also my first time making a public Github repo... and making a readme.md file for that matter, and also the first time I used requirements.txt. I wanted to make this so my friends could use this as a very basic introduction to some concepts, and possibly random strangers on the internet, too! (The Gemini API is cool too! I might get around to adding image/video/audio processing demos someday since the API does support that.)