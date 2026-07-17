from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

song_list = pd.read_csv(DATA_DIR / "song_list.csv", keep_default_na=False)
unique_songs = pd.read_csv(DATA_DIR / "unique_songs_for_classification.csv", keep_default_na=False)
classified = pd.read_csv(DATA_DIR / "classified_unique_songs.csv", keep_default_na=False)

# Recreate song key in full chart dataset
song_list["song_key"] = (
    song_list["song_title"].str.strip().str.lower()
    + " || "
    + song_list["artist"].str.strip().str.lower()
)

# Attach song_key to corrected classifications
classified_with_key = classified.merge(
    unique_songs[["unique_song_id", "song_key"]],
    on="unique_song_id",
    how="left"
)

analysis_dataset = song_list.merge(
    classified_with_key,
    on="song_key",
    how="left",
    suffixes=("", "_classified")
)

output_file = DATA_DIR / "analysis_dataset.csv"

analysis_dataset.to_csv(
    output_file,
    index=False,
    encoding="utf-8"
)

print("Final analysis dataset rebuilt.")
print(f"Rows: {len(analysis_dataset)}")
print(f"Saved to: {output_file}")

missing = analysis_dataset[analysis_dataset["primary_theme"].isna()]
print(f"Rows missing classifications: {len(missing)}")