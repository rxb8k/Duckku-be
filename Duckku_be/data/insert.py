import pandas as pd
import json
from collections import OrderedDict
import glob

def makeJsonData_Artist():
  artist_txt = open('artist.txt', 'r')
  artist_csv = pd.read_csv(artist_txt, sep='\t')

  artist_data_list=[]
  
  agency_list=artist_csv['agency']
  artist_list=artist_csv['artist']
  image_list=glob.glob('./img/artist/*.jpg') # 경로 확인 필요
  print(artist_list)
  print(image_list)

  artist_data_list=[]

  for artist, agency, img in zip(artist_list, agency_list, image_list):
    artist_data=OrderedDict()
    artist_data["model"]="album.artist"
    artist_data["fields"]={
      'artist_name' : artist,
      'agency' : agency,
      'artist_image' : img,
    }
    artist_data_list.append(artist_data)
  
  with open('artist-data.json', 'w', encoding="utf-8") as make_file:
    json.dump(artist_data_list, make_file, ensure_ascii=False, indent="\t")

  
# makeJsonData 함수 실행
makeJsonData_Artist()