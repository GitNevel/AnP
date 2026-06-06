class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print(f"Раб {self.name} наводит порядок.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=6.7, cleaner_name="Нет"):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = Cleaner(cleaner_name)

    def describe_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» | Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Харчевня «{self.restaurant_name}» открыта!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, location, working_hours, flavors=None):
        super().__init__(restaurant_name, cuisine_type)

        self.location = location
        self.working_hours = working_hours

        self.flavors = flavors if flavors else []

        self.types_inventory = {
            "на палочке": [],
            "в стаканчике": [],
            "в упаковке": []
        }

    def show_flavors(self):
        print(f"\n Меню «{self.restaurant_name}» ")
        if self.flavors:
            print("Сорта: " + ", ".join(self.flavors))
        else:
            print("Нужно больше мороженого.")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"[+] Вкус '{flavor}' добавлен в меню.")
        else:
            print(f"[!] Вкус '{flavor}' уже в меню.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"[-] Вкус '{flavor}' удален.")
        else:
            print(f"[!] Вкуса '{flavor}' больше нет.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"[?] Вкус '{flavor}' есть !")
            return True
        else:
            print(f"[?] Вкуса '{flavor}' сейчас нет.")
            return False

    def add_specific_type(self, ice_cream_type, flavor):
        if ice_cream_type not in self.types_inventory:
            self.types_inventory[ice_cream_type] = []

        if flavor not in self.types_inventory[ice_cream_type]:
            self.types_inventory[ice_cream_type].append(flavor)
            print(f"[+] В категорию '{ice_cream_type}' добавлен вкус '{flavor}'.")

    def show_specific_type(self, ice_cream_type):
        if ice_cream_type in self.types_inventory and self.types_inventory[ice_cream_type]:
            flavors_str = ", ".join(self.types_inventory[ice_cream_type])
            print(f"Мороженое типа '{ice_cream_type}': {flavors_str}")
        else:
            print(f"Для типа '{ice_cream_type}' пока нет других вкусов.")




print("ТЕСТ 11.1")
my_ice_cream_stand = IceCreamStand(
    restaurant_name="Морозилка",
    cuisine_type="Кафе-мороженое",
    location="Садовая 52, Большая морская 52, Санкт-Петербург, 190000",
    working_hours="05:00 - 24:00",
    flavors=["Ванильное", "Шоколадное", "Клубничное"]
)

my_ice_cream_stand.show_flavors()




print("\n11.2а")
print(f"Локация: {my_ice_cream_stand.location}")
print(f"Время нашей job'ы: {my_ice_cream_stand.working_hours}")

print("\n11.2б")
my_ice_cream_stand.add_flavor("Ванильное")
my_ice_cream_stand.add_flavor("Шоколадное")
my_ice_cream_stand.remove_flavor("Радужное")
my_ice_cream_stand.show_flavors()

print("\n11.2в")
my_ice_cream_stand.check_flavor("Ванильное")
my_ice_cream_stand.check_flavor("Клубничное")

print("\n11.2г")
my_ice_cream_stand.add_specific_type("на палочке", "Фруктовый лед")
my_ice_cream_stand.add_specific_type("в упаковке", "Сливочное")
my_ice_cream_stand.add_specific_type("в упаковке", "Шоколадное")
my_ice_cream_stand.add_specific_type("в стаканчике", "Пломбир")  # Добавляем новый тип на лету
my_ice_cream_stand.show_specific_type("в упаковке")
my_ice_cream_stand.show_specific_type("на палочке")
my_ice_cream_stand.show_specific_type("в стаканчике")