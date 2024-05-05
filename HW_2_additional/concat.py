with open("names.txt","r") as source_1:
    with open("first-names.txt","r") as source_2:
        with open("NAMES.txt","w") as dest:
            for line in source_1:
                dest.write(line)
            for line in source_2:
                l = line.lower()
                dest.write(l)