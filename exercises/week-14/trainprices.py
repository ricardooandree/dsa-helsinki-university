""" Description:
You are given information about train connections between cities. Each connection is bi-directional and has a certain price, which is the same in both directions.
Your task is to compute a price table that shows the lowest cost of traveling between all cities using train connections. 
The table is represented using nested lists, and it should include the names of the cities as well as the prices. The cities should be in alphabetical order.
If there is no route, the table should show -1 as the price. An example of the table is given in the code template below.
The class should have the following methods:

    add_city: adds a new city
    add_train: adds a train connection between two cities
    find_prices: returns the price table

You can assume that, when the method add_train is called, both cities have been added previously using the method add_city.
In a file trainprices.py, implement the class TrainPrices according to the following template.
"""


class TrainPrices:
    def __init__(self):
        # TODO
        pass

    def add_city(self, name):
        # TODO
        pass

    def add_train(self, city1, city2, price):
        # TODO
        pass

    def find_prices(self):
        # TODO
        pass

if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)

    print(t.find_prices())

    # method's expected output:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]