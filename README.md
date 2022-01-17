# **Getting better day by day**

#### 2022 목표

1. 빅데이터 과정 출석률 100% 수강완료
2. 8시 기상
3. 클라이밍 V6 달성
4. 일주일에 한 번 이상 새벽기도
5. 하루 1시간 이상 공부

---

## 목차

1. [Git ?](#git)
2. [Typora](#typora)
3. [Git Github 연결(User)](#git-github-연결(user))
4. [File Tree](#file-tree)
5. [***gitignore***](#gitignore)
6. [clone push pull](#clone-push-pull)
7. [branch](#branch)
8. [restore](#restore)
9. [reset](#reset)
10. [Profile](#profile)  
11. [Python](#python)

# Git ?

- 분산 **버전 관리** 시스템

  - 버전 관리 : 코드의 **히스토리(버전)**을 관리하는 도구

  - 개발되어온 **과정** 파악 가능

  - 이전 버전과의 **변경 사항 비교 및 분석**

    

- CLI(Command Line Interface) 

  -  터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식
  -  GUI(Graphic User Interface)에 비해 간단, 많은 세부적인 기능

- Git Bash의 사용 이유

  1. 명령어의 통일
  2. UNIX 계열 운영체제

- 터미널 명령어

  `touch` 
  
  - <u>파일 생성 명령어</u> (=`vi 파일명`)
  - 띄어쓰기로 구분하여 **여러 파일**을 한꺼번에 생성 가능
  - 숨김 파일을 만들기 위해서는 `.`을 파일 명 앞에 붙인다
  
  ```python
  
  $ touch text.txt
  
  ```
  
  `mkdir 파일명` :폴더 생성 명령어
  
  - make directory
  - <u>새 폴더를 생성하는 명령어</u>
  - 띄어쓰기 구분으로 **여러 폴더** 생성 가능
  - 폴더 이름 사이에 공백을 넣으러면 따옴표로 묶음
  
  ```python
  
  $ mkdir folder
  $ mkdir 'happy hacking'
  
  ```
  
  `ls` 
  
  - list segments
  
  - 디렉토리의 폴더/파일 목록을 보여줌
  
     - `-a` : all 옵션, 숨김 파일까지 모두 보여줌
     - `-1` : long 옵션. 용량, 수정 날짜 등 파일 정보를 자세히 보여준다
  
  ```python
  
  # 기본사용
  $ ls
  
  # all 옵션
  # ls -a
  
  # all, long 옵션 함께 적용
  $ ls -a -1
  
  # 여러 옵션 축약 가능
  $ ls -al
  
  ```
  
  `mv` 
  
  - move
  - <u>폴더/파일을 다른 폴더 내로 이동하거나 이름 변경하는 명령어</u>
  - 단, 다른 폴더로 이동할 때는 작성한 폴더가 반드시 있어야 한다. 없으면 이름 바뀜
  
  ```python
  
  # text.txt를 folder 폴더 안에 넣을 때
  $ mv text.txt folder
  
  # text1.txt의 이름을 text2.txt로 바꿀 때
  $ mv text1.txt text2.txt
  
  ```
  
  `cd`
  
  - change directory
  - 현재 작업 중인 디렉토리 변경하는 명령어
  - `cd ~` 를 입력하면 홈 디렉토리로 이동
  - `cd ..` 를 입력하면 부모 디렉토리로 이동함 (위로 가기)
  - `cd -` 를 입력하면 전 디렉토리로 이동 (뒤로 가기)
  
  ```python
  
  # 현재 작업 중인 디렉토리에 있는 folder폴더로 이동
  $ cd folder
  
  # 절대 경로를 통한 디렉토리 변경
  $ cd C:/Users/kyle/Desktop
  
  # 상대 경로를 통한 디렉토리 변경
  $ cd ../parent/child
  
  ```
  
  `rm`
  
  - remove
  - 폴더/파일 지우는 명령어
  - GUI와 달리 휴지통으로 이동하지 않고, 바로 `완전 삭제` 한다.
  - `*(asterisk, wildcard)` 를 이용해서 `rm *.txt` 라고 입력하면 txt 파일 전체를 다 지웁니다.
  - `-r` recursive 옵션. 폴더를 지울 때 사용합니다.
  
  ```python
  
  $ rm test.txt
  $ rm -r folder
  
  ```
  
  `start, open`
  
  - 폴더/파일을 여는 명령어
  - `windows` 에서는 start를, `Mac` 에서는 open을 사용할 수 있다.
  
  ```python
  
  # Windows
  $ start test.txt
  
  # Mac
  $ open test.txt
  
  ```
  
  `vi`
  
  - 기존에 파일이 있다면 수정
  - 파일이 없고, 새롭게 생성하면서 수정
  
  ```python
  $ vi a.txt
  
  `i` : 글쓰기 (insert)
  `esc` + `:` + `wq` : 저장
  ```

- Git Github 연결

  -  User 연결 : 한번만 해도 되는 작업

  ````python
  
  $ git config --global user.name "Your Name"
  $ git config -- global user.email your@email.com
  
  ````

  - epository 연결할 때, 한번만 해도 되는 작업

  ````python
  
  $ git init : git 시작
  
  $ git remote add origin <git repository url> : repository 연결
  
  $ ctrl + insert
  
  $ shift + insert : 붙여넣기
      
  ````

- 파일 수정, 생성 할 때마다 해야하는 작업!!

  - `git add .` : 모든 파일 staging area에 올리기

  - `git add <file_name>` : 파일 staging area에 올리기

  - `git commit -m 'commit message'` : 커밋 massage 작성

  - `git push origin master` : github로 밀어내기!

  - `git push -u 원격저장소명 브랜치명` : 이 명령어를 입력하면 추후에 git push만 입력하여 push 가능	

- 유용한 단축키
  - `위, 아래 방향키` : 과거에 작성했떤 명령어 조회
  - `tap` : 폴더/파일 이름 자동 완성
  - `ctrl + a` : 커서가 맨 앞으로 이동
  - `ctrl + e` : 커서가 맨 뒤로 이동
  - `ctrl + w` : 커서가 맨 앞 단어를 삭제
  - `ctrl + l` : 터미널 화면을 깨끗하게 청소
  - `ctrl + insert` : 복사
  - `shift + insert` : 불여넣기

# Typora 

### heading

- `#` : h1
- `##` : h2
- `###` : h3
- h6까지 있다.

### list

- 순서가 있는 1
  - `1.` : 순서가 있는 리스트 생성
- 순서가 없는
  - `-`/`*` : 순서가 없는 리스트 생성
- `tap`을 사용해서 들여쓰기 가능!!



### code block

- `" ``` "`
  - 백킷(`)을 세번 입력하면 코드 블럭이 만들어짐
  - 백킷(`)을 한번 입력하면 인라인 코드블럭이 만들어짐

```python

print('Hello D반!')
if my_class="D반":
    print('Yay!!')
else:
    print('cry...')
    
```

 `코드 실행은 되지 않음`



### 링크

- `[string](url)` : 링크 생성	

  ex.[헬로디반!](https://www.notion.so/558586a8e5ae40d48b6012d48c9d3ec4)

  - 잊지말자 full link!



### 이미지링크

- `![string](url)`:이미지링크생성

  ex. ![조정석](data:image/jpeg;base64,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)

  ex.![아이유](README/images.jpeg)



### 텍스트 강조

- `**텍스트**` : **안녕**->볼드체 : `ctrl`+`b`

- `*안녕*`:*안녕* ->이태리체 : `ctrl`+`i``

- ``~~잘가~~`:~~잘가~~ ->취소선 : `ctrl`+`shift`+`enter` 

  ​                                               notin 에서!

- `***한동권***` : ***한동권*** <- 볼트체 + 이태리체 `ctrl`+`b`+`i`



### 수평선

- `-`*3 : 연속으로 3번 입력하면 단락구분을 할 수있다.
- `*`*3
- `_`*3

### 인용문

- `>`

  - > 깃허브특강

- `>>`

  - > > 오지혜강사님 두뇌

### 표

| 1    | 2    | 3    |
| ---- | ---- | ---- |
|      |      |      |

- `|`+` ` : 개수가 간의 개수

# File Tree

c --- users --- student --- desktop --- TIL

![file_tree](README/find-file-tree.svg)

# ***gitignore***



- `git add .` 를 하기전에 gitignore 폴더를 만들어야한다.
- 쉽게 생각하면 `git init`을 하고 `gitignore`를 만든다.
- .gitignore 파일을 생성하고 파일 안에 무시할 파일을 넣어놓으면 그 파일은 무시가 된다!
-  `* + 파일확장자` : * 뒤의 **모든**확장자 무시
- `/` : 폴더 의미
- `https://www.toptal.com/developers/gitignore` : 사이트

# **clone push pull**

**가정** 

- 이미 레포지토리에 커밋이 올라가 있다.
- pull, push 하는 권한이 있다.



**clone**

- 빈 폴더( 상위 폴더에 깃이 없어야함)에 clone을 합니다.
  - `git clone {url}` -> 새로운 폴더에 생성
  - `git clone {url} .` -> 현재 폴더에 생성
- do something and push commit
  - 원격 저장소가 원본 로컬 저장소보다 상위 버전이 됨.
- 원본 로컬 저장소에서 원격 저장소 의 코밋을 pull 함
  -  `git pull`

**conflict 상황**

- 왼쪽 디렉토리에서 a.txt 변경합니다
- 그에 대한 코밋을 남깁니다.
- 원격 저장소에 push 합니다



- 오른쪽 디렉토리에서 a.txt를 다르게 변경합니다
- 그에 대 한 코밋을 남깁니다.
- 원격 저장소에서 pull 해옵니다.

Conflict! 를 해결합니다

- 원격 저장소에 push합니다
- 왼쪽 디렉토리에서 원격 저장소에서 pull 해옵니다.

# branch

- 브랜치만들기
  - git branch {브랜치이름} 

- 브랜치 확인
  - git branch
  
- 브랜치 지우기
  - git branch -d {브랜치이름}
  - git branch -D {브랜치이름}

- 브랜치 이동
  - git switch
  - git check out
  - 만들면서 이동
    - git switch -c 브랜치이름

- 브랜치 merge

  - 기준이 될 브랜치에서!
    - git merge(합칠 브랜치 이름)

  - 두 브랜치 모두에서 수정사항이 있지만, 겹치지 않은 상황
    - 3-way merge

  - 두 브랜치 모두에서 수정사항이 있고, 겹친상황
    - Conflict 해결 후 commit

  - 합쳐질 브랜치에서만 수정사항이 있는 상황

    - Fast-forword 잘 합쳐짐

      

- 깃 로그 확인

  - git log --oneline

  - git log --all --oneline

  - git log --all  --graph



# restore

- **`git restore {파일명}`**
  - 가장 최근 기록(스테이징 에리아 혹은 코밋)으로 돌아온다
- **`git restore {파일명} --staged`**
  - 스테이징  에리아에서 내려준다
- **`git rm {파일명} --cached`**
  -  untracked 상태로 바꿔준다
- **`git commit --amend`**
  -  파일 수정이 없으면 코밋 메세지만 작성해주고
  - 파일 수정이 있으면 그것을 반영하여 코밋을 덮어씌운다
- **`diff`**
  - 워킹디렉토리와 **가장 최근기록**(스테이징 에리아 혹은 코밋)의 차이를 보여준다
- **`diff --staged`**
  - **스테이징에리아와 코밋의 차이**를 보여준다



# reset

1. `git reset --soft <commit 고유번호>` 

   : 코밋만 하면 원 상태로 돌아올 수 있다

2. `git reset --mixed <commit 고유번호>` 

   : add, commit 까지 하면 원 상태로 돌아올 수 있다 

3. `git reset --hard <commit 고유번호>`

   : 정말 모두 리셋

4. `git reflog` : 코밋 리셋 기록을 확인

5. `git revert <commit 고유번호>` 

   : 해당 코밋을 취소하고 코밋을 만듬

   - `git revert  <commit 고유번호>..<고유번호>` 
     - 연속적인 리버트 방법!



# Profile

- https://startbootstrap.com/ 
  - 템플렛 다운로드 사이트
  - 자유롭게 다운받아 사용 가능하다
  - html 코드를 모르더라도, 대입하여 어느정도 수정 가능하다

# Python

- https://wikidocs.net/book/1 
  - 파이썬 서적
