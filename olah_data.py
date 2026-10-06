import pandas as pd

# ==========================================
# 1. MEMBACA DATA MENTAH
# ==========================================

nama_file = "data/film.csv"

df = pd.read_csv(nama_file)

print("DATA BERHASIL DIBACA!")
print("Jumlah data awal:", len(df))
print()


# ==========================================
# 2. MENGUBAH TIPE DATA
# ==========================================

df["Tahun Rilis"] = pd.to_numeric(
    df["Tahun Rilis"],
    errors="coerce"
)

df["Rating"] = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

df["Jumlah Vote"] = pd.to_numeric(
    df["Jumlah Vote"],
    errors="coerce"
)

df["Popularity"] = pd.to_numeric(
    df["Popularity"],
    errors="coerce"
)


# ==========================================
# 3. MENGHAPUS DATA TANPA JUDUL
# ==========================================

df = df.dropna(
    subset=["Judul Film"]
)


# ==========================================
# 4. MENGHAPUS DATA TANPA RATING
# ==========================================

df = df.dropna(
    subset=["Rating"]
)


# ==========================================
# 5. MENGHAPUS DATA DUPLIKAT
# ==========================================

df = df.drop_duplicates()


# ==========================================
# 6. MEMBATASI RATING 0-10
# ==========================================

df = df[
    (df["Rating"] >= 0) &
    (df["Rating"] <= 10)
]


# ==========================================
# 7. MENGISI GENRE KOSONG
# ==========================================

df["Genre"] = df["Genre"].fillna(
    "Unknown"
)


# ==========================================
# 8. MENYIMPAN DATA BERSIH
# ==========================================

nama_file_bersih = "data/film_bersih.csv"

df.to_csv(
    nama_file_bersih,
    index=False,
    encoding="utf-8-sig"
)


# ==========================================
# 9. HASIL PEMBERSIHAN
# ==========================================

print("==============================")
print("PEMBERSIHAN DATA SELESAI!")
print("==============================")

print("Jumlah data awal :", 1000)

print("Jumlah data akhir:", len(df))

print(
    "Data yang dihapus:",
    1000 - len(df)
)

print()

print(
    "File tersimpan:",
    nama_file_bersih
)

print()

print("Data kosong setelah dibersihkan:")

print(df.isnull().sum())

print()

print("==============================")
print("SELESAI!")
print("==============================")