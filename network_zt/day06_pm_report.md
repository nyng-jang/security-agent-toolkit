# Day 6 Docker ① · nginx 서버 · 오후 (이름 · 2026-10-19)

> **쓰는 법**
> - 문제를 하나 풀 때마다 그 문제 제목 아래를 채웁니다.
> - 질문마다 `쓸 내용:` 에 **무엇을 쓰면 되는지** 적혀 있습니다. 그 내용대로 `답:` 뒤에 씁니다.
> - 「왜 그럴까요?」 같은 질문은 한 단어로 끝내지 말고, 내 화면에서 본 값이나 배운 내용을 근거로 이유까지 씁니다.
> - 🔍 는 그 교시에 꼭 알아야 할 핵심 질문입니다. 답을 못 찾았으면 「모름 — 막힌 곳: …」 이라고 씁니다.

---

## 5교시 · 왜 도커인가 · 이미지와 컨테이너 · 같이 설치하기

### 문제 5-1 · 설치를 확인하고 첫 컨테이너 실행하기

- (가) `docker --version` 으로 나온 값을 적어 주세요.
  - 쓸 내용: 「Docker version … build …」 한 줄
  - 답: Docker version 29.8.2, build 7fc2dff

- (나) 🔍 `docker run hello-world` 출력이 말하는 일의 순서를 5.5 그림의 번호(① ~ ④)에 맞춰 설명해 주세요.
  - 쓸 내용: ① ~ ④ 번호마다 한 일 (클라이언트 · 엔진 · Docker Hub · 컨테이너)
  - 답:

  1. The Docker client contacted the Docker daemon.
  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
      (amd64)
  3. The Docker daemon created a new container from that image which runs the
      executable that produces the output you are currently reading.
  4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

- (다) 🔍 `docker images` 에 보인 것과 `docker ps -a` 에 보인 것은 각각 이미지와 컨테이너 중 무엇이고, 어떻게 다른가요?
  - 쓸 내용: ① images 에 보인 것과 그 종류 ② ps -a 에 보인 것과 그 종류 ③ 둘의 차이
  - 답:
  `docker images`: IMAGE, ID, DISK USAGE, CONTENT SIZE, EXTRA

  `docker ps -a` : CONTAINER ID, IMAGE, COMMAND, CREATED, STATUS, PORTS, NAMES

  - 둘의 차이: docker images 는 내 PC에 받아둔 이미지 목록을 보여주고, docker ps -a는 꺼져있는 컨테이너까지 포함한 모든 컨테이너 목록을 보여주는 명령어다.

- (라) 🔍 `docker images` 출력을 붙여 넣고, `hello-world` 줄의 `IMAGE` · `ID` · `EXTRA` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `IMAGE` · `ID` · `EXTRA` 의 값과 뜻
  - 답:

```
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   11a3eb1597e8       25.9kB         9.49kB    U   
```
② `IMAGE` · `ID` · `EXTRA` 의 값과 뜻
  - IMAGE: 이미지 이름과 태그(이름:태그). 태그 없ㅇ ㅣ 받으면 `latest`가 붙음.
  - ID: 이미지마다 붙는 고유 번호. 번호가 같으면 같은 이미지임.
  - EXTRA의 U: 이 이미지로 만든 컨테이너가 있다는 표시(꺼진 컨테이너도 포함) 

- (마) 🔍 `docker ps -a` 출력을 붙여 넣고, `hello-world` 줄의 `STATUS` · `PORTS` · `NAMES` · `IMAGE` 값과 각각의 뜻을 적어 주세요.
  - 쓸 내용: ① 출력 ② `STATUS` · `PORTS` · `NAMES` · `IMAGE` 의 값과 뜻
  - 답:

① 출력
```
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
6681c89958ef   hello-world   "/hello"   19 seconds ago   Exited (0) 18 seconds ago             goofy_lichterman
```
② `STATUS` · `PORTS` · `NAMES` · `IMAGE` 의 값과 뜻
  - STATUS: 컨테이너의 상태. 
    - `Up ...`: 켜져있음
    - `Exited (0)`: 정상으로 끝남
    - `Exited (0이 아닌 숫자)`: 오류로 끝남
    - `Created`: 만들어졌지만 시작하지 못함
  - PORTS: 내 PC와 연결된 포트. 비어있으면 밖에서 이 컨테이너로 접속할 길이 없다.
  - NAMES: 컨테이너 이름. logs, exec, stop, rm 뒤에 이 이름을 친다.
  - IMAGE: 어떤 이미지와 태그로 만든 컨테이너인지

### 문제 5-2 · Docker Hub 에서 이미지 이름 읽고 없는 이미지 받아 보기

- (가) `nginx:1.28` 에서 `nginx` 와 `1.28` 이 각각 무엇을 정하는지 적어 주세요.
  - 쓸 내용: ① nginx 가 정하는 것 ② 1.28 이 정하는 것
  - 답:
  ① nginx 가 정하는 것 : 다운로드할 소프트웨어(이미지)의 이름(Repository)
  
  ② 1.28 이 정하는 것 : 해당 이미지의 버전 또는 태그(Tag)

- (나) 🔍 `docker pull nginxx` 를 쳤을 때 나온 오류 문구와 그 뜻을 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② 뜻 ③ 고치는 방법
  - 답:

  Using default tag: latest

  Error response from daemon: pull access denied for nginxx, repository does not exist or may require 'docker login'

  - 뜻: Docker Hub에 nginxX라는 이름의 저장소(Repository)가 존재하지 않거나, 권한이 없어 접근할 수 없음을 의미합니다.
  - 고치는 방법: 오타를 수정하여 올바른 이미지 이름(nginx)으로 명령어를 다시 입력합니다.

- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(도커를 쓰면 무엇이 같아지는지)
  - 답: 웹 서버 이미지를 받을 때는 오타 없이 정확한 이름과 버전을 입력해야 원격 저장소에서 올바른 이미지를 안전하게 가져올 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: Docker 이미지는 이름:태그 형식으로 버전까지 정확하게 지정해야 하며, 이름을 잘못 입력하면 레포지토리를 찾을 수 없어 오류가 발생한다는 것을 알게 되었습니다.

## 6교시 · nginx 서버 켜고 접속 기록 읽기

### 문제 6-1 · 포트 없이 켜 보고, 포트를 연결해 접속하고, 기록 읽기

- (가) 포트 없이 켠 `web` 에 접속했을 때 어떻게 되었는지 적어 주세요.
  - 쓸 내용: 접속했을 때 나온 화면이나 오류와 `docker ps` 의 PORTS 열
  - 답: Error response from daemon: No such container: web

- (나) 🔍 `-p 8080:80` 이 하는 일을 내 PC의 포트와 컨테이너의 포트로 나눠 설명해 주세요.
  - 쓸 내용: ① 내 PC 쪽 포트 ② 컨테이너 쪽 포트 ③ 연결이 하는 일
  - 답: -p 8080:80은 내 PC의 8080번 포트로 들어오는 요청을 컨테이너 내부의 80번 포트로 전달(포트 포워딩)해주는 역할을 합니다. 앞쪽 숫자는 내 PC, 뒤쪽 숫자는 컨테이너의 포트를 의미합니다.

- (다) 🔍 `docker logs web` 출력에서 `GET /` 줄 하나를 붙여 넣고, 접속자 주소 · 시각 · 요청 · 응답 번호를 찾아 적어 주세요.
  - 쓸 내용: ① `GET /` 줄 ② 접속자 주소 · 시각 · 요청 · 응답 번호 네 가지
  - 답:  
  ```
  172.17.0.1 - - [19/Oct/2026:06:11:45 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36" "-"
  ```
  접속자 주소: 172.17.0.1

  시각: 19/Oct/2026:14:31:05

  요청: GET / (루트 경로 요청)

  응답 번호: 200 (성공)

### 문제 6-2 · 컨테이너 안을 들여다보고, 끄고, 지우기

- (가) 컨테이너 안에서 `ls /usr/share/nginx/html` 로 본 파일 이름을 모두 적고, 그중 브라우저의 첫 화면이 어느 파일인지 적어 주세요.
  - 쓸 내용: ① 파일 이름 모두 ② 첫 화면 파일
  - 답: 50x.html  index.html, index.html이 첫 화면. 
- (나) 🔍 `docker stop web` 뒤에 `docker ps` 와 `docker ps -a` 에 각각 `web` 이 보이나요? 차이를 설명해 주세요.
  - 쓸 내용: ① stop 뒤 ps 에 보이는지 ② ps -a 에 보이는지 ③ 차이의 이유
  - 답: ps에는 안보이는데 ps -a에는 보임. ps -a는 꺼진 컨테이너까지 보여주기 때문에
- (다) 🔍 같은 이름으로 다시 `run` 했을 때 나온 오류 문구와, `docker rm` 이 필요한 이유를 적어 주세요.
  - 쓸 내용: ① 오류 문구 ② rm 이 필요한 이유
  - 답: 오류문구 docker: Error response from daemon: Conflict. The container name "/web" is already in use by container "a2b3ac4d26f10621d8239b83753665f8aa7bbf435c27a1b64cf5821730bb4b8e". You have to remove (or rename) that container to be able to reuse that name.

  - rm이 필요한 이유: 꺼진 컨테이너 이름을 지워줌.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(켜는 명령 · 기록 보는 명령 · 정리 방법)
  - 답: Nginx 웹 서버는 docker run -d로 구동하고, docker logs로 접속 기록을 확인하며, 사용이 끝난 컨테이너는 stop과 rm으로 정리해야 충돌을 방지할 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: docker의 컨테이너 상태, 그리고 포트를 연결해 접속하고 기록을 읽는 명령을 배웠다. 

## 7교시 · 내 페이지 연결 · 두 서버 · 올리기

### 문제 7-1 · 컨테이너 안의 변경이 사라지는 것을 보고, 내 폴더를 연결하기

- (가) 컨테이너 안에서 바꾼 뒤 `docker rm -f web` 으로 지우고 다시 켰을 때 화면이 어떻게 되었는지 적어 주세요.
  - 쓸 내용: ① 바꾼 뒤 화면 ② 지우고 다시 켠 뒤 화면
  - 답: 컨테이너 내부에서 수정했을 때는 화면에 inside가 나타났으나, docker rm -f web으로 지우고 다시 켰을 때는 수정 내용이 사라지고 원래의 Welcome to nginx! 화면으로 돌아갔습니다.
- (나) 🔍 컨테이너 안에서 바꾼 내용이 사라진 이유와, `-v` 로 폴더를 연결하면 무엇이 달라지는지 적어 주세요.
  - 쓸 내용: ① 사라진 이유 ② -v 로 연결하면 달라지는 점
  - 답: 컨테이너 내부의 파일 변경 사항은 해당 컨테이너 내부에만 임시로 저장되므로, 컨테이너를 삭제하면 함께 사라집니다. -v 옵션을 사용해 내 PC의 폴더를 연결하면 파일은 안전하게 내 PC에 보존되고 컨테이너는 이를 참조하게 됩니다.
- (다) 🔍 `MSYS_NO_PATHCONV=1` 없이 `-v` 를 실행했을 때 화면에 무엇이 나왔고 왜 그랬는지 적어 주세요.
  - 쓸 내용: ① 화면에 나온 것 ② 그렇게 된 이유
  - 답: MSYS_NO_PATHCONV=1 없이 실행하면 오류는 발생하지 않지만 내 파일 대신 기본 Welcome to nginx! 화면이 나옵니다. Git Bash 환경에서 -v 뒤의 경로를 윈도우 경로 형식으로 자동 변환해 버려 올바른 폴더가 연결되지 않기 때문입니다.

### 문제 7-2 · 서버 두 대를 띄워 포트로 구분하고, 파일을 고쳐 바로 반영되는지 보기

- (가) 두 주소(`8080` · `8081`)에서 보이는 화면을 각각 적어 주세요.
  - 쓸 내용: 두 주소의 화면 문구
  - 답:

```
CONTAINER ID   IMAGE        COMMAND                   CREATED              STATUS              PORTS                                     NAMES
680dd3a61a47   nginx:1.28   "/docker-entrypoint.…"   7 seconds ago        Up 6 seconds        0.0.0.0:8081->80/tcp, [::]:8081->80/tcp   web-two
da99c073f91d   nginx:1.28   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   web-one
```
- (나) 🔍 `docker ps` 의 PORTS 열에서 두 서버를 구분해 주는 것은 무엇인가요?
  - 쓸 내용: PORTS 열에서 서버를 구분하는 값
  - 답: PORTS 열에 표시되는 내 PC 쪽 포트 번호(8080과 8081)가 두 서버를 구분해 줍니다.
- (다) 🔍 `:ro` 는 무슨 뜻이고, 왜 읽기 전용으로 연결하나요?
  - 쓸 내용: ① :ro 의 뜻 ② 읽기 전용으로 연결하는 이유
  - 답: :ro는 read-only(읽기 전용)를 의미합니다. 컨테이너가 호스트의 원본 파일을 임의로 수정하거나 손상시키지 못하도록 최소한의 읽기 권한만 부여하기 위해 사용합니다.
- (한 줄) 보안 담당에게 보낼 답을 한 문장으로 적어 주세요.
  - 쓸 내용: 보안 담당이 바로 읽을 수 있는 한 문장(두 서버를 어떻게 띄웠는지)
  - 답: 호스트 폴더를 읽기 전용으로 연결(-v ...:ro)하고 포트를 다르게 지정하여, 하나의 이미지로 서로 다른 두 개의 웹 서버를 독립적으로 구동할 수 있습니다.
- 이 교시에서 새로 알게 된 것 하나를 적어 주세요.
  - 쓸 내용: 자유롭게
  - 답: 볼륨 마운트(-v)를 활용해 컨테이너 외부의 파일을 안전하게 서빙하고 포트로 다중 서버를 관리하는 방법을 배웠습니다.

### 문제 7-3 · 오늘 만든 것을 깃허브에 올리기

- (가) `git status` 를 쳤을 때 빨간 목록에 줄이 몇 개였는지, 그 가운데 `.env` · `.venv` 가 있었는지 적어 주세요.
  - 쓸 내용: ① 줄 수 ② .env · .venv 가 있었는지
  - 답: 9줄
