import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

#print(parsed_data)
# organized_parsed_data = []
# for i in range(len(parsed_data)):
#     empty_dict = {}
#     empty_dict['company'] = parsed_data[i]['company']['name']
#     empty_dict['lat'] = parsed_data[i]['address']['geo']['lat']
#     empty_dict['lng'] = parsed_data[i]['address']['geo']['lng']
#     empty_dict['name'] = parsed_data[i]['name']
#     organized_parsed_data.append(empty_dict)

# dummy_data = []
# for searched_people in range(10):
#     if -80 < int(float(organized_parsed_data[searched_people]['lat'])) < 80 and -80 < int(float(organized_parsed_data[searched_people]['lng'])) < 80:
#         dummy_data.append(organized_parsed_data[searched_people])
#     else:
#         continue
# print(dummy_data)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

# def create_user():
#     censored_user_list = {}
#     for i in range(len(parsed_data)):
#         empty_list = []
#         empty_list.append(parsed_data[i]['name'])
#         print(empty_list)
#         censored_user_list[parsed_data[i]['company']['name']] = empty_list
#         print(censored_user_list)
#         censorship(censored_user_list)
#         if True:
#             del censored_user_list[[parsed_data[i]['company']['name']]]
#     return censored_user_list



def censorship(user_list):
    for company in user_list:
        if company in black_list:
            print(f'{company} 소속의 {user_list[company][0]} 은/는 등록할 수 없습니다')
            return False
        else:
            print('이상 없습니다.')
            return True

censored_user_list = {}
for i in range(len(parsed_data)):
    empty_list = []
    empty_list.append(parsed_data[i]['name'])
    censored_user_list[parsed_data[i]['company']['name']] = empty_list
print(censored_user_list)


censorship(censored_user_list)
if True:
    pass
else:
    del censored_user_list[[parsed_data[i]['company']['name']]]

#return censored_user_list



#print(create_user())