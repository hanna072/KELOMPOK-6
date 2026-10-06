import urllib.request
import urllib.parse
import json
import csv
import os
import time

# =========================================================
# MASUKKAN API READ ACCESS TOKEN TMDB KAMU DI SINI
# Jangan bagikan token ini kepada orang lain.
# =========================================================
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNWNkZjdmYzAzZDFlYWEyMWI0ZDdkNDdiZGUxOTQwYyIsIm5iZiI6MTc5MTE3MTk3NS42OTcsInN1YiI6IjZhYzMxZDg3YjZjOTZiYjdjOWRjYzVmMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.SxR79gc3YGJSQMHGzdDRvuqJJNQfP9xvzQQiBT1925s"

# =========================================================
# PENGATURAN
# =========================================================

URL = "https://api.themoviedb.org/3/discover/movie"

# 50 halaman x sekitar 20 film = sekitar 1.000 film
JUMLAH_HALAMAN = 50


# =========================================================
# DAFTAR GENRE TMDB
# =========================================================

genre_dict = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}


# =========================================================
# TEMPAT MENYIMPAN SEMUA DATA FILM
# =========================================================

hasil = []


# =========================================================
# MENGAMBIL DATA DARI TMDB
# =========================================================

print("Mulai mengambil data dari TMDB...")
print("Target:", JUMLAH_HALAMAN * 20, "film")
print()

for halaman in range(1, JUMLAH_HALAMAN + 1):

    print(f"Mengambil halaman {halaman}/{JUMLAH_HALAMAN}...")

    parameter = {
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "include_video": "false",
        "page": halaman
    }

    query_string = urllib.parse.urlencode(parameter)

    url_lengkap = URL + "?" + query_string

    request = urllib.request.Request(
        url_lengkap,
        method="GET"
    )

    request.add_header(
        "Authorization",
        "Bearer " + TOKEN
    )

    request.add_header(
        "accept",
        "application/json"
    )

    try:

        response = urllib.request.urlopen(request)

        data_json = response.read()

        data = json.loads(data_json)

        film_list = data.get("results", [])

        # =============================================
        # MEMPROSES SETIAP FILM
        # =============================================

        for film in film_list:

            # Judul
            judul = film.get("title", "")

            # Tahun rilis
            tanggal = film.get("release_date", "")

            if tanggal:
                tahun = tanggal[:4]
            else:
                tahun = ""

            # Genre
            genre_ids = film.get("genre_ids", [])

            genre_nama = []

            for genre_id in genre_ids:

                if genre_id in genre_dict:
                    genre_nama.append(
                        genre_dict[genre_id]
                    )

            genre = ", ".join(genre_nama)

            # Rating
            rating = film.get(
                "vote_average",
                0
            )

            # Jumlah vote
            jumlah_vote = film.get(
                "vote_count",
                0
            )

            # Popularity
            popularity = film.get(
                "popularity",
                0
            )

            # Bahasa
            bahasa = film.get(
                "original_language",
                ""
            )

            # Masukkan ke hasil
            hasil.append({

                "Judul Film": judul,

                "Tahun Rilis": tahun,

                "Genre": genre,

                "Rating": rating,

                "Jumlah Vote": jumlah_vote,

                "Popularity": popularity,

                "Bahasa": bahasa
            })

    except Exception as error:

        print()
        print("Terjadi kesalahan pada halaman", halaman)
        print(error)
        print()

        # Lanjut ke halaman berikutnya
        continue

    # Jeda sebentar supaya request tidak terlalu cepat
    time.sleep(0.1)


# =========================================================
# MENYIMPAN DATA KE CSV
# =========================================================

os.makedirs("data", exist_ok=True)

nama_file = "data/film.csv"

kolom = [
    "Judul Film",
    "Tahun Rilis",
    "Genre",
    "Rating",
    "Jumlah Vote",
    "Popularity",
    "Bahasa"
]


with open(
    nama_file,
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=kolom
    )

    writer.writeheader()

    writer.writerows(hasil)


# =========================================================
# HASIL AKHIR
# =========================================================

print()
print("==============================")
print("DATA BERHASIL DISIMPAN!")
print("==============================")

print("Lokasi:", nama_file)

print("Jumlah data:", len(hasil))

print()

print("Kolom data:")

for kolom_data in kolom:
    print("-", kolom_data)

print()

print("Selesai!")
