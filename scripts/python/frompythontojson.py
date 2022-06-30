import json

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

dataset = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


def convertToJson(meta):
    with open('example.json', 'w') as file:
        json.dump(dataset, file)



if __name__ == '__main__':
    convertToJson(dataset)
