import streamlit as st
import pickle

songs=pickle.load(open('songslist.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

song_lists=songs['song']
st.image("https://wallpapertag.com/wallpaper/full/1/f/d/892472-best-music-background-image-1920x1200-hd.jpg")
st.title("Music Recommendation System")
s="select the song you recently played"
song=st.selectbox(s,song_lists)
if st.button("Recommend"):
        idx = songs[songs['song'] == song].index[0]
        dist = sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[1:7]
        son= []
        art=[]
        for m_id in dist:
            son.append(songs.iloc[m_id[0]].song)
            art.append(songs.iloc[m_id[0]].artist)

        st.write("Songs You can also try")
        col1, col2, col3, col4, col5 ,col6= st.columns(6)
        with col1:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[0])
            st.text("Artist:"+art[0])
        with col2:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[1])
            st.text("Artist:"+art[1])

        with col3:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[2])
            st.text("Artist:"+art[2])
        with col4:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[3])
            st.text("Artist:"+art[3])
        with col5:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[4])
            st.text("Artist:"+art[4])
        with col6:
            st.image("https://tse2.mm.bing.net/th?id=OIP.u2iuTt6Ru2K53TtnKaJRQwHaHa&pid=Api&P=0&h=180.jpg")
            st.text(son[5])
            st.text("Artist:"+art[5])