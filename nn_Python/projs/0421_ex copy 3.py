import urllib.request
import xml.etree.ElementTree as etree

class GetData:
    # 파라미터 
    page = '1'              # 페이지수 
    row = '10'              # 페이지당 목록 수 
    sDate = '20200310'      # 조회 시작일 : YYYYMMDD
    eDate = '20200422'      # 조회 종료일 : YYYYMMDD
    # 파라미터 조합 
    params = '&' + 'pageNo=' + page + '&' + 'numOfRows=' + row + '&' + 'startCreateDt=' + sDate + '&' + 'endCreateDt=' + eDate
    # API  인증키 
    key = 'pheKFj8Pv7Uv7EnJIYCWrt2jBSOo6WalN3YPI08%' + '2FjDXHKtpOthPuS4atzK7C8W2xQv071%' + '2FNJej2ceRkz9T6QYg%3D%3D'

    # Open API URL 
    url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=' + key + params


    def main(self):
        #1. 서버에서 데이터를 가져와서 파일로 저장
        data = urllib.request.urlopen(self.url).read()
        f = open("covid19.xml", "wb")
        f.write(data) #파일로 저장됨
        f.close()

        #2. 파일을 읽어서 파싱
        tree = etree.parse('covid19.xml')
        root = tree.getroot()

        #3.출력
        print('===========')
        for a in root.findall('item'):
            print(a.findtext('decideCnt'))
            print(a.findtext('clearCnt'))
            print(a.findtext('deathCnt'))
            print('------------------')

getData = GetData()
if __name__ == '__main__':
    getData.main()
