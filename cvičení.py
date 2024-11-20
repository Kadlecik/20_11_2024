"""
# ukol1

class moje:
    def __init__(self, mesto, region, zeme,pocet_obcanu, psc, predcisli):
        self.mesto = mesto
        self.region = region
        self.zeme = zeme
        self.pocet_obcanu = pocet_obcanu
        self.psc = psc
        self.predcisli= predcisli
    def get_info(self):
        return f"město {self.mesto} v regionu {self.region} ze země {self.zeme} s počtem občanů {self.pocet_obcanu} poštovní směrovací číslo {self.psc} s předčíslím {self.predcisli}."

h1 = moje ("Velké Vselisy", "středočeský kraj","česká republika", "326", "29427", "0")
print (h1.get_info())
print(h1)


#ukol4
class zlomek:
    def __init__(self, citatel, jmenovatel):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

f = zlomek(1 , 2)
print (f)


class letadlo:
    def __init__ (self , pasazer):
        self.name = name
        self.pasazer = pasazer

    def __eq__(self, other):
        return self.nema == other.name and self.pasazer == other.pasazer

    def __add__(self, other):
        pass

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
"""
import csv
class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __iadd__(self, passengers):
        self.current_passengers += passengers
        return self

    def __isub__(self, passengers):
        self.current_passengers -= passengers
        return self

    def __add__(self, passengers):
        new_plane = Airplane(self.airplane_type, self.max_passengers)
        new_plane.current_passengers = self.current_passengers + passengers
        return new_plane

    def __sub__(self, passengers):
        new_plane = Airplane(self.airplane_type, self.max_passengers)
        new_plane.current_passengers = self.current_passengers - passengers
        return new_plane

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __str__(self):
        return f"Airplane(type={self.airplane_type}, max_passengers={self.max_passengers}, current_passengers={self.current_passengers})"

    def save_to_csv(self, param):
        pass


# Příklad použití
plane1 = Airplane("Boeing 747", 416)
plane2 = Airplane("Airbus A380", 853)

print(plane1 == plane2)  # False, různé typy letadel

plane1 += 50
print(plane1)  # Aktuální počet cestujících: 50

plane1 -= 10
print(plane1)  # Aktuální počet cestujících: 40

print(plane1 > plane2)  # False, Airbus A380 má vyšší kapacitu
print(plane1 < plane2)  # True, Boeing 747 má nižší kapacitu
plane1.save_to_csv ("plane1.csv")

