class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print(f"Раб {self.name} убираеться.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=6.7, cleaner_name="Нет"):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        self.rating = rating

        self.cleaner = Cleaner(cleaner_name)

    def describe_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» | Кухня: {self.cuisine_type} | Текущий рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Харчевня «{self.restaurant_name}» открыта!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана «{self.restaurant_name}» обновлен до {self.rating}.")

    def start_cleaning(self):
        print(f"[Менеджер]: Навести порядок в «{self.restaurant_name}»!")
        self.cleaner.clean()

print("10.1")
newRestaurant = Restaurant("Макшнакнакс", "Питерская", cleaner_name="Артур Пирожков")

print(f"Название: {newRestaurant.restaurant_name}")
print(f"Тип кухни: {newRestaurant.cuisine_type}")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

print("\n10.2")
restaurant_1 = Restaurant("Rosstics", "Американская")
restaurant_2 = Restaurant("Мурино", "Русская")
restaurant_3 = Restaurant("Москва", "Грузинская")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("\n10.3")
restaurant_1.describe_restaurant()
restaurant_1.update_rating(4.8)
restaurant_1.describe_restaurant()

print("\n10.4")
newRestaurant.start_cleaning()