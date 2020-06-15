import pymongo
from pymongo import MongoClient

# 1. 몽고디비 연결 
client = MongoClient('mongodb://localhost:27017/')
print("client.HOST:{0}".format(client.HOST))
# 2. 데이터베이스 생성 
# db = client['데이터베이스 이름']
mdb = client['mdb_py2']
print(mdb)

# 3. 컬렉션 생성 
# 3-1 컬렉션 객체 생성 
coms = mdb.coms
# 3-2 데이터 입력
com = [ 
    {"국가" : "중국", "회사명" : "Xiaomi",       "대표제품" : ["보조배터리", "미밴드",   "공기청정기"]},
    {"국가" : "미국", "회사명" : "Apple",        "대표제품" : ["아이폰",     "아이패드", "맥북"]},
    {"국가" : "독일", "회사명" : "Benz",         "대표제품" : ["S클래스",    "E클래스",  "지바겐"]},
    {"국가" : "일본", "회사명" : "SoftBank",     "대표제품" : ["반도체",     "전자기기", "배터리"]},
    {"국가" : "한국", "회사명" : "Samsung",      "대표제품" : [" 스마트폰 ", "TV",       "반도체"]}
]
# 3-3 데이터 인서트 
result_ds = coms.insert_many(com)
print(result_ds)
# 3-4 컬렉션 조회 
mdb.list_collection_names()
# 3-5 컬렉션 삭제 
#coms.drop()
# 4. 모든 도큐먼트 조회
#for c in coms.find({"국가" : "한국"}):
#    print(com)

# 11. w정렬
print("== 회사명 내림차순 정렬 ==")
coms_sort = coms.find().sort("회사명", -1)
for c in coms_sort:
    print(c)



print("=== The End ===")