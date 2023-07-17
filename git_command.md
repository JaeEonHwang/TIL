## commit 순서
1. git add 'file' or .
2. git commmit -m 'message'
3. git remote add (원격 저장소 이름) (원격 저장소 url)
4. git push (원격 저장소 이름) (브랜치 이름)<br>
(현재는 git push origin master)
<br>

## git command

* git push add origin 'remote url'<br>
: 로컬 저장소에 원격 저장소 추가
<br>(git아, push해줘, origin 이라는 이름의 원격 저장소에 master branch를)
* git pull origin master
<br>: 원격 저장소의 변경사항만을 받아옴 (업데이트)
* git clone 'remote url'<br>
: 원격 저장소 전체를 복제 (다운로드)
* git move (현재파일) (바꿀 이름) <br>
: 파일 이름 바꾸기
* touch (파일이름) <br>
: 파일 생성
* rm (파일이름)
: 파일 삭제

## git push 팁
* git push **-u** (원격저장소) (브랜치)를 한 번 해두면 이후에 'git push'만 해도 같은 장소에 저장이 된다

## .gitingore 사용법
`#` : 주석 <br>
    # 이 줄은 적용되지 않는다.

`*` : 와일드 카드<br>
    *.txt : txt파일은 모두 무시

! : 무시를 무시<br>
    !go.txt : *.txt로 txt 파일은 무시하기로 했지만, 이 규칙을 무시하고 go.txt는 staged에 올린다.

/ : path 표시<br>
    /module : 루트 디렉터리 아래 /module 파일을 무시. 그러나, user/module은 무시되지 않는다.<br>
    js/ : js 디렉토리 아래 모든 파일 무시<br>
    

ex) css/*.txt : css 디렉토리 아래 확장자가 txt를 모두 무시 