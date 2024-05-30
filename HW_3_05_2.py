import json
import gzip

class MusicCatalog:
    def __init__(self):
        self.data = {}

    def add_group(self, group, albums):
        self.data[group] = albums

    def remove_group(self, group):
        if group in self.data:
            del self.data[group]
        else:
            print(f"{group} not found.")

    def search_group(self, group):
        if group in self.data:
            return self.data[group]
        else:
            return f"{group} not found."

    def edit_group(self, group, new_albums):
        if group in self.data:
            self.data[group] = new_albums
        else:
            print(f"{group} not found.")

    def save_data(self, filename):
        with gzip.open(filename, 'wb') as f:
            json.dump(self.data, f, ensure_ascii=False)

    def load_data(self, filename):
        with gzip.open(filename, 'rb') as f:
            self.data = json.load(f)

mc = MusicCatalog()

mc.add_group("The Beatles", ["Abbey Road", "Sgt. Pepper's Lonely Hearts Club Band"])
mc.add_group("Led Zeppelin", ["Led Zeppelin IV", "Physical Graffiti"])
mc.add_group("Pink Floyd", ["The Dark Side of the Moon", "Wish You Were Here"])

print(mc.search_group("The Beatles"))  # Виведе: ['Abbey Road', "Sgt. Pepper's Lonely Hearts Club Band"]

mc.edit_group("The Beatles", ["Let It Be", "Revolver"])

mc.remove_group("Led Zeppelin")

mc.save_data("music_catalog.json.gz")
mc.load_data("music_catalog.json.gz")

print(mc.data)