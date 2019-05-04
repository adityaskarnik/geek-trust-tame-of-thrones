import random

animals = {'Land' : 'Panda', 'Water' : 'Octopus', 'Ice' : 'Mammoth', 'Air' : 'Owl', 'Fire' : 'Dragon', 'Space': 'Gorilla'}
all_kingdoms = ["Air", "Land", "Ice", "Fire", "Water", "Space"]
messages = []
allegiance = {'Land': [], 'Water': [], 'Ice': [], 'Air': [], 'Fire': [], 'Space': []}
winner = {}

def valar_morghulis(competing):
    for i in range(6):
        for kingdom in competing:
            if bool(animals):
                whoall = []
                random_message = random.choice(messages)
                messages.remove(random_message)
                if all([char in random_message.lower() for char in list(animals.keys())[0].lower()]): whoall.append(list(animals.keys())[0])
                [whoall.remove(i) for i in competing if i in whoall]
                [animals.pop(i, None) for i in whoall]
                allegiance[kingdom].append(whoall)
    for kingdom in competing:
        count = 0
        for i in allegiance[kingdom]:
            if len(i) > 0:
                count = count+1
        winner[kingdom] = count
        print("Allies for",kingdom,count)


messages_file = "/home/adityakarnik/Downloads/Python/GeekTrustTest/boc-messages.txt"
with open(messages_file,"r") as m:
    for message in m:
        message = message.replace(",\n","").replace("\"","").strip()
        messages.append(message)
while True:
    input_message = input("\n1. Who is the ruler of Southeros? \n2. Allies of Ruler? \n3. Enter Kingdoms competing to be the ruler: \n4. Type 'quit'\n\n")
    if input_message == "1":
        print("\nWho is the ruler of Southeros?")
        if (bool(winner) and winner[max(winner, key=winner.get)]>0):
            print(max(winner, key=winner.get))
        else:
            print("None")
    elif input_message == "2":
        print("\nAllies of Ruler?")
        if (bool(winner) and winner[max(winner, key=winner.get)]>0):
            print(next(i for i in allegiance[max(winner, key=winner.get)] if len(i) > 0))
        else:
            print("None")
    elif input_message == "3":
        competing = input("\nEnter Kingdoms competing to be the ruler: ").split()
        valar_morghulis(competing)
    else: break