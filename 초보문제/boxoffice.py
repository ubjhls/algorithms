import datetime
import requests
import pprint

now = datetime.datetime(2019,7,13)

dic={}
for i in range(51):
    targetDt = (now-datetime.timedelta(weeks=50-i)).strftime('%Y%m%d')
    key = 'f3f6bccf37b5643f47db688990cacfbf'
    api_url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
    response = requests.get(api_url).json()
    for j in range(len(response.get('boxOfficeResult').get('weeklyBoxOfficeList'))):
        dic.update({response.get('boxOfficeResult').get('weeklyBoxOfficeList')[j].get('movieNm') : {
            "영화이름" : response.get('boxOfficeResult').get('weeklyBoxOfficeList')[j].get('movieNm'),
            "영화코드" : response.get('boxOfficeResult').get('weeklyBoxOfficeList')[j].get('movieCd'),
            "누적관객수" : response.get('boxOfficeResult').get('weeklyBoxOfficeList')[j].get('audiAcc')
        }})
pprint.pprint(dic)

import csv
with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화이름', '영화코드','누적관객수']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in dic.values():
        csv_writer.writerow(item)