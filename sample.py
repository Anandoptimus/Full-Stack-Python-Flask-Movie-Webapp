import requests
from requests.auth import HTTPBasicAuth
API_KEY = '2f151d0fc4b9be61f32863baca136d71'
API_LINK = "https://api.themoviedb.org/3/search/movie"

parama = {
    "query": "Fight Club",
    "language": "en-US",
    "api_key": API_KEY
}
url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

headers = {"Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en;q=0.9"
           }

response = requests.get(f"https://api.themoviedb.org/3/movie/550", params={"api_key": API_KEY})
print(response.json()["original_title"])
print(response.json()["poster_path"])
print(response.json()["overview"])
print(response.json()["release_date"].split("-")[0])





# {'adult': False, 'backdrop_path': '/hZkgoQYus5vegHoetLkCJzb17zJ.jpg', 'genre_ids': [18], 'id': 550, 'original_language': 'en', 'original_title': 'Fight Club', 'overview': 'A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground "fight clubs" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.', 'popularity': 85.852, 'poster_path': '/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg', 'release_date': '1999-10-15', 'title': 'Fight Club', 'video': False, 'vote_average': 8.44, 'vote_count': 27584}