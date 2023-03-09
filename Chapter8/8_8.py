def make_album(artist, album_title):
    """builds a dictionary of albums"""
    album = {'artist': artist.title(), 'album': album_title.title()}
    return album

while True:
    print('Tell me your favorite albums')
    print('(type q when you are done)')
    artist = input("Who is the artist:\n")
    if artist == 'q':
        break
    album = input("What is the name of the album:\n")
    if album == 'q':
        break
    album_dictionary = make_album(artist, album)
    print(album_dictionary)
