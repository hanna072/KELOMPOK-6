import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import html


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Movie Night | Dashboard Film",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# THEME / CSS
# ============================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 0%,
            rgba(255, 30, 90, 0.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 20%,
            rgba(120, 50, 220, 0.12),
            transparent 30%
        ),
        #070811;
    color: #f5f5f7;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0c0e1b 0%,
            #090b16 100%
        );

    border-right: 1px solid rgba(255, 50, 100, 0.22);
}

section[data-testid="stSidebar"] * {
    color: #eeeeF5 !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.08);
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    position: relative;

    padding: 42px 46px;

    border-radius: 26px;

    background:
        radial-gradient(
            circle at 85% 30%,
            rgba(255, 40, 100, 0.20),
            transparent 32%
        ),
        linear-gradient(
            120deg,
            #151027,
            #27091e 55%,
            #100b20
        );

    border: 1px solid rgba(255, 50, 100, 0.35);

    box-shadow:
        0 0 45px rgba(255, 30, 90, 0.10),
        inset 0 0 40px rgba(120, 50, 220, 0.05);

    margin-bottom: 30px;
}

.hero-label {
    color: #ff5478;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 5px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 48px;
    font-weight: 900;
    line-height: 1.08;

    background:
        linear-gradient(
            90deg,
            #ffffff 0%,
            #ffb0c0 45%,
            #ff3f6d 100%
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #b7bac9;
    font-size: 16px;
    margin-top: 12px;
}

.hero-source {
    color: #ff718e;
    font-size: 13px;
    margin-top: 20px;
}


/* =========================================================
   SECTION
   ========================================================= */

.section-title {
    font-size: 27px;
    font-weight: 850;
    color: #ffffff;
    margin-top: 30px;
    margin-bottom: 18px;
}


/* =========================================================
   KPI CARDS
   ========================================================= */

.kpi {
    background:
        linear-gradient(
            145deg,
            rgba(24, 27, 48, 0.98),
            rgba(11, 13, 26, 0.98)
        );

    border-radius: 18px;

    padding: 20px;

    min-height: 135px;

    border: 1px solid rgba(255,255,255,0.07);

    box-shadow:
        0 10px 30px rgba(0,0,0,0.25);
}

.kpi-red {
    border-top: 3px solid #ff315d;
}

.kpi-blue {
    border-top: 3px solid #3b82f6;
}

.kpi-yellow {
    border-top: 3px solid #f4bd45;
}

.kpi-purple {
    border-top: 3px solid #a855f7;
}

.kpi-icon {
    font-size: 27px;
}

.kpi-label {
    color: #9297aa;
    font-size: 13px;
    margin-top: 8px;
}

.kpi-value {
    color: #ffffff;
    font-size: 27px;
    font-weight: 850;
    margin-top: 6px;
}


/* =========================================================
   TRENDING CARDS
   ========================================================= */

.trending-card {
    background:
        linear-gradient(
            145deg,
            #15182b,
            #0c0e1c
        );

    border-radius: 17px;

    padding: 17px;

    margin-bottom: 12px;

    border: 1px solid rgba(255,255,255,0.07);

    box-shadow:
        0 8px 24px rgba(0,0,0,0.22);
}

.trending-card:hover {
    border-color: rgba(255,49,93,0.60);
}

.rank {
    color: #ff3d6b;
    font-size: 11px;
    font-weight: 850;
    letter-spacing: 1.5px;
}

.movie-name {
    color: #ffffff;
    font-size: 16px;
    font-weight: 800;
    margin-top: 8px;
}

.movie-meta {
    color: #858ba0;
    font-size: 12px;
    margin-top: 7px;
}

.badge {
    display: inline-block;

    margin-top: 10px;

    padding: 5px 9px;

    border-radius: 20px;

    background: rgba(245,189,69,0.12);

    color: #ffc94d;

    font-size: 11px;
    font-weight: 750;
}


/* =========================================================
   INSIGHT CARD
   ========================================================= */

.insight {
    padding: 20px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            rgba(255,49,93,0.10),
            rgba(168,85,247,0.10)
        );

    border: 1px solid rgba(255,255,255,0.07);

    color: #c7cad6;

    line-height: 1.6;

    margin-top: 15px;
}


/* =========================================================
   DARK TABLE
   ========================================================= */

.dark-table {
    width: 100%;
    border-collapse: collapse;

    background: #101222;

    border-radius: 15px;

    overflow: hidden;

    font-size: 13px;
}

.dark-table th {
    background: #181b31;

    color: #ff6686;

    padding: 13px;

    text-align: left;

    border-bottom: 1px solid #292d46;
}

.dark-table td {
    padding: 12px;

    color: #d8d9e2;

    border-bottom: 1px solid #202338;
}

.dark-table tr:hover {
    background: #171a2e;
}


/* =========================================================
   SEARCH
   ========================================================= */

div[data-testid="stTextInput"] input {
    background: #111324;
    color: white;
    border: 1px solid #30344d;
}

div[data-testid="stNumberInput"] input {
    background: #111324;
    color: white;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;

    color: #5f6477;

    padding: 40px 0 20px;

    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

try:

    df = pd.read_csv("data/film_bersih.csv")

except FileNotFoundError:

    st.error(
        "File data/film_bersih.csv tidak ditemukan."
    )

    st.stop()


# ============================================================
# DATA CLEANING TAMBAHAN
# ============================================================

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

df = df.dropna(
    subset=[
        "Tahun Rilis",
        "Rating",
        "Jumlah Vote",
        "Popularity"
    ]
)

df["Tahun Rilis"] = df[
    "Tahun Rilis"
].astype(int)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    "## 🎬 MOVIE NIGHT"
)

st.sidebar.markdown(
    "### 🎛️ Filter Dashboard"
)

st.sidebar.markdown("---")


# Tahun

tahun_min = int(
    df["Tahun Rilis"].min()
)

tahun_max = int(
    df["Tahun Rilis"].max()
)

tahun_range = st.sidebar.slider(
    "📅 Tahun Rilis",
    min_value=tahun_min,
    max_value=tahun_max,
    value=(tahun_min, tahun_max)
)


# Rating

rating_min = st.sidebar.slider(
    "⭐ Rating Minimum",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)


# Vote

vote_min = st.sidebar.number_input(
    "👥 Jumlah Vote Minimum",
    min_value=0,
    max_value=int(
        df["Jumlah Vote"].max()
    ),
    value=50,
    step=100
)


st.sidebar.markdown("---")


st.sidebar.markdown(
    "### 🍿 Tentang Dashboard"
)

st.sidebar.write(
    "Dashboard ini menganalisis film "
    "berdasarkan rating, popularitas, "
    "jumlah vote, tahun rilis, dan bahasa."
)

st.sidebar.markdown(
    "---"
)

st.sidebar.caption(
    "🎬 Sumber data: TMDB"
)


# ============================================================
# FILTER DATA
# ============================================================

data = df[
    (df["Tahun Rilis"] >= tahun_range[0])
    &
    (df["Tahun Rilis"] <= tahun_range[1])
    &
    (df["Rating"] >= rating_min)
    &
    (df["Jumlah Vote"] >= vote_min)
].copy()


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="hero">'
    '<div class="hero-label">🎞️ MOVIE STATISTICS</div>'
    '<div class="hero-title">Dashboard Analisis Film Populer</div>'
    '<div class="hero-description">'
    'Temukan tren, rating, popularitas, dan fakta menarik '
    'dari dunia perfilman.'
    '</div>'
    '<div class="hero-source">'
    '🎬 Data bersumber dari TMDB'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATA KOSONG
# ============================================================

if data.empty:

    st.warning(
        "Tidak ada film yang sesuai dengan filter yang dipilih."
    )

    st.stop()


# ============================================================
# KPI
# ============================================================

st.markdown(
    "## 📌 Ringkasan Statistik"
)


film_populer = data.loc[
    data["Popularity"].idxmax()
]


judul_populer = str(
    film_populer["Judul Film"]
)

if len(judul_populer) > 25:

    judul_populer = (
        judul_populer[:25]
        + "..."
    )


k1, k2, k3, k4 = st.columns(4)


with k1:

    st.markdown(
        f'<div class="kpi kpi-red">'
        f'<div class="kpi-icon">🎞️</div>'
        f'<div class="kpi-label">Jumlah Film</div>'
        f'<div class="kpi-value">'
        f'{len(data):,}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k2:

    st.markdown(
        f'<div class="kpi kpi-blue">'
        f'<div class="kpi-icon">⭐</div>'
        f'<div class="kpi-label">Rata-rata Rating</div>'
        f'<div class="kpi-value">'
        f'{data["Rating"].mean():.2f}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k3:

    st.markdown(
        f'<div class="kpi kpi-yellow">'
        f'<div class="kpi-icon">👥</div>'
        f'<div class="kpi-label">Rata-rata Vote</div>'
        f'<div class="kpi-value">'
        f'{data["Jumlah Vote"].mean():,.0f}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with k4:

    st.markdown(
        f'<div class="kpi kpi-purple">'
        f'<div class="kpi-icon">🔥</div>'
        f'<div class="kpi-label">Film Terpopuler</div>'
        f'<div class="kpi-value" '
        f'style="font-size:18px;">'
        f'{html.escape(judul_populer)}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MOVIE NIGHT SECTION
# ============================================================

st.markdown(
    "## 🍿 Movie Night"
)


chart_col, trend_col = st.columns(
    [2.15, 1]
)


# ============================================================
# TOP 10 POPULARITY
# ============================================================

with chart_col:

    st.markdown(
        "### 🔥 Top 10 Film Paling Populer"
    )

    top10 = (
        data
        .sort_values(
            "Popularity",
            ascending=False
        )
        .head(10)
        .copy()
    )

    top10["Judul Pendek"] = (
        top10["Judul Film"]
        .astype(str)
        .apply(
            lambda x:
            x[:24] + "..."
            if len(x) > 24
            else x
        )
    )

    top10 = top10.sort_values(
        "Popularity",
        ascending=True
    )


    fig = px.bar(
        top10,
        x="Popularity",
        y="Judul Pendek",
        orientation="h",
        text="Popularity"
    )


    fig.update_traces(
        marker_color="#ff315d",
        texttemplate="%{text:.1f}",
        textposition="outside",
        hovertemplate=(
            "<b>%{customdata[0]}</b>"
            "<br>Popularity: %{x:.2f}"
            "<br>Rating: %{customdata[1]:.2f}"
            "<extra></extra>"
        ),
        customdata=top10[
            [
                "Judul Film",
                "Rating"
            ]
        ]
    )


    fig.update_layout(
        height=440,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="#d9dbe5"
        ),

        margin=dict(
            l=10,
            r=35,
            t=10,
            b=20
        ),

        xaxis=dict(
            title="Popularity",
            gridcolor="rgba(255,255,255,0.08)",
            zeroline=False
        ),

        yaxis=dict(
            title="",
            gridcolor="rgba(0,0,0,0)"
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# ============================================================
# TRENDING NOW
# ============================================================

with trend_col:

    st.markdown(
        "### 🔥 Trending Now"
    )


    trending = (
        data
        .sort_values(
            "Popularity",
            ascending=False
        )
        .head(5)
    )


    for nomor, (_, film) in enumerate(
        trending.iterrows(),
        start=1
    ):

        judul = html.escape(
            str(film["Judul Film"])
        )

        st.markdown(
            f'<div class="trending-card">'
            f'<div class="rank">'
            f'#{nomor} • TRENDING 🔥'
            f'</div>'
            f'<div class="movie-name">'
            f'{judul}'
            f'</div>'
            f'<div class="movie-meta">'
            f'🎬 {film["Tahun Rilis"]}'
            f' &nbsp;•&nbsp; '
            f'👥 {film["Jumlah Vote"]:,} vote'
            f'</div>'
            f'<div class="badge">'
            f'⭐ {film["Rating"]:.1f}'
            f' &nbsp;•&nbsp; '
            f'🔥 {film["Popularity"]:.1f}'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )


# ============================================================
# INSIGHT
# ============================================================

st.markdown(
    '<div class="insight">'
    '🎬 <b>Movie Insight</b><br>'
    'Popularitas film tidak selalu berarti '
    'ratingnya paling tinggi. Gunakan analisis '
    'di bawah untuk melihat hubungan antara '
    'rating, popularity, dan jumlah vote.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FILM PER TAHUN
# ============================================================

st.markdown(
    "## 📅 Perkembangan Film Berdasarkan Tahun"
)


per_tahun = (
    data
    .groupby("Tahun Rilis")
    .size()
    .reset_index(
        name="Jumlah Film"
    )
)


fig_year = px.bar(
    per_tahun,
    x="Tahun Rilis",
    y="Jumlah Film"
)


fig_year.update_traces(
    marker_color="#8b5cf6",
    hovertemplate=(
        "Tahun: %{x}"
        "<br>Jumlah Film: %{y}"
        "<extra></extra>"
    )
)


fig_year.update_layout(
    height=380,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="#d9dbe5"
    ),

    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    ),

    xaxis=dict(
        title="Tahun Rilis",
        gridcolor="rgba(255,255,255,0.06)"
    ),

    yaxis=dict(
        title="Jumlah Film",
        gridcolor="rgba(255,255,255,0.08)"
    )
)


st.plotly_chart(
    fig_year,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)


# ============================================================
# RATING VS POPULARITY
# ============================================================

st.markdown(
    "## 📈 Rating vs Popularity"
)


fig_scatter = px.scatter(
    data,
    x="Rating",
    y="Popularity",
    hover_name="Judul Film",
    hover_data={
        "Rating": ":.2f",
        "Popularity": ":.2f",
        "Jumlah Vote": ":,",
        "Tahun Rilis": True
    }
)


fig_scatter.update_traces(
    marker=dict(
        size=8,
        color="#ff3d6b",
        opacity=0.70,
        line=dict(
            width=1,
            color="#ff9ab0"
        )
    )
)


fig_scatter.update_layout(
    height=450,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="#d9dbe5"
    ),

    margin=dict(
        l=30,
        r=30,
        t=20,
        b=30
    ),

    xaxis=dict(
        title="Rating",
        range=[0, 10],
        dtick=1,
        gridcolor="rgba(255,255,255,0.08)"
    ),

    yaxis=dict(
        title="Popularity",
        gridcolor="rgba(255,255,255,0.08)"
    )
)


st.plotly_chart(
    fig_scatter,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)


# ============================================================
# KORELASI
# ============================================================

korelasi_popularity = (
    data[
        ["Rating", "Popularity"]
    ]
    .corr()
    .iloc[0, 1]
)


korelasi_vote = (
    data[
        ["Rating", "Jumlah Vote"]
    ]
    .corr()
    .iloc[0, 1]
)


c1, c2 = st.columns(2)


with c1:

    st.markdown(
        f'<div class="kpi kpi-purple">'
        f'<div class="kpi-icon">📊</div>'
        f'<div class="kpi-label">'
        f'Korelasi Rating ↔ Popularity'
        f'</div>'
        f'<div class="kpi-value">'
        f'{korelasi_popularity:.3f}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        f'<div class="kpi kpi-blue">'
        f'<div class="kpi-icon">📊</div>'
        f'<div class="kpi-label">'
        f'Korelasi Rating ↔ Jumlah Vote'
        f'</div>'
        f'<div class="kpi-value">'
        f'{korelasi_vote:.3f}'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TOP RATING
# ============================================================

st.markdown(
    "## 🏆 Film dengan Rating Tertinggi"
)


top_rating = (
    data[
        data["Jumlah Vote"] >= 100
    ]
    .sort_values(
        "Rating",
        ascending=False
    )
    .head(10)
)


table_rows = ""

for _, film in top_rating.iterrows():

    title = html.escape(
        str(film["Judul Film"])
    )

    table_rows += (
        "<tr>"
        f"<td>{title}</td>"
        f"<td>{int(film['Tahun Rilis'])}</td>"
        f"<td>⭐ {film['Rating']:.3f}</td>"
        f"<td>{film['Jumlah Vote']:,}</td>"
        f"<td>{film['Popularity']:.2f}</td>"
        "</tr>"
    )


st.markdown(
    '<table class="dark-table">'
    '<thead>'
    '<tr>'
    '<th>Judul Film</th>'
    '<th>Tahun</th>'
    '<th>Rating</th>'
    '<th>Jumlah Vote</th>'
    '<th>Popularity</th>'
    '</tr>'
    '</thead>'
    '<tbody>'
    + table_rows +
    '</tbody>'
    '</table>',
    unsafe_allow_html=True
)


# ============================================================
# PENCARIAN FILM
# ============================================================

st.markdown(
    "## 🔎 Eksplorasi Film"
)


search = st.text_input(
    "Cari berdasarkan judul film",
    placeholder="Contoh: Spider-Man"
)


if search:

    data_search = data[
        data["Judul Film"]
        .astype(str)
        .str.contains(
            search,
            case=False,
            na=False
        )
    ].copy()

else:

    data_search = data.head(20).copy()


# ============================================================
# DARK SEARCH TABLE
# ============================================================

search_rows = ""

for _, film in data_search.iterrows():

    title = html.escape(
        str(film["Judul Film"])
    )

    genre = html.escape(
        str(film["Genre"])
    )

    language = html.escape(
        str(film["Bahasa"])
    )

    search_rows += (
        "<tr>"
        f"<td>{title}</td>"
        f"<td>{int(film['Tahun Rilis'])}</td>"
        f"<td>{genre}</td>"
        f"<td>⭐ {film['Rating']:.2f}</td>"
        f"<td>{film['Jumlah Vote']:,}</td>"
        f"<td>{film['Popularity']:.2f}</td>"
        f"<td>{language}</td>"
        "</tr>"
    )


st.markdown(
    '<table class="dark-table">'
    '<thead>'
    '<tr>'
    '<th>Judul Film</th>'
    '<th>Tahun</th>'
    '<th>Genre</th>'
    '<th>Rating</th>'
    '<th>Vote</th>'
    '<th>Popularity</th>'
    '<th>Bahasa</th>'
    '</tr>'
    '</thead>'
    '<tbody>'
    + search_rows +
    '</tbody>'
    '</table>',
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    '🎬 MOVIE NIGHT • DASHBOARD ANALISIS FILM POPULER'
    '<br>'
    'Statistical Film Analysis • TMDB Dataset'
    '</div>',
    unsafe_allow_html=True
)