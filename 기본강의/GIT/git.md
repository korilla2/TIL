# 깃(GIT)

- 파일 하나하나가 아닌 폴더를 통째로 관리하는 tool

- 폴더를 저장소(리포)로 보냄

## 명령어

- `git init`
  - 해당폴더부터 하위폴더까지 관리대상에 편입시작
  - 상위폴더엔 영향없음
  - 제대로 되었다면 `git bash` 터미널에서 `(master)` 라고 보여짐
- `rm -r .git`
  - 숨김파일로  .git 폴더가 생긴 상태
  - 해제하고 싶은 경우 이 폴더를 지워주면 됨
- `git status`
  - 현재 상태를 파악
  - 매우 자주 사용 될 명령어
- `git add + 파일명.확장자`
  - 스테이지에 파일을 올림
  - `git add .` 현재위치의 모든파일 add
- `git log`
  - 로그확인
- `git log --oneline`
  - 로그를 간단하게 보여줌
- `git restore --staged + 파일명.확장자`
  - 스테이지에서 내림
- `git restore + 파일명.확장자`
  - 이전 파일의 내용으로 변경
- `git commit -m 'first commit'`
  - 파일을 저장소에 보냄
- `git config --global user.email + '이름'`
- `git config --global user.name + '이메일'`
  - 유저 및 이메일 등록
- `cat ~/.gitconfig`
  - 유저네임, 이메일 확인
- `git push -u origin master` 
  - 깃허브(원격)로 보냄
- `git remote add origin + 깃허브에서 준 주소`
  - 원격연결

## 초기세팅

1. `git init`
2. `git config --global user.email + '이름'`
3. `git config --global user.name + '이메일'`
4. `cat ~/.gitconfig`
5. 깃허브에서 리포생성
6. `git remote add origin + 깃허브에서 준 주소`



## 사용순서

1. `git add .`
2. `git commit -m '메시지'`
3. `git push -u origin master`