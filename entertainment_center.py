import fresh_tomatoes
import media


toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that came blablabla",
    "http://br.web.img3.acsta.net/r_1280_720/pictures/14/03/17/10/20/509771.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )
avatar = media.Movie(
    "Avatar",
    "A story of a man and his friend that came  to war blablabla",
    "https://images-na.ssl-images-amazon.com/images/I/61OUGpUfAyL._SY679_.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "A story of a man and his friend that came  to war blablabla",
    "https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/0/4/047620140408-posters-filmes-retro-pulp-fiction-tarantino.jpg",
    "https://www.youtube.com/watch?v=YBZp3tkua2Y"
    )
hunter = media.Movie(
    "Hunter",
    "A story of a man and his friend that came  to war blablabla",
    "https://filmspot.com.pt/images/filmes/posters/big/399402.jpg",
    "https://www.youtube.com/watch?v=XEm1M1UEjCA"
    )
blackway = media.Movie(
    "Blackway",
    "A story of a man and his friend that came  to war blablabla",
    "http://br.web.img3.acsta.net/r_1920_1080/pictures/16/03/18/15/45/381671.jpg",
    "https://www.youtube.com/watch?v=-MUUX8y0LHw"
    )
um_lugar_silencioso = media.Movie(
    "Um Lugar Silencioso",
    "A story of a man and his friend that came  to war blablabla",
    "https://pm1.narvii.com/6803/1c18c4fd3e8888bc9045d3b328a1a5706af5620dv2_hq.jpg",
    "https://www.youtube.com/watch?v=8W6iMmhVDgE"
    )
movies = [
    toy_story,
    avatar,
    pulp_fiction,
    hunter,
    blackway,
    um_lugar_silencioso
    ]
fresh_tomatoes.open_movies_page(movies)
