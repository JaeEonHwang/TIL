


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

people_list =[]
number_of_book = 100

def increase_user():
    pass

def create_user(person):
    name, age, address = person
    user_info = {}
    print(f'{name}님 환영합니다!')
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    people_list.append(user_info)

def rental_book(info):
    name = info['name']
    age = info['age']
    number = age // 10
    print('남은 책의 수 :', decrease_book(number))
    print(f'{name}님이 {number}권의 책을 대여하셨습니다.')

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book

people = list(zip(name,age,address))

list(map(create_user,people))
many_user = people_list

list(map(rental_book,new_dict))

