import csv
import requests
import json



def find_detail_with_token(district, token_list):
    with open('divar_crawler/divar_crawler/statics/csv/%s.csv' % district, 'a') as data_file:
        csv_writer = csv.writer(data_file)
        csv_writer.writerow(["slug", "category_title", "city",
                             "district", "latin_city", "meter", "built_year", "total_cost", "price_per_meter", "floor",
                             "room",
                             "elevator", "parking", "storage", "divder", "lat", "long", "token"])
        for token in token_list:
            print(token)
            print(district)
            title = description = slug = category_title = category = city = district = latin_city = meter = built_year = total_cost = price_per_meter = floor = room = elevator = parking = storage = divder = lat = long = None
            url = "https://api.divar.ir/v5/posts/%s" % token
            getter = requests.get(url)
            try:
                json_data = json.loads(getter.text)

                data = json_data.get('data')
                if data:
                    cate = data.get("category")
                    if cate:
                        category_title = cate.get("title")
                        slug = cate.get("slug")
                    city = data.get("city")
                    district = data.get("district")

                    webengage = data.get('webengage')
                    latin_city = webengage.get("city")
                    price = webengage.get("price")

                    widgets = json_data.get("widgets")
                    if widgets:
                        list_data = json_data.get("widgets").get("list_data")
                        for data_new in list_data:
                            if data_new.get("title"):
                                title = data_new["title"]
                                if title == "متراژ":
                                    meter = data_new["value"]
                                if title == "قیمت کل":
                                    total_cost = data_new["value"]
                                if title == "ساخت":
                                    built_year = data_new["value"]
                                if title == "قیمت هر متر":
                                    price_per_meter = data_new["value"]
                                if title == "طبقه":
                                    floor = data_new["value"]
                            if data_new.get("format"):
                                format = data_new.get("format")
                                if format == "group_feature_row":
                                    for item in data_new["items"]:
                                        if item["title"] == "آسانسور":
                                            elevator = 1
                                        if item["title"] == "پارکینگ":
                                            parking = 1
                                        if item["title"] == "انباری":
                                            storage = 1
                                    if data_new.get("has_divider"):
                                        divder = 1
                                if format == "group_info_row":
                                    for item in data_new["items"]:
                                        if item["title"] == "متراژ":
                                            meter = item["value"]
                                        if item["title"] == "اتاق":
                                            room = item["value"]
                                        if item["title"] == "ساخت":
                                            built_year = item["value"]
                        location = widgets.get('location')
                        if location:
                            lat = location.get('latitude')
                            long = location.get('longitude')

                        # global all_img
                        # all_img = []
                        # images = widgets.get('web_images')
                        # for img in images:
                        #     for image_add in img:
                        #         if image_add["type"] == "image/jpeg":
                        #             all_img.append(image_add["src"])

                    # web_url = json_data["data"]["share"]["web_url"]
                    # title = json_data["data"]["share"]["title"]
                    # description = json_data["data"]["share"]["description"]
                    dataset = [slug, category_title, city,
                               district, latin_city, meter, built_year, total_cost, price_per_meter, floor, room, elevator, parking,
                               storage, divder, lat, long, token]

                    # if len(all_img) > 0:
                    #     for image_url in all_img:
                    #         dataset.append(image_url)
                    #     all_img.clear()
                    csv_writer.writerow(dataset)
            except:
                print("oh oh iteration limitation")
