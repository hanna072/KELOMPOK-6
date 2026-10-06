import pandas as pd

# ==========================================
# 1. MEMBACA DATA
# ==========================================

df = pd.read_csv("data/film_bersih.csv")

print("======================================")
print("       ANALISIS DATA FILM")
print("======================================")

print("Jumlah film:", len(df))
print()


# ==========================================
# 2. STATISTIK RATING
# ==========================================

print("===== STATISTIK RATING =====")

print("Rata-rata rating:", round(df["Rating"].mean(), 2))
print("Median rating:", df["Rating"].median())
print("Rating minimum:", df["Rating"].min())
print("Rating maksimum:", df["Rating"].max())
print("Standar deviasi:", round(df["Rating"].std(), 2))

print()


# ==========================================
# 3. TOP 10 FILM PALING POPULER
# ==========================================

print("===== TOP 10 FILM PALING POPULER =====")

top_populer = df.sort_values(
    "Popularity",
    ascending=False
).head(10)

print(
    top_populer[
        ["Judul Film", "Tahun Rilis", "Rating", "Jumlah Vote", "Popularity"]
    ].to_string(index=False)
)

print()


# ==========================================
# 4. TOP 10 RATING TERTINGGI
#    DENGAN MINIMAL 100 VOTE
# ==========================================

print("===== TOP 10 RATING TERTINGGI =====")

film_rating = df[
    df["Jumlah Vote"] >= 100
]

top_rating = film_rating.sort_values(
    "Rating",
    ascending=False
).head(10)

print(
    top_rating[
        ["Judul Film", "Tahun Rilis", "Rating", "Jumlah Vote"]
    ].to_string(index=False)
)

print()


# ==========================================
# 5. JUMLAH FILM BERDASARKAN TAHUN
# ==========================================

print("===== JUMLAH FILM BERDASARKAN TAHUN =====")

film_per_tahun = (
    df.dropna(subset=["Tahun Rilis"])
      .groupby("Tahun Rilis")
      .size()
      .sort_values(ascending=False)
)

print(film_per_tahun.head(10))

print()


# ==========================================
# 6. JUMLAH FILM BERDASARKAN BAHASA
# ==========================================

print("===== JUMLAH FILM BERDASARKAN BAHASA =====")

film_per_bahasa = (
    df["Bahasa"]
    .value_counts()
)

print(film_per_bahasa.head(10))

print()


# ==========================================
# 7. KORELASI RATING DAN POPULARITY
# ==========================================

print("===== KORELASI RATING DAN POPULARITY =====")

korelasi = df[
    ["Rating", "Popularity"]
].corr().loc["Rating", "Popularity"]

print(
    "Korelasi Pearson:",
    round(korelasi, 3)
)

print()


# ==========================================
# 8. KORELASI RATING DAN JUMLAH VOTE
# ==========================================

print("===== KORELASI RATING DAN JUMLAH VOTE =====")

korelasi_vote = df[
    ["Rating", "Jumlah Vote"]
].corr().loc["Rating", "Jumlah Vote"]

print(
    "Korelasi Pearson:",
    round(korelasi_vote, 3)
)

print()


# ==========================================
# SELESAI
# ==========================================

print("======================================")
print("       ANALISIS SELESAI!")
print("======================================")