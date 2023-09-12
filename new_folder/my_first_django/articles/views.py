from django.shortcuts import render

# Create your views here.
def hello(request):
    # 사용자의 요정을 처리하는 로직
    print('hello')
    # 사용자에게 응답으로 나가는 부분
    return render(request, 'articles/hello.html')


def ssafy(request):
    return render(request, 'articles/ssafy.html')


def get_money(request):
    # DB에서 값을 가져오거나 사용자의 입력을 받아서 채울 수 있음
    name = 'ssafy'
    account = '012-34567-89012'
    money = 40000
    context = {
        'name': name,
        'account': account,
        'money': money
    }
    return render(request, 'articles/bank.html', context)
    # context는 html에서 사용할 값을 전달해주는 부분
    # 반드시 데이터 타입은 딕셔너리여야 한다.

import random
def lotto(request):
    number = random.sample(range(46), 6)
    context = {
        'number': number
    }
    return render(request, 'articles/lotto.html', context)