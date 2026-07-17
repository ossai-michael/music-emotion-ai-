from pathlib import Path

import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_FILE = DATA_DIR / "song_list.csv"
UNIQUE_OUTPUT_FILE = DATA_DIR / "unique_songs_for_classification.csv"
DUPLICATES_OUTPUT_FILE = DATA_DIR / "duplicate_chart_entries.csv"


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

song_list = pd.read_csv(INPUT_FILE)


# --------------------------------------------------
# CREATE A SIMPLE SONG KEY
# --------------------------------------------------
# This helps us identify the same song across charts.
# Example:
# Luther + Kendrick Lamar & SZA
# should only be classified once, even if it appears
# on Rap and Global 200.

song_list["song_key"] = (
    song_list["song_title"].str.strip().str.lower()
    + " || "
    + song_list["artist"].str.strip().str.lower()
)


# --------------------------------------------------
# CREATE UNIQUE SONG LIST
# --------------------------------------------------

unique_songs = (
    song_list
    .drop_duplicates(subset=["song_key"])
    .copy()
)


# Add a new unique song ID
unique_songs.insert(
    0,
    "unique_song_id",
    range(1, len(unique_songs) + 1)
)


# Keep only the columns Claude needs for classification
unique_songs_for_classification = unique_songs[
    [
        "unique_song_id",
        "song_key",
        "song_title",
        "artist",
    ]
].copy()


# Add chart-appearance context so Claude knows where the song appeared
chart_context = (
    song_list
    .assign(
        chart_appearance=(
            song_list["comparison_group"]
            + " #"
            + song_list["year_end_rank"].astype(str)
        )
    )
    .groupby("song_key", as_index=False)["chart_appearance"]
    .agg("; ".join)
    .rename(columns={"chart_appearance": "chart_appearances"})
)

# --------------------------------------------------
# FIND DUPLICATE CHART ENTRIES
# --------------------------------------------------

duplicate_chart_entries = (
    song_list[
        song_list.duplicated(
            subset=["song_key"],
            keep=False
        )
    ]
    .sort_values(
        ["song_key", "comparison_group"]
    )
)


# --------------------------------------------------
# SAVE FILES
# --------------------------------------------------

unique_songs_for_classification.to_csv(
    UNIQUE_OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

duplicate_chart_entries.to_csv(
    DUPLICATES_OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)


# --------------------------------------------------
# PRINT SUMMARY
# --------------------------------------------------

print()
print("Unique-song preparation complete.")
print(f"Total chart entries: {len(song_list)}")
print(f"Unique songs to classify: {len(unique_songs_for_classification)}")
print(f"Duplicate chart entries: {len(duplicate_chart_entries)}")

print()
print(f"Saved unique songs to:\n{UNIQUE_OUTPUT_FILE}")

print()
print(f"Saved duplicate chart entries to:\n{DUPLICATES_OUTPUT_FILE}")