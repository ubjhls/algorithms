import csv
import requests
import pprint
result =[]
f = open('boxoffice.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
count = 1
for line in rdr:
    if count > 1 and count % 2 == 1:
        result.append(line[1])
    count=count+1
f.close() 


dic={}
for movieCd in result:
    key = 'f3f6bccf37b5643f47db688990cacfbf'
    api_url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
    response = requests.get(api_url).json()
    movieInfo = response['movieInfoResult']['movieInfo']
    dic[response.get('movieInfoResult').get('movieInfo').get('movieCd')] ={
     "영화대표코드" : movieInfo.get('movieCd'),
     "영화명(국문)" : movieInfo.get('movieNm'),
     "영화명(영문)" : movieInfo.get('movieNmEn'),
     "영화명(원문)" : movieInfo.get('movieNmOg'),
     "영화명(관람등급)" : movieInfo.get('audits')[0].get('watchGradeNm') if movieInfo.get('audits') else None,
     "영화명(개봉연도)" : movieInfo.get('openDt'),
     "상영시간" : movieInfo.get('showTm'),
     "장르명" : movieInfo.get('genres')[0].get('genreNm') if movieInfo.get('genres') else None,
     "감독명" : movieInfo.get('directors')[0].get('peopleNm') if movieInfo.get('directors') else None 
    }
print(dic)

import csv
with open('movie.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화대표코드', '영화명(국문)','영화명(영문)','영화명(원문)','영화명(관람등급)','영화명(개봉연도)','상영시간','장르명','감독명']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in dic.values():
        csv_writer.writerow(item)