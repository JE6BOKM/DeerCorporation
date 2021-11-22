# 디어코퍼레이션

- 과제 출제 기업 정보
  - 기업명 : 디어코퍼레이션
  - [디어코퍼레이션](https://web.deering.co/)
  - [wanted 채용공고 링크](https://www.wanted.co.kr/wd/59051)

## 💁‍♀️ Members

| 이름   | github                                    | 담당 기능                 |
| ------ | ----------------------------------------- | ------------------------- |
| 신재민 | [shinjam](https://github.com/shinjam)     | 지역정보 및 지도 API 연동 |
| 신우주 | [shinwooju](https://github.com/shinwooju) | 모델링                    |
| 최혜림 | [rimi0108](https://github.com/rimi0108)   | 배포                      |
| 강성묵 | [miranaky](https://github.com/miranaky)   | 요금 계산                 |
| 김민규 | [SkyStar-K](https://github.com/SkyStar-K) | 모델링                    |

## ⭐ 과제 내용

### [필수 포함 사항]

- READ.ME 작성
  - 프로젝트 빌드, 자세한 실행 방법 명시
  - 구현 방법과 이유에 대한 간략한 설명
  - 완료된 시스템이 배포된 서버의 주소
  - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### [과제 안내]

디어는 사용자의 요금을 계산하기 위해 다양한 상황을 고려합니다.

- 우선 지역별로 다양한 요금제를 적용하고 있습니다. 예를 들어 건대에서 이용하는 유저는 기본요금 790원에 분당요금 150원, 여수에서 이용하는 유저는 기본요금 300원에 분당요금 70원으로 적용됩니다.
- 할인 조건도 있습니다. 사용자가 파킹존에서 반납하는 경우 요금의 30%를 할인해주며, 사용자가 마지막 이용으로부터 30분 이내에 다시 이용하면 기본요금을 면제해줍니다.
- 벌금 조건도 있습니다. 사용자가 지역 바깥에 반납한 경우 얼마나 멀리 떨어져있는지 거리에 비례하는 벌금을 부과하며, 반납 금지로 지정된 구역에 반납하면 6,000원의 벌금을 요금에 추과로 부과합니다.
- 예외도 있는데, 킥보드가 고장나서 정상적인 이용을 못하는 경우의 유저들을 배려하여 1분 이내의 이용에는 요금을 청구하지 않고 있습니다.

최근에 다양한 할인과 벌금을 사용하여 지자체와 협력하는 경우가 점점 많아지고 있어 요금제에 새로운 할인/벌금 조건을 추가하는 일을 쉽게 만드려고 합니다. 어떻게 하면 앞으로 발생할 수 있는 다양한 할인과 벌금 조건을 기존의 요금제에 쉽게 추가할 수 있는 소프트웨어를 만들 수 있을까요?

우선은 사용자의 이용에 관한 정보를 알려주면 현재의 요금 정책에 따라 요금을 계산해주는 API를 만들어주세요. 그 다음은, 기능을 유지한 채로 새로운 할인이나 벌금 조건이 쉽게 추가될 수 있게 코드를 개선하여 최종 코드를 만들어주세요.

## 사용 기술 및 tools

> - Back-End : <img src="https://img.shields.io/badge/Python 3.8-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Django 3.2-092E20?style=for-the-badge&logo=Django&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/postgresql 13.1-0064a5?style=for-the-badge&logo=Postgresql&logoColor=white"/>
> - Deploy : <img src="https://img.shields.io/badge/AWS_EC2-232F3E?style=for-the-badge&logo=Amazon&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>
> - ETC : <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white"/>

## 🏄‍♀️ 모델링

![5 drawio](https://user-images.githubusercontent.com/5153352/142803130-6cdddbe3-7195-4812-b93b-3dce55ac21d0.png)

## API

[링크-postman document](https://lively-eclipse-444504.postman.co/documentation/13670333-63aa4993-d56c-4ea1-ab6e-f91b1[…]ish?workspaceId=914aa13c-f4c2-4899-8d0e-cda711806b1b)

## 구현 기능

### 로그인 기능

- 사용자 인증을 통해 Deer 이용 기록을 저장/확인 합니다.

  - 구현
    - JWT 인증 방식을 이용합니다.
    - 유저 회원가입/로그인 을 통해 JWT Token을 받습니다.

### 지역 정보 연동 (Naver 지도 API)

- 행정 구역 구분 데이터와 네이버 지도 api를 이용하여 DB에 지역 정보를 저장합니다.
  - 행정 구역 별 위치 정보를 Naver 지도 API에서 받아와서 DB에 저장합니다.

### Ride History

- 로그인된 사용자는 사용 후 사용 기록을 보냅니다.
  - 사용 시작 시간, 사용 종료 시간, 종료 지점의 위도,경도, 사용한 Deer Id
- 사용 기록을 분석하여 요금을 측정합니다.
  - 다음 내용에 따라 계산합니다.
  - 지역별 요금으로 기본 요금과 분당 부과되는 요금 계산
  - 30분 이내 사용시 기본요금 면제
  - 1분 이내 사용시 요금 과금 없음
  - 지역을 벗어난 경우 추가 요금 과금
  - 주차장에서 종료한 경우 주차지역별 할인
  - 주차 금지 구역에서 종료한 경우 벌금 과금

## 설치 및 실행 방법

### Local 개발 및 테스트용

```bash
$ git clone https://github.com/JE6BOKM/DeerCorporation.git && cd DeerCorporation

# .envs/.local.naver 에 NAVER_CLIENT_ID와 NAVER_CLIENT_SECRET 설정
$ touch .envs/.local.naver

# docker build and run
$ docker-compose -f docker/compose/local.yml up --build

# super user 생성
$docker-compose -f docker/compose/local_m1.yml run --rm django ./manage.py createsuperuser
```

# Reference

이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 디어코퍼레이션에서 출제한 과제를 기반으로 만들었습니다.
