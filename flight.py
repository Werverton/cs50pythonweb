from tokenize import PseudoExtras
from xmlrpc.client import Boolean


class Flight:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name) -> Boolean:
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers) #subtrai a capacidade pelo número de passageiros adcionados na lista


flight = Flight(3) #instanciei flight

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print("No available seat")
###
