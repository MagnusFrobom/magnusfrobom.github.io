from pytube import Playlist
p = Playlist('https://www.youtube.com/watch?v=_3f_t0qHPmo&list=PLMUVYRN636-Qh1Nb0HHa39nCSAjsgNZYa')

print(f'Downloading: {p.title}')

for video in p.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download('C:\M.O')