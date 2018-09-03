import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored
title = colored(figlet_format("DAD JOKE 9000!"), color="yellow", attrs =["blink"])
print(title)

url = "https://icanhazdadjoke.com/search"
user_search = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(
	url,
	headers={"Accept": "application/json"},
    params={
    	"term": user_search,
    	"limit": 20
    }
)
data = response.json()
if data["total_jokes"] == 0:
	print (f"Sorry, I'dont have any jokes about {user_search}! Please try again.")
else:
	answer = choice(data["results"])
	print (f"I found {data['total_jokes']} joke(s) about {user_search}. Here's one: ")
	print (answer["joke"])