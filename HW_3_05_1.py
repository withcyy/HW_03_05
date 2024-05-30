import json
import gzip

class CountryCapitals:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
        else:
            print(f"{country} not found")

    def search_country(self, country):
        if country in self.data:
            return  self.data[country]
        else:
            print(f"{country} not found")

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
        else:
            print(f"{country} not found")

    def save_data(self, filename):
        with gzip.open(filename, 'wb') as f:
            json.dump(self.data, f)

    def load_data(self, filename):
        with gzip.open(filename, 'rt') as f:
            self.data = json.load(f)

cc = CountryCapitals()
cc.add_country("Ukraine", "Kyiv")
cc.add_country("France", "Paris")
cc.add_country("Germany", "Berlin")

print(cc.search_country("Ukraine"))
cc.edit_country("Ukraine", "Lviv")
cc.remove_country("Germany")
cc.save_data("countries.json")
cc.load_data("countries.json")
print(cc.data)