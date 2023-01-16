import json
import csv

ADS_DATA = "../datasets/data_with_csv/ad.csv"
CATEGORIES_DATA = "../datasets/data_with_csv/categories.csv"
USER_DATA = "../datasets/data_with_csv/user.csv"
LOCATION_DATA = "../datasets/data_with_csv/location.csv"


def read_file(data, json_file, model):
    result = []
    try:
        with open(data, 'r', encoding='utf-8') as f:
            for line in csv.DictReader(f):
                add_to_dict = {
                    'model': model,
                    'pk': int(line['Id'] if 'Id' in line else line['id']),
                }
                if 'id' in line:
                    del line['id']
                else:
                    del line['Id']

                if "is_published" in line:
                    if line["is_published"] == 'TRUE':
                        line["is_published"] = True
                    else:
                        line["is_published"] = False

                if "price" in line:
                    line["price"] = int(line["price"])

                if "category_id" in line:
                    line["category"] = [int(line["category_id"])]
                    del line["category_id"]

                if "author_id" in line:
                    line["author"] = int(line["author_id"])
                    del line["author_id"]

                if "location_id" in line:
                    line["location"] = int(line["location_id"])
                    del line["location_id"]

                if "age" in line:
                    line["age"] = int(line["age"])

                add_to_dict['fields'] = line
                result.append(add_to_dict)

        with open(json_file, 'w', encoding='utf-8') as j_f:
            j_f.write(json.dumps(result, ensure_ascii=False))

    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    read_file(data=ADS_DATA, json_file="ads.json", model="ads.ad")
    read_file(data=CATEGORIES_DATA, json_file="categories.json", model="category.category")
    read_file(data=USER_DATA, json_file="user.json", model="user.user")
    read_file(data=LOCATION_DATA, json_file="location.json", model="location.location")
