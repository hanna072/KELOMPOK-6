import html

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Movie Night | Dashboard Film",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PALET WARNA (dipakai oleh Plotly; CSS memakai nilai yang sama)
# ============================================================

BG = "#0F1C22"        # latar utama (hijau petrol gelap)
SURFACE = "#172A31"   # panel / kartu
LINE = "#2B444D"      # garis & border
TEXT = "#EEF1EA"      # teks utama
MUTED = "#A3B7B8"     # teks sekunder
AMBER = "#F0B340"     # aksen utama (lampu marquee)
CORAL = "#E8705A"     # aksen kedua
SAGE = "#8FBF9F"      # aksen ketiga


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Figtree:wght@400;500;600;700&display=swap');

:root {
    --bg: #0F1C22;
    --surface: #172A31;
    --surface-2: #1E3640;
    --line: #2B444D;
    --text: #EEF1EA;
    --muted: #A3B7B8;
    --dim: #7F9697;
    --amber: #F0B340;
    --coral: #E8705A;
    --sage: #8FBF9F;
    --display: 'Bricolage Grotesque', 'Segoe UI', sans-serif;
    --body: 'Figtree', 'Segoe UI', Arial, sans-serif;
}

/* ---------- Dasar ---------- */

.stApp {
    background: var(--bg);
    color: var(--text);
    font-family: var(--body);
}

.stApp p,
.stApp li,
.stApp label,
.stApp span,
[data-testid="stMarkdownContainer"] {
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu,
footer {
    visibility: hidden;
}

.block-container {
    max-width: 1280px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {
    background: #0B161B;
    border-right: 1px solid var(--line);
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: var(--text);
}

section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    color: var(--muted);
    font-size: 0.88rem;
    font-weight: 600;
}

section[data-testid="stSidebar"] hr {
    border-color: var(--line);
}

.brand {
    font-family: var(--display);
    font-size: 26px;
    font-weight: 800;
    color: var(--text);
    line-height: 1;
}

.brand-sub {
    color: var(--muted);
    font-size: 13px;
    margin-top: 6px;
}

.side-title {
    font-family: var(--display);
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    margin: 4px 0 6px;
}

.side-text {
    color: var(--muted);
    font-size: 13.5px;
    line-height: 1.6;
}

/* ---------- Widget (slider, input) ---------- */

div[data-baseweb="slider"] [role="slider"] {
    background-color: var(--amber);
    box-shadow: none;
}

[data-testid="stSliderThumbValue"] {
    color: var(--amber);
    font-weight: 700;
}

[data-testid="stTickBarMin"],
[data-testid="stTickBarMax"] {
    color: var(--muted);
}

div[data-baseweb="input"],
div[data-baseweb="base-input"] {
    background: var(--surface);
    border-color: var(--line);
    border-radius: 10px;
}

div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input {
    background: var(--surface);
    color: var(--text);
    -webkit-text-fill-color: var(--text);
    font-family: var(--body);
}

div[data-baseweb="input"] input::placeholder {
    color: var(--dim);
    -webkit-text-fill-color: var(--dim);
}

div[data-baseweb="input"]:focus-within {
    border-color: var(--amber);
}

[data-testid="stNumberInputStepDown"],
[data-testid="stNumberInputStepUp"] {
    background: var(--surface-2);
    color: var(--text);
}

/* ---------- Hero ---------- */

.hero {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 34px;
}

.strip {
    height: 22px;
    background:
        linear-gradient(90deg, rgba(240, 179, 64, 0.55) 0 12px, transparent 12px)
        10px 7px / 30px 8px repeat-x,
        #0B161B;
}

.hero-body {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    gap: 32px;
    padding: 38px 44px;
}

.hero-title {
    font-family: var(--display);
    font-size: clamp(34px, 4.6vw, 56px);
    font-weight: 800;
    line-height: 1.05;
    color: var(--text);
    letter-spacing: -0.02em;
    max-width: 14ch;
}

.hero-desc {
    color: var(--muted);
    font-size: 17px;
    line-height: 1.6;
    margin-top: 16px;
    max-width: 52ch;
}

.hero-src {
    display: inline-block;
    margin-top: 18px;
    padding: 5px 12px;
    border-radius: 999px;
    border: 1px solid var(--line);
    color: var(--muted);
    font-size: 13px;
}

.hero-side {
    text-align: right;
    flex-shrink: 0;
}

.hero-big {
    font-family: var(--display);
    font-size: clamp(34px, 4vw, 50px);
    font-weight: 700;
    color: var(--amber);
    line-height: 1;
}

.hero-cap {
    color: var(--muted);
    font-size: 14px;
    margin-top: 8px;
}

@media (max-width: 800px) {
    .hero-body {
        flex-direction: column;
        align-items: flex-start;
        padding: 28px 24px;
    }
    .hero-side {
        text-align: left;
    }
}

/* ---------- Judul bagian ---------- */

.sec {
    margin: 46px 0 20px;
}

.sec-title {
    font-family: var(--display);
    font-size: 30px;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.01em;
    line-height: 1.15;
}

.sec-desc {
    color: var(--muted);
    font-size: 15px;
    margin-top: 6px;
    max-width: 70ch;
    line-height: 1.55;
}

.panel-title {
    font-family: var(--display);
    font-size: 19px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 4px;
}

/* ---------- Statistik ringkas ---------- */

.stat {
    padding: 6px 0 6px 18px;
    border-left: 4px solid var(--amber);
}

.stat.coral { border-left-color: var(--coral); }
.stat.sage  { border-left-color: var(--sage); }
.stat.line  { border-left-color: var(--muted); }

.stat-label {
    color: var(--muted);
    font-size: 14px;
    font-weight: 500;
}

.stat-value {
    font-family: var(--display);
    font-size: 40px;
    font-weight: 700;
    color: var(--text);
    line-height: 1.1;
    margin-top: 4px;
}

.stat-value.small {
    font-size: 21px;
    line-height: 1.25;
    margin-top: 8px;
}

/* ---------- Daftar trending ---------- */

.trend {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    padding: 14px 0;
    border-bottom: 1px solid var(--line);
}

.trend:last-child {
    border-bottom: none;
}

.trend-rank {
    font-family: var(--display);
    font-size: 34px;
    font-weight: 800;
    color: var(--amber);
    line-height: 1;
    min-width: 30px;
}

.trend-info {
    flex: 1;
    min-width: 0;
}

.trend-name {
    font-weight: 700;
    font-size: 16px;
    color: var(--text);
    line-height: 1.3;
}

.trend-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 6px 14px;
    color: var(--muted);
    font-size: 13px;
    margin-top: 5px;
}

.pill {
    display: inline-block;
    padding: 2px 10px;
    border-radius: 999px;
    background: rgba(240, 179, 64, 0.16);
    color: var(--amber);
    font-weight: 700;
    font-size: 12.5px;
}

/* ---------- Insight ---------- */

.insight {
    margin: 28px 0 0;
    padding: 6px 0 6px 22px;
    border-left: 4px solid var(--coral);
}

.insight-title {
    font-family: var(--display);
    font-weight: 700;
    font-size: 18px;
    color: var(--text);
}

.insight-text {
    color: var(--muted);
    font-size: 15.5px;
    line-height: 1.65;
    margin-top: 4px;
    max-width: 75ch;
}

/* ---------- Kartu korelasi ---------- */

.corr {
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 14px;
}

.corr-label {
    color: var(--muted);
    font-size: 14px;
}

.corr-value {
    font-family: var(--display);
    font-size: 38px;
    font-weight: 700;
    color: var(--text);
    margin-top: 4px;
    line-height: 1.1;
}

.corr-note {
    color: var(--muted);
    font-size: 13.5px;
    margin-top: 6px;
}

/* ---------- Tabel ---------- */

.table-wrap {
    overflow-x: auto;
    border: 1px solid var(--line);
    border-radius: 12px;
    background: var(--surface);
}

.tbl {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.tbl th {
    text-align: left;
    padding: 14px 16px;
    background: var(--surface-2);
    color: var(--text);
    font-weight: 700;
    border-bottom: 1px solid var(--line);
    white-space: nowrap;
}

.tbl td {
    padding: 13px 16px;
    color: var(--text);
    border-bottom: 1px solid var(--line);
}

.tbl tr:last-child td {
    border-bottom: none;
}

.tbl tbody tr:hover td {
    background: rgba(240, 179, 64, 0.06);
}

.tbl .num {
    text-align: right;
    font-variant-numeric: tabular-nums;
}

.tbl td.title-cell {
    font-weight: 600;
}

.tbl td.muted {
    color: var(--muted);
}

/* ---------- Footer ---------- */

.footer {
    margin-top: 60px;
    padding-top: 22px;
    border-top: 1px solid var(--line);
    color: var(--dim);
    font-size: 13px;
    text-align: center;
    line-height: 1.7;
}

.footer b {
    font-family: var(--display);
    color: var(--muted);
    font-size: 15px;
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# FUNGSI BANTU
# ============================================================

def render(markup: str) -> None:
    """Tampilkan HTML. Baris dirapatkan agar Markdown tidak
    salah membaca indentasi sebagai blok kode."""
    flat = "".join(line.strip() for line in markup.splitlines())
    st.markdown(flat, unsafe_allow_html=True)


def section(title: str, desc: str = "") -> None:
    desc_html = f'<div class="sec-desc">{desc}</div>' if desc else ""
    render(
        f'<div class="sec">'
        f'<div class="sec-title">{title}</div>'
        f'{desc_html}'
        f'</div>'
    )


def panel_title(text: str) -> None:
    render(f'<div class="panel-title">{text}</div>')


def stat(label: str, value: str, tone: str = "", small: bool = False) -> str:
    size = " small" if small else ""
    return (
        f'<div class="stat {tone}">'
        f'<div class="stat-label">{label}</div>'
        f'<div class="stat-value{size}">{value}</div>'
        f'</div>'
    )


def style_fig(fig, height: int, margin=None):
    """Gaya Plotly yang seragam dan terbaca di tema gelap."""
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Figtree, Segoe UI, sans-serif", color=MUTED, size=13),
        margin=margin or dict(l=10, r=20, t=10, b=10),
        hoverlabel=dict(
            bgcolor=SURFACE,
            bordercolor=AMBER,
            font=dict(family="Figtree, Segoe UI, sans-serif", color=TEXT, size=13),
        ),
        showlegend=False,
    )
    fig.update_xaxes(
        gridcolor=LINE,
        zeroline=False,
        linecolor=LINE,
        tickfont=dict(color=MUTED),
        title_font=dict(color=MUTED),
    )
    fig.update_yaxes(
        gridcolor=LINE,
        zeroline=False,
        linecolor=LINE,
        tickfont=dict(color=MUTED),
        title_font=dict(color=MUTED),
    )
    return fig


def kekuatan_korelasi(r: float) -> str:
    if pd.isna(r):
        return "Data belum cukup untuk dihitung."
    arah = "positif" if r >= 0 else "negatif"
    a = abs(r)
    if a < 0.2:
        level = "sangat lemah"
    elif a < 0.4:
        level = "lemah"
    elif a < 0.6:
        level = "sedang"
    elif a < 0.8:
        level = "kuat"
    else:
        level = "sangat kuat"
    return f"Hubungan {level}, arah {arah}."


def build_table(headers, rows, num_cols=()) -> str:
    """headers: list judul kolom, rows: list of list (sel sudah berupa HTML),
    num_cols: indeks kolom yang rata kanan."""
    head = "".join(
        f'<th class="{"num" if i in num_cols else ""}">{h}</th>'
        for i, h in enumerate(headers)
    )
    body = ""
    for row in rows:
        cells = ""
        for i, cell in enumerate(row):
            cls = []
            if i == 0:
                cls.append("title-cell")
            if i in num_cols:
                cls.append("num")
            cells += f'<td class="{" ".join(cls)}">{cell}</td>'
        body += f"<tr>{cells}</tr>"
    return (
        '<div class="table-wrap"><table class="tbl">'
        f"<thead><tr>{head}</tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table></div>"
    )


# ============================================================
# LOAD DATA
# ============================================================

try:
    df = pd.read_csv("data/film_bersih.csv")
except FileNotFoundError:
    st.error("File data/film_bersih.csv tidak ditemukan.")
    st.stop()


# ============================================================
# DATA CLEANING TAMBAHAN
# ============================================================

for kolom in ["Tahun Rilis", "Rating", "Jumlah Vote", "Popularity"]:
    df[kolom] = pd.to_numeric(df[kolom], errors="coerce")

df = df.dropna(subset=["Tahun Rilis", "Rating", "Jumlah Vote", "Popularity"])
df["Tahun Rilis"] = df["Tahun Rilis"].astype(int)
df["Jumlah Vote"] = df["Jumlah Vote"].astype(int)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    render(
        '<div class="brand">Movie Night</div>'
        '<div class="brand-sub">Dashboard analisis film</div>'
    )
    st.markdown("---")
    render('<div class="side-title">Filter data</div>')

    tahun_min = int(df["Tahun Rilis"].min())
    tahun_max = int(df["Tahun Rilis"].max())

    tahun_range = st.slider(
        "Tahun rilis",
        min_value=tahun_min,
        max_value=tahun_max,
        value=(tahun_min, tahun_max),
    )

    rating_min = st.slider(
        "Rating minimum",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1,
    )

    vote_min = st.number_input(
        "Jumlah vote minimum",
        min_value=0,
        max_value=int(df["Jumlah Vote"].max()),
        value=50,
        step=100,
    )

    st.markdown("---")
    render(
        '<div class="side-title">Tentang dashboard</div>'
        '<div class="side-text">Dashboard ini menganalisis film '
        'berdasarkan rating, popularitas, jumlah vote, tahun rilis, '
        'dan bahasa.</div>'
    )
    st.markdown("---")
    st.caption("Sumber data: TMDB")


# ============================================================
# FILTER DATA
# ============================================================

data = df[
    (df["Tahun Rilis"] >= tahun_range[0])
    & (df["Tahun Rilis"] <= tahun_range[1])
    & (df["Rating"] >= rating_min)
    & (df["Jumlah Vote"] >= vote_min)
].copy()


# ============================================================
# HERO
# ============================================================

render(
    f"""
    <div class="hero">
        <div class="strip"></div>
        <div class="hero-body">
            <div class="hero-main">
                <div class="hero-title">Dashboard Analisis Film Populer</div>
                <div class="hero-desc">Temukan tren, rating, popularitas,
                dan fakta menarik dari dunia perfilman.</div>
                <span class="hero-src">Data bersumber dari TMDB</span>
            </div>
            <div class="hero-side">
                <div class="hero-big">{tahun_range[0]} sampai {tahun_range[1]}</div>
                <div class="hero-cap">rentang tahun rilis yang dipilih</div>
            </div>
        </div>
        <div class="strip"></div>
    </div>
    """
)


# ============================================================
# DATA KOSONG
# ============================================================

if data.empty:
    st.warning(
        "Tidak ada film yang sesuai dengan filter. "
        "Coba turunkan rating minimum atau jumlah vote minimum."
    )
    st.stop()


# ============================================================
# RINGKASAN STATISTIK
# ============================================================

section("Ringkasan statistik", "Gambaran umum dari film yang lolos filter.")

film_populer = data.loc[data["Popularity"].idxmax()]
judul_populer = html.escape(str(film_populer["Judul Film"]))

k1, k2, k3, k4 = st.columns(4)

with k1:
    render(stat("Jumlah film", f"{len(data):,}", "coral"))

with k2:
    render(stat("Rata-rata rating", f'{data["Rating"].mean():.2f}', ""))

with k3:
    render(stat("Rata-rata vote", f'{data["Jumlah Vote"].mean():,.0f}', "sage"))

with k4:
    render(stat("Film terpopuler", judul_populer, "line", small=True))


# ============================================================
# FILM PALING POPULER
# ============================================================

section(
    "Film paling populer",
    "Sepuluh film dengan skor popularitas tertinggi, dan lima yang sedang naik daun.",
)

chart_col, trend_col = st.columns([2.1, 1], gap="large")

with chart_col:
    panel_title("Top 10 popularitas")

    top10 = (
        data.sort_values("Popularity", ascending=False)
        .head(10)
        .copy()
    )

    top10["Judul Pendek"] = (
        top10["Judul Film"]
        .astype(str)
        .apply(lambda x: x[:26] + "..." if len(x) > 26 else x)
    )

    top10 = top10.sort_values("Popularity", ascending=True)

    # Film teratas diberi warna penuh, sisanya lebih redup
    warna_bar = ["rgba(240,179,64,0.42)"] * (len(top10) - 1) + [AMBER]

    fig = px.bar(
        top10,
        x="Popularity",
        y="Judul Pendek",
        orientation="h",
        text="Popularity",
    )

    fig.update_traces(
        marker_color=warna_bar,
        texttemplate="%{text:.1f}",
        textposition="outside",
        textfont=dict(color=TEXT),
        cliponaxis=False,
        customdata=top10[["Judul Film", "Rating"]],
        hovertemplate=(
            "<b>%{customdata[0]}</b>"
            "<br>Popularity: %{x:.2f}"
            "<br>Rating: %{customdata[1]:.2f}"
            "<extra></extra>"
        ),
    )

    style_fig(fig, height=450, margin=dict(l=10, r=50, t=10, b=10))
    fig.update_xaxes(
        title="Popularity",
        range=[0, top10["Popularity"].max() * 1.15],
    )
    fig.update_yaxes(title="", gridcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


with trend_col:
    panel_title("Sedang tren")

    trending = data.sort_values("Popularity", ascending=False).head(5)

    items = ""
    for nomor, (_, film) in enumerate(trending.iterrows(), start=1):
        judul = html.escape(str(film["Judul Film"]))
        items += (
            f'<div class="trend">'
            f'<div class="trend-rank">{nomor}</div>'
            f'<div class="trend-info">'
            f'<div class="trend-name">{judul}</div>'
            f'<div class="trend-meta">'
            f'<span>Rilis {int(film["Tahun Rilis"])}</span>'
            f'<span>{int(film["Jumlah Vote"]):,} vote</span>'
            f'<span class="pill">Rating {film["Rating"]:.1f}</span>'
            f'</div>'
            f'</div>'
            f'</div>'
        )

    render(f"<div>{items}</div>")


render(
    '<div class="insight">'
    '<div class="insight-title">Populer belum tentu berating tinggi</div>'
    '<div class="insight-text">Popularitas film tidak selalu berarti '
    'ratingnya paling tinggi. Gunakan analisis di bawah untuk melihat '
    'hubungan antara rating, popularitas, dan jumlah vote.</div>'
    '</div>'
)


# ============================================================
# FILM PER TAHUN
# ============================================================

section(
    "Perkembangan film berdasarkan tahun",
    "Jumlah film yang dirilis tiap tahun pada rentang yang dipilih.",
)

per_tahun = (
    data.groupby("Tahun Rilis")
    .size()
    .reset_index(name="Jumlah Film")
)

fig_year = px.bar(per_tahun, x="Tahun Rilis", y="Jumlah Film")

fig_year.update_traces(
    marker_color=SAGE,
    hovertemplate="Tahun: %{x}<br>Jumlah film: %{y}<extra></extra>",
)

style_fig(fig_year, height=380, margin=dict(l=10, r=10, t=10, b=10))
fig_year.update_xaxes(title="Tahun rilis", gridcolor="rgba(0,0,0,0)")
fig_year.update_yaxes(title="Jumlah film")

st.plotly_chart(fig_year, use_container_width=True, config={"displayModeBar": False})


# ============================================================
# RATING VS POPULARITY
# ============================================================

section(
    "Rating dan popularitas",
    "Setiap titik adalah satu film. Arahkan kursor untuk melihat judulnya.",
)

scatter_col, corr_col = st.columns([2.2, 1], gap="large")

with scatter_col:
    fig_scatter = px.scatter(
        data,
        x="Rating",
        y="Popularity",
        hover_name="Judul Film",
        hover_data={
            "Rating": ":.2f",
            "Popularity": ":.2f",
            "Jumlah Vote": ":,",
            "Tahun Rilis": True,
        },
    )

    fig_scatter.update_traces(
        marker=dict(
            size=9,
            color=AMBER,
            opacity=0.6,
            line=dict(width=1, color=BG),
        )
    )

    style_fig(fig_scatter, height=460, margin=dict(l=10, r=10, t=10, b=10))
    fig_scatter.update_xaxes(title="Rating", range=[0, 10], dtick=1)
    fig_scatter.update_yaxes(title="Popularity")

    st.plotly_chart(
        fig_scatter,
        use_container_width=True,
        config={"displayModeBar": False},
    )

korelasi_popularity = data[["Rating", "Popularity"]].corr().iloc[0, 1]
korelasi_vote = data[["Rating", "Jumlah Vote"]].corr().iloc[0, 1]

with corr_col:
    nilai_pop = "-" if pd.isna(korelasi_popularity) else f"{korelasi_popularity:.3f}"
    nilai_vote = "-" if pd.isna(korelasi_vote) else f"{korelasi_vote:.3f}"

    render(
        f'<div class="corr">'
        f'<div class="corr-label">Korelasi rating dan popularity</div>'
        f'<div class="corr-value">{nilai_pop}</div>'
        f'<div class="corr-note">{kekuatan_korelasi(korelasi_popularity)}</div>'
        f'</div>'
        f'<div class="corr">'
        f'<div class="corr-label">Korelasi rating dan jumlah vote</div>'
        f'<div class="corr-value">{nilai_vote}</div>'
        f'<div class="corr-note">{kekuatan_korelasi(korelasi_vote)}</div>'
        f'</div>'
    )


# ============================================================
# RATING TERTINGGI
# ============================================================

section(
    "Film dengan rating tertinggi",
    "Hanya film dengan minimal 100 vote yang dihitung, supaya rating lebih bisa dipercaya.",
)

top_rating = (
    data[data["Jumlah Vote"] >= 100]
    .sort_values("Rating", ascending=False)
    .head(10)
)

rows = []
for _, film in top_rating.iterrows():
    rows.append(
        [
            html.escape(str(film["Judul Film"])),
            f'{int(film["Tahun Rilis"])}',
            f'<span class="pill">{film["Rating"]:.3f}</span>',
            f'{int(film["Jumlah Vote"]):,}',
            f'{film["Popularity"]:.2f}',
        ]
    )

if rows:
    render(
        build_table(
            ["Judul film", "Tahun", "Rating", "Jumlah vote", "Popularity"],
            rows,
            num_cols=(1, 2, 3, 4),
        )
    )
else:
    st.info("Belum ada film dengan 100 vote atau lebih pada filter ini.")


# ============================================================
# PENCARIAN FILM
# ============================================================

section(
    "Cari film",
    "Ketik sebagian judul untuk mencari. Jika kosong, ditampilkan 20 film pertama.",
)

search = st.text_input(
    "Cari berdasarkan judul film",
    placeholder="Contoh: Spider-Man",
)

if search:
    data_search = data[
        data["Judul Film"]
        .astype(str)
        .str.contains(search, case=False, na=False, regex=False)
    ].copy()
else:
    data_search = data.head(20).copy()

if data_search.empty:
    st.info("Tidak ada judul yang cocok. Coba kata kunci yang lebih pendek.")
else:
    search_rows = []
    for _, film in data_search.iterrows():
        search_rows.append(
            [
                html.escape(str(film["Judul Film"])),
                f'{int(film["Tahun Rilis"])}',
                f'<span style="color:var(--muted)">{html.escape(str(film["Genre"]))}</span>',
                f'<span class="pill">{film["Rating"]:.2f}</span>',
                f'{int(film["Jumlah Vote"]):,}',
                f'{film["Popularity"]:.2f}',
                html.escape(str(film["Bahasa"])),
            ]
        )

    render(
        build_table(
            ["Judul film", "Tahun", "Genre", "Rating", "Vote", "Popularity", "Bahasa"],
            search_rows,
            num_cols=(1, 3, 4, 5),
        )
    )


# ============================================================
# FOOTER
# ============================================================

render(
    '<div class="footer">'
    '<b>Movie Night</b><br>'
    'Dashboard analisis film populer, memakai dataset TMDB'
    '</div>'
)