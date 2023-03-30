import re

def read():
    a:list = []
    with open("res.txt","w") as res_file:
        with open("text.txt","r") as info_file:
            for i in info_file:
                s = re.sub(r'[\n]', '', i)
                a.append(s)
        data = [line.strip().split(',') for line in a]
    return data

print(read())