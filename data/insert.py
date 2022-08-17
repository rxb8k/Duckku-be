import pandas as pd
import json
from collections import OrderedDict
import glob

ARTIST_ID={}
# {'소녀시대': 1, '레드벨벳': 2, '에스파': 3, 'BTS': 4, '세븐틴': 5, '블랙핑크': 6, 
# '트와이스': 7, 'ITZY': 8, '아이브': 9, '몬스타액스': 10, '아이들': 11, '아이유': 12}

def makeJsonData_Artist():
  artist_txt = open('artist.txt', 'r')
  artist_csv = pd.read_csv(artist_txt, sep='\t')
  artist_data_list=[]

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



def makeJsonData_Album():
  album_xlsx=pd.read_excel('album.xlsx')
  album_data_list=[]
  
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



def makeJsonData_Photocard():
  photocard_data_list=[]
  for album in zip():
    photocard_data=OrderedDict()
    photocard_data["model"]="album.Photocard"
    photocard_data["fields"]={
      'album_id' : album, # fk
      'artist' : artist, # fk
      'img' : f"{year}-{month}-1 00:00:00",
      'name' : ARTIST_ID[artist],
      'album_image' : '',
    }
    photocard_data_list.append(photocard_data)
  
  with open('photocard-data.json', 'w', encoding="utf-8") as make_file:
    json.dump(photocard_data_list, make_file, ensure_ascii=False, indent="\t")


# 각 모델에 대해 makeJsonData 함수 실행
makeJsonData_Artist()
makeJsonData_Album()
makeJsonData_Photocard()