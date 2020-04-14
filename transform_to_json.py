import json

with open("./fast_food.csv", 'r') as d:
    lines = d.readlines()
    restaurants = {
                    "McDonald's": [],
                    "Dominos": [],
                    "Wendy's": [],
                    "Popeyes": [],
                    "Burger King": [],
                    "Pizza Hut": [],
                    "KFC": [],
                    "Taco Bell": []
                }

    for line in lines[1:]:
        id, restaurant, description, calories, protein, fat, iron, sodium, cholesterol, carbohydrates, water = line.split(',')
        water = water.strip()  # get rid of \n
        item = {}
        item["id"] = id
        item["calories"] = calories
        item["sodium"] = sodium
        item["iron"] = iron
        item["cholesterol"] = cholesterol
        item["name"] = description
        item["carbs"] = carbohydrates
        item["protein"] = protein
        item["fat"] = fat
        item["water"] = water
        restaurants[restaurant].append(item)

with open("data.json", "w") as j:
    json.dump(restaurants, j, indent=4)
