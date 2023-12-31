# 더꾸

 > 본 프로젝트는 멋쟁이사자처럼 대학 10주년 해커톤에서 은상(강남언니상)을 수상했습니다 🥈

## Description
💿 토큰형 앨범 및 온라인 앨범 구매, 보관 플랫폼

필요 없는 CD를 빼고 사용자가 필요로 하는 것들만을 담은 새로운 앨범 **토큰형 앨범**과 나만의 덕질존, **온라인 앨범 구매/보관 플랫폼**을 통해 새로운 덕질 문화를 제안합니다.

![image1](https://blog-rxb8k.vercel.app/static/images/hackathon/1.png)
![image2](https://blog-rxb8k.vercel.app/static/images/hackathon/2.png)
![image3](https://blog-rxb8k.vercel.app/static/images/hackathon/3.png)

## Usage
+ 서버 실행

```
python manage.py runserver
```

+ 아티스트, 앨범, 수록곡, 포토카드 데이터 생성 및 입력 자동화
1. `data/insert.py` 내부 함수를 실행하여 필요한 데이터를 json 파일로 생성

```
git checkout add-data
cd data
python insert.py makeJsonData_Artist makeJsonData_Music makeJsonData_Album makeJsonData_Photocard
```

2. loaddata를 통해 json 파일로 저장된 데이터를 데이터베이스에 저장
```
python manage.py loaddata artist-data.json album-data.json music-data.json photocard-data.json
```

## Review
[해커톤 회고 포스트 보러가기 - 1000명 앞에서 내 아이디어가 발표되던 순간을 기억하며](https://blog-rxb8k.vercel.app/blog/project/likelion-10th-hackaton-review)
