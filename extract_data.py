iterattion = 1000

with open("./8 feb/data/Pet_Supplies.json", "r")as in_file:
    with open (f"./8 feb/data/Pet_supplies_{iterattion}.json", "w")as out_file:
        for _ in range(iterattion):
            line = in_file.readline()
            out_file.write(line)