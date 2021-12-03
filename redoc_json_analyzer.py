import json

# with를 이용해 파일을 연다.
# json 파일은 같은 폴더에 있다고 가정!

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('start')

with open('C:\\Users\\최승건\\Desktop\\openapi_127_0_0_1.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

    # json_array_info = json_data["info"]
    # print(json_array_info)
    # print(json_array_info['title'])
    # print(json_array_info['version'])

    json_array_info_paths = json_data["paths"]
    # print(json_array_info_paths)

    # cnt = len(json_array_info_paths);
    # print('cnt : ',cnt)

    api_cnt = 1;
    for key, value in json_array_info_paths.items():
        method = ''
        method_cnt = 0
        method_tmp = []
        key_split = key.split('/')
        try:
            depth1 = key_split[2]
        except:
            depth1 = ''
        try:
            depth2 = key_split[3]
        except:
            depth2 = ''

        try:
            depth3 = key_split[4]
        except:
            depth3 = ''

        try:
            depth4 = key_split[5]
        except:
            depth4 = ''

        print(api_cnt, '"{}"'.format(key), '"{}"'.format(depth1), '"{}"'.format(depth2),
              '"{}"'.format(depth3), '"{}"'.format(depth4), end=', ')
        for subkey, subvalue in value.items():
            method_tmp.append(subkey+',')
            method_cnt+=1
        method = ''.join(method_tmp)
        print('"{}"'.format(method[0:len(method)-1]), method_cnt, '"{}"'.format(subvalue['summary']) )
        api_cnt += 1

    # json_array_info_components = json_data["components"]
    # print(json_array_info_components)
    #
    # json_object = json_data["info"]
    # print(json_object)

    # json_array = json_object["json_bool"]
    # print(json_bool)