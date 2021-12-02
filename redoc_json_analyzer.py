import json

# with를 이용해 파일을 연다.
# json 파일은 같은 폴더에 있다고 가정!

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('start')

with open('/Users/choiseunggun/Downloads/openapi_127_0_0_1.json') as json_file:
    json_data = json.load(json_file)

    # json_array_info = json_data["info"]
    # print(json_array_info)
    # print(json_array_info['title'])
    # print(json_array_info['version'])

    json_array_info_paths = json_data["paths"]
    # print(json_array_info_paths)

    cnt = len(json_array_info_paths);
    # print('cnt : ',cnt)

    cnt = 1;
    for key, value in json_array_info_paths.items():
        for subkey, subvalue in value.items():
            print(cnt, key,subkey,'"',subvalue['summary'],'"')
            cnt=cnt+1

    # json_array_info_components = json_data["components"]
    # print(json_array_info_components)
    #
    # json_object = json_data["info"]
    # print(json_object)

    # json_array = json_object["json_bool"]
    # print(json_bool)