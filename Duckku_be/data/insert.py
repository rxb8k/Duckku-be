import pandas as pd
import json
from collections import OrderedDict

def insertData_Artist():
  artist_txt = open('artist.txt', 'r')
  artist_csv = pd.read_csv(artist_txt, sep='\t')

  artist_data_list=[]
  
  agency_list=artist_csv['agency']
  artist_list=artist_csv['artist']
  # image 필요
  print(artist_list)

  artist_data_list=[]

  for artist, agency in zip(artist_list, agency_list):
    artist_data=OrderedDict()
    artist_data["model"]="album.artist"
    artist_data["fields"]={
      'artist_name' : artist,
      'agency' : agency,
      'artist_image' : '',
    }
    artist_data_list.append(artist_data)
  
  with open('artist-data.json', 'w', encoding="utf-8") as make_file:
    json.dump(artist_data_list, make_file, ensure_ascii=False, indent="\t")

  
insertData_Artist()