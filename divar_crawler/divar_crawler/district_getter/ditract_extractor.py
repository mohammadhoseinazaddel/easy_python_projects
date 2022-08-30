import requests
import json

start_urls = 'https://api.divar.ir/v8/web-search/tehran/buy-residential'
getter = requests.get(start_urls)

data = json.loads(getter.text)
districts = data['input_suggestion']['json_schema']['properties']['districts']['properties']['vacancies']['items']['enum']
districts_name = data['input_suggestion']['json_schema']['properties']['districts']['properties']['vacancies']['items']['enumNames']
def district_extractor():
    with open('districts_num_name.json', 'w') as json_file:
        final_dic={}
        counter=0
        for dist_num in districts:
            final_dic[districts_name[counter]]=dist_num
            counter+=1
        json.dump(final_dic, json_file, ensure_ascii=False)
            
    with open('districts_numbers.json', 'w') as json_file:
        json.dump(districts, json_file, ensure_ascii=False)