import json
from difflib import get_close_matches
data = json.load(open("list_of_words.json"))

def translate(wo):
    wo = wo.lower()
    if wo in data:
        return data[wo]
    elif wo.title() in data:
        return data[wo.title()]
    elif wo.upper() in data:
        return data[wo.upper()]
    elif len(get_close_matches(wo, data.keys())) > 0:
        response = input("Did you mean %s? Y or N: " % get_close_matches(wo, data.keys())[0])
        response = response.lower()
        if response == "y":
            return data[get_close_matches(wo, data.keys())[0]]
        elif response == "n":
            return "Word not in dictionary"
        else:
            return "Word not in dictionary"
    else:
        return "Word not in dictionary"

word = input("Enter word: ")
result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
