from rest_framework import serializers
from .models import User
from artist.serializers import ArtistSerializer
from album.serializers import AlbumSerializer

class UserSerializer(serializers.ModelSerializer):
    userSubartist_type_List = ArtistSerializer(read_only = True,many = True) # many
    userBuyalbum_type_List = AlbumSerializer(read_only = True, many = True)
    usersSubalbum_type_List = AlbumSerializer(read_only = True, many = True)
    
    class Meta:
        model = User
        fields = ['id', 'userEmail', 'userName', 'userSubartist_type_List', 'userBuyalbum_type_List', 'usersSubalbum_type_List', 'ticket_apply_complete', 'ticket_apply_complete']
