# dictionary of animals and there emblem
animals = {'Land' : 'Panda', 'Water' : 'Octopus', 'Ice' : 'Mammoth', 'Air' : 'Owl', 'Fire' : 'Dragon'}
# empty list to add the final allies
whoall = []

class GoldenCrown():

    def allies(self):
        while True:
            # to accept the what the user wants to check
            input_message = input("\n1. Who is the ruler of Southeros? \n2. Allies of Ruler? \n3. Input Messages to kingdoms from King Shan \n4. Type 'quit'\n\n")
            if input_message == "1":
                if len(whoall) > 2:
                    print("King Shan")
                else: 
                    print("None")
            elif input_message == "2":
                # to check and print the allies of king shah
                if (len(whoall) > 0):
                    print(whoall)
                else:
                    print("None")
            elif input_message == "3":
                # getting user input for the message to be sent to allies
                message = input("Enter the message: ")
                for key, value in animals.items():
                    # reading the message from the input and checking each character
                    # and matching with the dictionary
                    # all() will return the values if true,
                    # then add that current key to the final allies list
                    if all([char in message.lower() for char in value.lower()]): whoall.append(key)
            else: break