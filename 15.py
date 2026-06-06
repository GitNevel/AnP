import json

with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

name = input("Введите название продукта: ")
price = int(input("Введите цену: "))
available_str = input("В наличии? (да/нет): ").strip().lower()
available = available_str == 'да'
weight = int(input("Введите вес: "))

data["products"].append({
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
})

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

for item in data['products']:
    print(f"Название: {item['name']}")
    print(f"Цена: {item['price']}")
    print(f"Вес: {item['weight']}")
    print("В наличии\n" if item['available'] else "Нет в наличии!\n")