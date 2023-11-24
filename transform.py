'''
changeFormat(string) -> string
Transforms a string in the format "Aa Bb Cc, Dd Ee Ff, Gg Hh Ii" to "aabbcc, ddeeff, gghhii"
'''
def changeFormat(string):
    L = string.split(", ")
    for i in range(len(L)):
        L[i] = L[i].lower().replace(" ", "")
        L[i] = L[i].replace("á", "a")
        L[i] = L[i].replace("é", "e")
        L[i] = L[i].replace("í", "i")
        L[i] = L[i].replace("ó", "o")
        L[i] = L[i].replace("ú", "u")
        L[i] = L[i].replace("ñ", "n")
        L[i] = L[i].replace("Á", "a")
        L[i] = L[i].replace("É", "e")
        L[i] = L[i].replace("Í", "i")
        L[i] = L[i].replace("Ó", "o")
        L[i] = L[i].replace("Ú", "u")

    res = ""
    for i in range(len(L)):
        res += L[i]
        if i != len(L) - 1:
            res += ", "
    return res
assert changeFormat("Aa Bb Cc, Dd Ee Ff, Gg Hh Ii") == "aabbcc, ddeeff, gghhii"
assert changeFormat("Áa Bb Cc, Dd Ée Ff, Gg Hh Íi") == "aabbcc, ddeeff, gghhii"


'''
stripList(list) -> list
Deletes the spaces at the beginning and end of each string in a list
'''
def stripList(L):
    for i in range(len(L)):
        L[i] = L[i].strip()
    return L
assert stripList(["  a", "b  ", "  c  "]) == ["a", "b", "c"]

# open data.json

import json

with open("prompts.json", "r") as f:
    data = json.load(f)

new_data = {"prompts_styles": [], "prompts_concepts": {}}

new_data["prompts_styles"] = data["prompts_styles"]

for llave in data["prompts_concepts"]:
    new_llave = changeFormat(llave)
    new_data["prompts_concepts"][new_llave] = {}
    # esp_prompts
    new_data["prompts_concepts"][new_llave]["esp_prompts"] = stripList(data["prompts_concepts"][llave]["esp_prompts"])
    # eng_prompts
    new_data["prompts_concepts"][new_llave]["eng_prompts"] = stripList(data["prompts_concepts"][llave]["eng_prompts"])

# guardar en res.json
with open("res.json", "w") as f:
    json.dump(new_data, f, indent=4)