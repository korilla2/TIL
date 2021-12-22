# 깃허브

- 커밋만 할 경우 로컬 저장소로 이동
- 푸쉬를 날려주면 깃허브라는 원격저장소에 보관된다

## git ignore

- 원격저장소에 올리면 안되는 경우
- 원격저장소에 올릴 필요가 없는 경우
- 해당 파일을 추적하지 말라는 의미로 작성

### 사용법

1. `.gitignore` 파일 생성
2. 해당 파일 내에 올리고 싶지 않은 `파일명.확장자` 써주고 저장
3. [gitignore.io ](https://www.toptal.com/developers/gitignore) 해당 홈페이지에서 ignore 파일 생성을 도와줌

## 깃허브 시작하기

1. 회원가입
2. 오른쪽 위에 New repository 를 통해 새로운 저장소 생성
3. 저장소 이름만 설정하고 나머진 바꾸지 않는다
4. `git remote add origin + 주소`
5. 잘 연동이 되었다면 푸쉬를 날려주자
6. 파일이 원격저장소로 잘 이동했는지 깃허브 홈페이지에서 확인

## 깃허브 활용하기

- `git clone + 주소` 데이터를 내려받자
- 원본 - 깃허브 - 복사 서로 연동이 되었다
- 이제 push pull 을 이용해서 서로 동기화가 가능하다
- 작성한뒤 push로 깃허브로 보내고
- 받을곳에서 pull 을 이용해 적용시킨다
  - `git push origin master` `git pull origin master`

## 주의사항 오류

1. 이름이 다른 파일이 있는 경우
   - 오토병합이 일어난다
   - pull -> push -> pull(other)

2. 같은 파일인데 내용이 다른 경우
   - 오토 병합이 일어나지 않고 충돌이 일어난다
   - 이럴땐 수동으로 수정을 해줘야 한다

## 분기 branch

- `git branch + 이름` 브랜치 생성
- `git branch` 브랜치 목록 확인
- `git branch -d + 이름` 브랜치 삭제
- `git switch + 이름` 이름으로 해당되는 브랜치로 이동
  - head 가 가리키는 곳이 master에서 이름으로 이동

- branch 는 평행세계라 생각하자
- commit 하는 시점부터 분기마다 독립적으로 작동

### branch 활용 이유

- 커밋을 안 할수는 없음
- 기존 소프트웨어 위에 작업하기엔 위험부담이 큼
- 그렇기에 분기를 만들어 따로 작업을 한 뒤
- 완성되면 원본과 합쳐 최종본을 만듦

## 병합 merge

- 분기를 사용한 이유는 결국 master 와 안전하게 합치기 위함
  1. `git switch master` 마스터로 이동
  2. `git merge + 분기 이름 ` 
  3. master 와 해당 branch 가 안전하게 합쳐짐

## 협업

1. remote 에서 저장소 먼저 생성
2. collaborator 추가
3. 팀원들 각자 clone
4. `$ git switch -c <my-branch>` 로 각자 브랜치 생성
5. 작업 => add => commit > 반복
6. `$ git push origin <my-branch>`  master 가 아니라는 점 조심
7. 리모트에서 pull request 생성
8. 상의 후 merge 결정
   1. 초록색 => 오토 머지 가능
   2. 빨간색 => 깃허브에서 수동으로 수정 후 진행

9. 로컬 master 브랜치에서 `$ git pull origin master`
10. 반복
