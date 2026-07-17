from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_FILE = DATA_DIR / "classified_unique_songs.csv"
OUTPUT_FILE = DATA_DIR / "validation_sample.csv"

SAMPLE_SIZE = 10
RANDOM_SEED = 42

classified = pd.read_csv(INPUT_FILE, keep_default_na=False)

validation_sample = (
    classified
    .sample(
        n=min(SAMPLE_SIZE, len(classified)),
        random_state=RANDOM_SEED
    )
    .sort_values("unique_song_id")
    .copy()
)

validation_sample["human_theme_assessment"] = ""
validation_sample["human_message_assessment"] = ""
validation_sample["human_notes"] = ""
validation_sample["correction_needed"] = ""

columns_to_keep = [
    "unique_song_id",
    "song_title",
    "artist",
    "primary_theme",
    "secondary_theme",
    "primary_emotion",
    "emotional_valence",
    "message_orientation",
    "message_score",
    "value_signal",
    "evidence_basis",
    "confidence_score",
    "human_review_needed",
    "rationale",
    "human_theme_assessment",
    "human_message_assessment",
    "human_notes",
    "correction_needed",
]

validation_sample = validation_sample[columns_to_keep]

validation_sample.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

print("Validation sample created.")
print(f"Rows selected: {len(validation_sample)}")
print(f"Saved to: {OUTPUT_FILE}")
print()
print(validation_sample[["unique_song_id", "song_title", "artist"]])