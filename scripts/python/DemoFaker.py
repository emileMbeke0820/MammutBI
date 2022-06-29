from faker import Faker

fake_data = Faker()


def createAndSaveData():
    table = []
    for x in range(10):
        table.append({"a": fake_data.user_name(), "b": fake_data.address()})
    return table


# Dictionnary kann in List umgewandelt werden!
# Jasoondump machen

if __name__ == '__main__':
    dataset = createAndSaveData()
    print(dataset)
