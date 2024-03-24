meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "DOXEAR": "Robar informacion de una persona",
            "CAMPEAR": "Estar escondido en un lugar para matar alas personas",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }
word = input("Escriba una palabra moderna que no entienda (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no se encuentra en el diccionario LOL")
