import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Double check it"
        else:
            return "We didn't understand you're entry"
    else:
        return "The word doesn't exist. Double Check it"

word = input(" Enter a word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)
