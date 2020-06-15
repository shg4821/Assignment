import json

# 1. 객체 배열 데이터 
areas = '[{"name": " 삼성 ", "area": [" 미국 ", " 홍콩 ", " 싱가포르 "]}, {"name":" 엘지 ", "area": [" 영국 ", " 호주 "]}]'
print(areas) # areas 타입이 string
# print(areas[0][name])

# 스트링 -> json화
areas_d = json.loads(areas)

# 출력 
print(areas_d)
for a in areas_d:
    print("{0} : {1}".format(a['name'], ",".join(a['area'])))