from pathlib import Path

import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "song_list.csv"

DATA_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# CHART INFORMATION
# --------------------------------------------------

CHART_YEAR = 2025

TRACKING_PERIOD = (
    "2024-10-26 to 2025-10-18"
)

SOURCE_URLS = {
    "Rap": (
        "https://www.billboard.com/charts/"
        "year-end/2025/hot-rap-songs/"
    ),
    "R&B": (
        "https://www.billboard.com/charts/"
        "year-end/2025/hot-r-and-b-songs/"
    ),
    "Country": (
        "https://www.billboard.com/charts/"
        "year-end/2025/hot-country-songs/"
    ),
    "Rock & Alternative": (
        "https://www.billboard.com/charts/"
        "year-end/2025/hot-rock-alternative-songs/"
    ),
    "Global 200": (
        "https://www.billboard.com/charts/"
        "year-end/2025/billboard-global-200/"
    ),
}


# --------------------------------------------------
# VERIFIED TOP-10 CHART DATA
# --------------------------------------------------

CHART_DATA = {

    "Rap": [
        ("Luther", "Kendrick Lamar & SZA"),
        (
            "TV Off",
            "Kendrick Lamar featuring Lefty Gunplay"
        ),
        ("Not Like Us", "Kendrick Lamar"),
        ("Squabble Up", "Kendrick Lamar"),
        ("Nokia", "Drake"),
        (
            "All the Way",
            "BigXthaPlug featuring Bailey Zimmerman"
        ),
        (
            "Sticky",
            "Tyler, the Creator featuring "
            "GloRilla, Sexyy Red & Lil Wayne"
        ),
        (
            "Whatchu Kno About Me",
            "GloRilla & Sexyy Red"
        ),
        (
            "Peekaboo",
            "Kendrick Lamar featuring AzChike"
        ),
        ("Denial Is a River", "Doechii"),
    ],

    "R&B": [
        (
            "Timeless",
            "The Weeknd & Playboi Carti"
        ),
        ("Mutt", "Leon Thomas"),
        (
            "30 for 30",
            "SZA with Kendrick Lamar"
        ),
        ("Cry for Me", "The Weeknd"),
        (
            "Burning Blue",
            "Mariah the Scientist"
        ),
        (
            "Somebody Loves Me",
            "PARTYNEXTDOOR, Drake & Cash Cobain"
        ),
        (
            "Like Him",
            "Tyler, the Creator featuring Lola Young"
        ),
        (
            "Heart of a Woman",
            "Summer Walker"
        ),
        ("Residuals", "Chris Brown"),
        ("Folded", "Kehlani"),
    ],

    "Country": [
        (
            "A Bar Song (Tipsy)",
            "Shaboozey"
        ),
        ("Love Somebody", "Morgan Wallen"),
        ("I'm the Problem", "Morgan Wallen"),
        (
            "I Had Some Help",
            "Post Malone featuring Morgan Wallen"
        ),
        ("Just in Case", "Morgan Wallen"),
        ("Good News", "Shaboozey"),
        (
            "What I Want",
            "Morgan Wallen featuring Tate McRae"
        ),
        (
            "All the Way",
            "BigXthaPlug featuring Bailey Zimmerman"
        ),
        ("I Got Better", "Morgan Wallen"),
        ("I Never Lie", "Zach Top"),
    ],

    "Rock & Alternative": [
        (
            "Birds of a Feather",
            "Billie Eilish"
        ),
        ("Too Sweet", "Hozier"),
        ("Stargazing", "Myles Smith"),
        ("Wildflower", "Billie Eilish"),
        ("Messy", "Lola Young"),
        (
            "No One Noticed",
            "The Marías"
        ),
        ("Sailor Song", "Gigi Perez"),
        ("Liar", "Jelly Roll"),
        ("Undressed", "sombr"),
        ("Back to Friends", "sombr"),
    ],

    "Global 200": [
        ("APT.", "ROSÉ & Bruno Mars"),
        (
            "Die with a Smile",
            "Lady Gaga & Bruno Mars"
        ),
        (
            "Birds of a Feather",
            "Billie Eilish"
        ),
        ("Ordinary", "Alex Warren"),
        (
            "Beautiful Things",
            "Benson Boone"
        ),
        ("Lose Control", "Teddy Swims"),
        (
            "That's So True",
            "Gracie Abrams"
        ),
        (
            "Luther",
            "Kendrick Lamar & SZA"
        ),
        ("Espresso", "Sabrina Carpenter"),
        (
            "Golden",
            "HUNTR/X: EJAE, Audrey Nuna & REI AMI"
        ),
    ],
}


# --------------------------------------------------
# BUILD DATASET
# --------------------------------------------------

rows = []

song_id = 1

for comparison_group, songs in CHART_DATA.items():

    if comparison_group == "Global 200":
        group_type = "Global benchmark"
        market_scope = "Global"
        chart_name = "Billboard Global 200"

    else:
        group_type = "Genre"
        market_scope = "United States"
        chart_name = (
            f"Billboard Hot "
            f"{comparison_group} Songs"
        )

        if comparison_group == "Rock & Alternative":
            chart_name = (
                "Billboard Hot Rock "
                "& Alternative Songs"
            )

    for rank, song in enumerate(
        songs,
        start=1
    ):

        song_title, artist = song

        rows.append(
            {
                "song_id": song_id,
                "comparison_group": comparison_group,
                "group_type": group_type,
                "market_scope": market_scope,
                "year_end_rank": rank,
                "song_title": song_title,
                "artist": artist,
                "chart_name": chart_name,
                "chart_year": CHART_YEAR,
                "tracking_period": TRACKING_PERIOD,
                "source_url": (
                    SOURCE_URLS[
                        comparison_group
                    ]
                ),
            }
        )

        song_id += 1


# --------------------------------------------------
# CREATE DATAFRAME
# --------------------------------------------------

song_list = pd.DataFrame(
    rows
)


# --------------------------------------------------
# VALIDATE DATA
# --------------------------------------------------

assert len(song_list) == 50

assert (
    song_list[
        "comparison_group"
    ]
    .value_counts()
    .eq(10)
    .all()
)

assert (
    song_list[
        "year_end_rank"
    ]
    .between(1, 10)
    .all()
)

assert not (
    song_list[
        [
            "song_title",
            "artist",
            "comparison_group",
        ]
    ]
    .isna()
    .any()
    .any()
)


# --------------------------------------------------
# SAVE CSV
# --------------------------------------------------

song_list.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

print()
print(
    "Dataset created successfully."
)

print(
    f"Total chart entries: "
    f"{len(song_list)}"
)

print()

print(
    "Entries by comparison group:"
)

print(
    song_list[
        "comparison_group"
    ]
    .value_counts()
)

print()

print(
    f"Saved to:\n{OUTPUT_FILE}"
)