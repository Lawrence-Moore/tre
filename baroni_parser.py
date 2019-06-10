def parse_command(commands, u):
    primitive = []
    current_words = []
    for i, word in enumerate(commands):
        # print(commands[:i+1], current_words, primitive)
        if word == 'walk':
            current_words.append(word)
        elif word == 'look':
            current_words.append(word)
        elif word == 'run':
            current_words.append(word)
        elif word == 'jump':
            current_words.append(word)

        elif current_words == ['turn'] and word == 'left':
            primitive.append('turn left')
            current_words = []
        elif current_words == ['turn'] and word == 'right':
            primitive.append('turn right')
            current_words = []

        elif len(current_words) > 1 and current_words[0] in u and current_words[1] == 'opposite' and word == 'left':
            primitive.append([['turn left', 'turn left'], current_words[0]])
            current_words = []
        elif len(current_words) > 1 and current_words[0] in u and current_words[1] == 'opposite' and word == 'right':
            primitive.append([['turn right', 'turn right'], current_words[1]])
            current_words = []

        elif len(current_words) > 1 and current_words[0] == "turn" and current_words[1] == 'opposite' and word == 'left':
            primitive.append([['turn left', 'turn left'], current_words[0]])
            current_words = []
        elif len(current_words) > 1 and current_words[0] == "turn" and current_words[1] == 'opposite' and word == 'right':
            primitive.append([['turn left', 'turn left'], current_words[1]])
            current_words = []

        elif current_words == ['turn', 'around'] and word == 'left':
            primitive.append(['turn left', 'turn left', 'turn left', 'turn left'])
            current_words = []
        elif current_words == ['turn', 'around'] and word == 'right':
            primitive.append(['turn right', 'turn right', 'turn right', 'turn right'])
            current_words = []

        elif len(current_words) > 1 and current_words[0] in u and current_words[1] == 'around' and word == 'left':
            primitive.append(['turn left', current_words[0], 'turn left', current_words[0], 
                'turn left', current_words[0], 'turn left', current_words[0]])
            current_words = []
        elif len(current_words) > 1 and current_words[0] in u and current_words[1] == 'around' and word == 'right':
            primitive.append(['turn right', current_words[0], 'turn right', current_words[0], 
                'turn right', current_words[0], 'turn right', current_words[0]])
            current_words = []

        elif current_words != [] and current_words[0] in u and word == 'left':
            primitive.append([current_words[0], 'left'])
            current_words = []
        elif current_words != [] and current_words[0] in u and word == 'right':
            primitive.append([current_words[0], 'right'])
            current_words = []

        elif word == 'turn':
            current_words.append("turn")
        elif word == 'around':
            current_words.append("around")
        elif word == 'opposite':
            current_words.append("opposite")       
        elif word == 'twice':
            if len(current_words) == 1 and current_words[0] in u:
                primitive.append(current_words[0])
            current_words = []
            primitive = primitive * 2
        elif word == 'thrice':
            if len(current_words) == 1 and current_words[0] in u:
                primitive.append(current_words[0])
            current_words = []
            primitive = primitive * 3
        elif word == 'and':
            if current_words != []:
                primitive += current_words
            return [primitive, parse_command(commands[i + 1:], u)] 
        elif word == 'after':
            if current_words != []:
                primitive += current_words
            return [parse_command(commands[i + 1:], u), primitive]
    if current_words != []:
        primitive += current_words
    return primitive

def parse_line(line):

    command, actions = line.split("IN: ")[1].split(" OUT: ")
    u = ['walk', 'look', 'run', 'jump']
    return command, actions, parse_command(command.split(), u)

file = open('baroni_dataset.txt', 'r')
f = open("baroni_dataset_ground_truth.txt","w+")

file_read = file.readlines()
for line in file_read:
    command, actions, comp = parse_line(line)
    f.write(str(comp) + "\n")
f.close()
file.close()
