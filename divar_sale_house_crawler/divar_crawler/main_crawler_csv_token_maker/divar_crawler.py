import csv
import requests
import json
from time import sleep

data_file = open('token.csv', 'a')
token_csv_writer = csv.writer(data_file)
token_csv_writer.writerow(['district_num', 'token'])

def token_ditractor(district_num):
    main_url = "https://api.divar.ir/v8/web-search/tehran/buy-apartment?districts=%s" % str(district_num)
    getter_url(main_url, district_num)


url_tokens=[]
token_distriction_dict={}

def getter_url(url, district_num = None):
    sleep(0.1)
    getter = requests.get(url)
    try:
        json_data = json.loads(getter.text)
        widget_data = json_data.get("widget_list")
        for wid_data_content in widget_data:
            wid_data = wid_data_content["data"]
            token = wid_data["token"]
            token_csv_writer.writerow([district_num,token])
            url_tokens.append(token)
            print (token)
            print (url)


        if json_data["seo_details"].get("next"):
            next_page = json_data["seo_details"]["next"]
            next_url = f"https://api.divar.ir/v8/web-search/{next_page}"
            getter_url(next_url, district_num)
        else:
            token_distriction_dict[district_num]=url_tokens
            with open(f'divar_crawler/statics/{district_num}.json', 'a') as json_file:
                json.dump(token_distriction_dict, json_file, ensure_ascii=False)
            url_tokens.clear()
            token_distriction_dict.clear()
    except:
        print("token crawling in url:%s district:%s failed" %(url, district_num))



        """ write in one file """
# def token_ditractor(district_num):
#     with open('tokens.json', 'a') as json_file:
#         json_file.write("{")
#         main_url = "https://api.divar.ir/v8/web-search/tehran/buy-apartment?districts=%s" % str(district_num)
#         getter_url(main_url, district_num)
#         json_file.de
#         json_file.write("}")

# url_tokens=[]
# token_distriction_dict={}

# def getter_url(url, district_num = None):
#     getter = requests.get(url)
#     json_data = json.loads(getter.text)
#     widget_data = json_data["widget_list"]

#     for wid_data_content in widget_data:
#         wid_data = wid_data_content["data"]
#         token = wid_data["token"]
#         token_csv_writer.writerow([district_num,token])
#         url_tokens.append(token)
#         print (token)
#         print (url)


#     if json_data["seo_details"].get("next"):
#         next_page = json_data["seo_details"]["next"]
#         next_url = f"https://api.divar.ir/v8/web-search/{next_page}"
#         getter_url(next_url, district_num)
#     else:
#         token_distriction_dict[district_num]=url_tokens
#         with open('tokens.json', 'a') as json_file:
#             json_file.write("{")
#             json.dump(token_distriction_dict, json_file, ensure_ascii=False)
#             json_file.write(",")
#         url_tokens.clear()
#         token_distriction_dict.clear()