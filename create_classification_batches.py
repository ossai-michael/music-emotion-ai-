from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
BATCH_DIR = DATA_DIR / "classification_batches"

INPUT_FILE = DATA_DIR / "unique_songs_for_classification.csv"

BATCH_SIZE = 5

BATCH_DIR.mkdir(exist_ok=True)

songs = pd.read_csv(INPUT_FILE, keep_default_na=False)

required_columns = [
    "unique_song_id",
    "song_key",
    "song_title",
    "artist",
]

missing_columns = [
    col for col in required_columns
    if col not in songs.columns
]

if missing_columns:
    raise ValueError(
        f"Missing columns in {INPUT_FILE}: {missing_columns}"
    )

songs = songs[required_columns].copy()

for start in range(0, len(songs), BATCH_SIZE):
    batch = songs.iloc[start:start + BATCH_SIZE]
    batch_number = (start // BATCH_SIZE) + 1

    output_file = (
        BATCH_DIR
        / f"classification_batch_{batch_number:02}.csv"
    )

    batch.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )

    print(
        f"Created {output_file} "
        f"with {len(batch)} songs"
    )

print()
print(f"Total unique songs: {len(songs)}")
print(f"Batch size: {BATCH_SIZE}")
print(f"Batches saved in: {BATCH_DIR}")