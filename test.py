def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user_info_name, user_info_age, user_info_address = name, age, address
    user_info['name'] = user_info_name
    user_info['age'] = user_info_age
    user_info['address'] = user_info_address
    people_list.append(user_info)
    return people_list


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

people = list(zip(name,age,address))
user_info = {}
people_list =[]

# for person in people:
#     name, age, address = person
#     create_user(name, age, address)

# print(people_list)

print(people)
print(*people)
