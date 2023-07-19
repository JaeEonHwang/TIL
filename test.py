def create_user(person):
    name, age, address = person
    user_info = {}
    print(f'{name}님 환영합니다!')
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    people_list.append(user_info)
    return people_list

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

people = list(zip(name,age,address))

people_list =[]

# for person in people:
#     name, age, address = person
#     create_user(name, age, address)

# print(people_list)

# print(*people[0])
# print(people)

#print(list(map(create_user,people[i])))

list(map(create_user,people))

print(people_list)
