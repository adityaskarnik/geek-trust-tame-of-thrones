animals = {'Land' : 'Panda', 'Water' : 'Octopus', 'Ice' : 'Mammoth', 'Air' : 'Owl', 'Fire' : 'Dragon'}

whoall = []

while True:
    input_message = input("1. Who is the ruler of Southeros? \n2. Allies of Ruler? \n3. Input Messages to kingdoms from King Shan \n4. Type 'quit'\n")
    if input_message == "1":
        if len(whoall) > 2:
            print("King Shan")
        else: 
            print("None")
    elif input_message == "2":
        if (len(whoall) > 0):
            print(whoall)
        else:
            print("None")
    elif input_message == "3":
        message = input("Enter the message: ")
        for key, value in animals.items():
            if all([char in message.lower() for char in value.lower()]): whoall.append(key)
    else: break