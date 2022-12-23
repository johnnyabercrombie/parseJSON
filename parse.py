# Write a function to parse a JSON string into a dictionary

json = """
    {
        "test": "123",
        "comma,value": "comma,value",
        "number": 123,
        "string": "123"
    }
"""

def parseJson(string):
    startedWord = False
    startedInt = False
    key = ""
    word = ""
    output = {}

    for char in string:
        if char == "\"":
            if startedWord:
                # End of word
                startedWord = False

                if key:
                    output[key] = word
                    key = ""
                else:
                    key = word

                word = ""
            else:
                startedWord = True
        elif startedWord:
            word += char
        elif char.isdigit():
            word += char
            startedInt = True
        elif startedInt:
            output[key] = int(word)
            key = ""
            word = ""
            startedInt = False

    return output

output = parseJson(json)
assert output == {'test': '123', 'comma,value': 'comma,value', 'number': 123, 'string': '123'}
