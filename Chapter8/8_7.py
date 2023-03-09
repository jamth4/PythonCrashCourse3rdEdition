def make_album(artist, album_title):
    """builds a dictionary of albums"""
    album = {'artist': artist.title(), 'album': album_title.title()}
    return album

album1 = make_album('bob dylan', 'blonde on blonde')
print(album1)

album2 = make_album('green day', 'dookie')
print(album2)

album3 = make_album('the beatles', 'yellow submarine')
print(album3)