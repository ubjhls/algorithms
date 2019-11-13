# project 01 - 파이썬을 활용한 데이터 수집

## 1)  boxoffice

- 먼저 영화진흥위원회 오픈 api를 통해 데이터 수집

- 기본 url : `http://www.kobis.or.kr...st.json?key={key}&targetDt={targetDt}&weekGb={weekGb}`에 key 값, target 날짜, weekGb = '0' 을 통해 .json 으로 데이터를 받아온다.

- 요청 변수 : key , targetDt, weekGb

- 시간을 나타내는 모듈을 이용해 50주 전부터 차례로 불러와 중복값 제거

- ```python
  import datetime
  now = datetime.datetime(2019,7,13)
  targetDt = (now-datetime.timedelta(weeks=50-i)).strftime('%Y%m%d')
  ```

- csv 로 저장

- ```python
  import csv
  with open('boxoffice.csv', 'w', encoding='utf-8') as f:
      fieldnames = ['영화이름', '영화코드','누적관객수']
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()
      for item in dic.values():
          csv_writer.writerow(item)
  ```

- 

### 2) movie

- boxoffice 와 마찬가지로 url을 받아온다.

- 요청 변수 :  key , movieCd

- boxoffice 에서 수집한 대표코드를 이용해 정보들을 불러온다.

- ```python
  f = open('boxoffice.csv', 'r', encoding='utf-8'
  ```

- 중복되는 리스트들을 하나의 범주로 묶어서 간략화

- ```python
  movieInfo = response['movieInfoResult']['movieInfo']
  ```



### 3) director

- 요청변수 : key ,peopleCd

- movie 에서 수집한 감독정보를 이용해 정보를 불러온다

- ```python
  f = open('movie.csv', 'r', encoding='utf-8')	
  ```

- 감독 정보가 없거나 동명이인을 처리하기 위해 조건문을 사용