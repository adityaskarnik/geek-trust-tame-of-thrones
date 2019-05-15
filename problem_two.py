import random
import os
cwd = os.getcwd()
# declaring dictionary the ruler and its emblem 
animals = {'Land' : 'Panda', 'Water' : 'Octopus', 'Ice' : 'Mammoth', 'Air' : 'Owl', 'Fire' : 'Dragon', 'Space': 'Gorilla'}
# list of all the 6 kingdoms
all_kingdoms = ["Air", "Land", "Ice", "Fire", "Water", "Space"]
messages = []
# empty values dictionary to add the allies of the kingdom
allegiance = {'Land': [], 'Water': [], 'Ice': [], 'Air': [], 'Fire': [], 'Space': []}
winner = {}

class BreakerOfChains():

    """
    function to selecting a random message from message list and validating it with kingdom's emblem
    also remove checking and remove the kingdom which is already in competing list
    else adding the kindom to the allegiance of that kingdom
    also returning the number if allies each kingdom has
    """
    def valar_morghulis(self, competing):
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

    def ruler(self):
        # reading all messages from the boc-messages.txt
        messages_file = cwd+"/boc-messages.txt"
        with open(messages_file,"r") as m:
            for message in m:
                message = message.replace(",\n","").replace("\"","").strip()
                messages.append(message)
        while True:
            # to accept the what the user wants to check
            input_message = input("\n1. Who is the ruler of Southeros? \n2. Allies of Ruler? \n3. Enter Kingdoms competing to be the ruler: \n4. Type 'quit'\n\n")
            if input_message == "1":
                print("\nWho is the ruler of Southeros?")
                # checking from the winner list who has the maximum support number
                # print the winner kingdom
                if (bool(winner) and winner[max(winner, key=winner.get)]>0):
                    print(max(winner, key=winner.get))
                else:
                    print("None")
            elif input_message == "2":
                print("\nAllies of Ruler?")
                # getting the winner and the which kingdom are giving the support
                if (bool(winner) and winner[max(winner, key=winner.get)]>0):
                    print(next(i for i in allegiance[max(winner, key=winner.get)] if len(i) > 0))
                else:
                    print("None")
            elif input_message == "3":
                competing = input("\nEnter Kingdoms competing to be the ruler: ").split()
                self.valar_morghulis(competing)
            else: break