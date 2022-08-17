import pandas as pd
import json
from collections import OrderedDict
import glob

ALL_MEMBERS=[]
MEMBER_GROUP={} # 멤버-그룹 매핑
ARTIST_ID={} # 아티스트 PK
#   {'소녀시대': 1, '레드벨벳': 2, '에스파': 3, 'BTS': 4, '세븐틴': 5, '블랙핑크': 6, 
#   '트와이스': 7, 'ITZY': 8, '아이브': 9, '몬스타액스': 10, '아이들': 11, '아이유': 12}

group_mem_txt=open('group_members.txt','r')
group_mem_csv=pd.read_csv(group_mem_txt, sep='\t')
member_list=group_mem_csv['Member']
group_list=group_mem_csv['Group']
MEMBER_GROUP={ m:g for m, g in zip(member_list, group_list) }


# 아티스트 객체 JSON 데이터 생성
def makeJsonData_Artist():
  artist_data_list=[]
  artist_txt = open('artist.txt', 'r')
  artist_csv = pd.read_csv(artist_txt, sep='\t')

  id_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  artist_list=artist_csv['artist']
  agency_list=artist_csv['agency']
  image_list=glob.glob('./img/artist/*.jpg') # 경로 확인 필요

  for id, artist, agency, img in zip(id_list, artist_list, agency_list, image_list):
    artist_data=OrderedDict()
    artist_data["model"]="album.Artist"
    artist_data["fields"]={
      'id' : id,
      'artist_name' : artist,
      'agency' : agency,
      'artist_image' : img,
    }
    ARTIST_ID[artist]=id
    artist_data_list.append(artist_data)
  
  with open('artist-data.json', 'w', encoding="utf-8") as make_file:
    json.dump(artist_data_list, make_file, ensure_ascii=False, indent="\t")



# 앨범 객체 JSON 데이터 생성
def makeJsonData_Album():
  album_data_list=[]
  album_xlsx=pd.read_excel('album.xlsx')
  
  album_name_list=album_xlsx['앨범명']
  agency_list=album_xlsx['소속사']
  created_year_list=album_xlsx['발매년도']
  created_month_list=album_xlsx['발매월']
  artist_list=album_xlsx['아티스트']
  music_list=album_xlsx['수록곡목록']
  price_withT_list=album_xlsx['응모권포함가격']
  price_withoutT_list=album_xlsx['응모권미포함가격']
  album_type_list=album_xlsx['앨범 종류']

  for album, agency, artist, albumType, year, month, music, priceWithT, priceWithout in zip(album_name_list, agency_list, artist_list, album_type_list, 
  created_year_list, created_month_list, music_list, price_withT_list, price_withoutT_list):
    album_data=OrderedDict()
    album_data["model"]="album.Album"
    album_data["fields"]={
      'name' : album,
      'agency' : agency,
      'created_at' : f"{year}-{month}-1 00:00:00",
      'artist' : ARTIST_ID[artist], # fk
      'album_image' : '',
      'music_list' : music,
      'price_with_ticket' : priceWithT,
      'price_without_ticket' : priceWithout,
    }
    album_data_list.append(album_data)
  
  with open('album-data.json', 'w', encoding="utf-8") as make_file:
    json.dump(album_data_list, make_file, ensure_ascii=False, indent="\t")



# 포토카드 객체 JSON 데이터 생성
def makeJsonData_Photocard():
  photocard_data_list=[]
  image_list=glob.glob('./img/photocard/*.jpg') # 경로 확인 필요

  album_xlsx=pd.read_excel('album.xlsx')
  
  album_name_list=album_xlsx['앨범명']
  artist_list=album_xlsx['아티스트']

  for Photoimg in image_list: # 하나의 포토카드 이미지에 대해
    for album in album_name_list: # 앨범 개수만큼의 포토카드 객체 생성
        photocard_data=OrderedDict()
        name=Photoimg[16:-5]
        photocard_data["model"]="album.Photocard"
        photocard_data["fields"]={
          'id' : 1,
          'album_id' : album, # fk
          'artist' : MEMBER_GROUP[name], # fk
          'img' : Photoimg,
          'name' : name,
          'album_image' : '',
        }
        # if name not in ALL_MEMBERS: ALL_MEMBERS.append(Photoimg[16:-5])
        photocard_data_list.append(photocard_data)
      
    with open('photocard-data.json', 'w', encoding="utf-8") as make_file:
      json.dump(photocard_data_list, make_file, ensure_ascii=False, indent="\t")


# 각 모델에 대해 makeJsonData 함수 실행
makeJsonData_Artist()
makeJsonData_Album()
makeJsonData_Photocard()