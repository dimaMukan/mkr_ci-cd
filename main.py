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

def sort_area(data):
    sorted_area = sorted(data, key=lambda x: int(x[1]), reverse=True)
    return sorted_area


# print(read())
print(sort_area(read()))
