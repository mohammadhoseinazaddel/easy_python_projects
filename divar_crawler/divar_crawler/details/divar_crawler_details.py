import csv
import requests
import json


n=4

data_file = open('divar_crawler/details/detailsoutput.csv', 'w')
csv_writer = csv.writer(data_file)
csv_writer.writerow(["title", "slug", "category_title", "category", "city",
                   "district", "latin_city", "meter", "built_year", "total_cost", "price_per_meter", "floor", "room", "elevator", "parking", "storage", "divder", "description"])
title=description=slug=category_title=category=city=district=latin_city=meter=built_year=total_cost=price_per_meter=floor=room=elevator=parking=storage=divder=None
for i in range(n):
    url = "http://api.divar.ir/v8/web-search/tehran/buy-residential?page=%s" % str(n)
    getter = requests.get(url)
    json_data = json.loads(getter.text)
    widget_data = json_data["widget_list"]
    for wid_data_content in widget_data:
        wid_data = wid_data_content["data"]
        token = wid_data["token"]
        print(token)
        url = "https://api.divar.ir/v5/posts/%s" % token
        getter = requests.get(url)
        json_data = json.loads(getter.text)
        title = json_data["data"]["share"]["title"]
        description = json_data["data"]["share"]["description"]
        slug = json_data["data"]["category"]["slug"]
        category_title = json_data["data"]["category"]["title"]
        category = json_data["data"]["category"]["second_slug"]
        # address = json_data["data"]["business_data"]["data"]["address"]
        # shortAddress = json_data["data"]["business_data"]["data"]["shortAddress"]
        # telephoneNumber = json_data["data"]["business_data"]["data"]["telephoneNumber"]
        city = json_data["data"]["city"]
        district = json_data["data"]["district"]
        latin_city = json_data["data"]["webengage"]["city"]
        list_data = json_data["widgets"]["list_data"]
        for data_new in list_data:
            if data_new["title"]:
                title = data_new["title"]
                if title=="متراژ":
                    meter = data_new["value"]
                if title=="قیمت کل":
                    total_cost = data_new["value"]
                if title=="ساخت":
                    built_year = data_new["value"]
                if title=="قیمت هر متر":
                    price_per_meter = data_new["value"]
                if title=="طبقه":
                    floor = data_new["value"]
            if data_new["format"]:
                if data_new["format"] == "group_feature_row":
                    for item in data_new["items"]:
                        if item["title"] == "آسانسور":
                            elevator = 1
                        if item["title"] == "پارکینگ":
                            parking = 1
                        if item["title"] == "انباری":
                            storage = 1
                    if data_new["has_divider"]:
                        divder = 1
                if data_new["format"] == "group_info_row":
                    for item in data_new["items"]:
                        if item["title"] == "متراژ":
                            meter = item["value"]
                        if item["title"] == "اتاق":
                            room = item["value"]
                        if item["title"] == "ساخت":
                            built_year = item["value"]
        images_add=[]
        if json_data["widgets"]["web_images"]:
            for img in json_data["widgets"]["web_images"]:
                for image_add in img:
                    if image_add["type"] == "image/jpeg":
                        images_add.append(image_add["src"])


        web_url = json_data["data"]["share"]["web_url"]
        dataset = [title, slug, category_title, category, city,
                   district, latin_city, meter, built_year, total_cost, price_per_meter, floor, room, elevator, parking, storage, divder, description]
        csv_writer.writerow(dataset)
