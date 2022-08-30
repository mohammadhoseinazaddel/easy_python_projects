import json
from divar_crawler.district_getter.ditract_extractor import district_extractor
from divar_crawler.main_crawler_csv_token_maker.divar_crawler import token_ditractor
from divar_crawler.data_getter_with_token.data_getter_with_token import find_detail_with_token


def token_extractor():
    district_extractor()
    with open('districts_numbers.json', 'r') as f:
        districts = json.load(f)
        for district in districts:
            token_ditractor(district)


def details_extractor(district=None):
    # TODO should read csv tokens and get details for every one of them
    if district:
        detail_token_extractor(district)
    else:
        with open('districts_numbers.json', 'r') as f:
            districts = json.load(f)
            for district in districts:
                detail_token_extractor(district)


def detail_token_extractor(district):
    name_file = "divar_crawler/divar_crawler/statics/%s.json" % district
    try:
        with open(name_file, 'r') as f:
            json_data = json.load(f)
        token_list = json_data[district]
        find_detail_with_token(district, token_list)
    except:
        print("%s.json doenot exist" % (district))


if __name__ == "__main__":
    new_token = input("do you want new tokens it will take a while hahahaha: y/n  ")
    if new_token == "y":
        token_extractor()

    district_selected = input("do you want special district if yes type its code otherwise type 0: RestrictNumber/0 ")
    # TODO search name of district and retur its code
    if district_selected == "0":
        details_extractor()
    else:
        details_extractor(district_selected)
