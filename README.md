# Heartbroken, Hopeful, or Happy?

## An AI-Assisted Analysis of Themes, Emotions, and Messages in 2025 Billboard Year-End Genre Chart Leaders

This project analyzes the dominant themes, emotions, message orientations, and value signals in 50 high-performing songs across five Billboard 2025 year-end genre chart groups:

- Rap
- R&B
- Country
- Rock & Alternative
- Afrobeats

The goal was not to determine whether songs are “good” or “bad,” or to measure listener psychology. Instead, the project asks:

> What themes, emotions, and values appear most often in commercially successful songs across selected genres?

## Tableau Story

[View the Tableau Story here](https://public.tableau.com/app/profile/michael.ossai/viz/DataProject_17845991368060/Story1)

## Project Summary

Across the 50 chart entries, love, desire, and heartbreak emerge as the project’s central pattern.

At the primary theme level, **Love & Attachment**, **Sex & Desire**, and **Heartbreak & Longing** account for **60%** of all chart entries. At the secondary theme level, those same categories account for **48%**. In total, **74%** of entries contain love, sex/desire, or heartbreak as either a primary or secondary theme.

The project also finds that emotional tone and message score do not always move together. Some genres appear emotionally positive while carrying lower message scores, while others are emotionally darker but more reflective or constructive.

## Key Findings

### 1. Afrobeats had the most positive emotional tone

Afrobeats was the only genre in this sample where all 10 chart entries were classified as emotionally positive. In this project, “emotionally positive” means the dominant tone leaned upbeat, joyful, confident, hopeful, or celebratory. “Negative” does not mean the song is bad; it means the dominant tone leaned sad, anxious, angry, numb, painful, or unresolved.

### 2. Love, sex/desire, and heartbreak dominate the theme map

The most common primary themes were relationship-centered. Love, sex/desire, and heartbreak accounted for 60% of all primary themes and 48% of all secondary themes.

This suggests that relationship dynamics are not only the headline of many charting songs, but also a recurring subplot even when the song’s main subject is status, conflict, identity, or escape.

### 3. Themes and values are connected, but not identical

Themes describe what the songs are about. Value signals describe the behavior, worldview, coping pattern, or emotional logic the song appears to normalize, chase, critique, or wrestle with.

Across genres, relationships remain central, but they lead in different directions — toward connection, pleasure and escape, status and ego, conflict, or emotional instability.

### 4. Desire and longing lead the emotional vocabulary

“Primary emotion” refers to the dominant feeling expressed through the song’s lyrics, narrative, and speaker/persona. It is not an audio analysis of melody, tempo, production, or vocal performance.

Across all 50 entries, desire and longing were the most common primary emotions.

### 5. Positive emotional tone does not always mean constructive messaging

The scatterplot comparing emotional valence and message score shows that the most emotionally positive genres are not always the most constructive. Afrobeats and Rap scored high on emotional tone but lower on message score, while Rock & Alternative had the highest average message score despite a darker emotional tone.

## Methodology

I built a dataset of 50 chart entries from five Billboard 2025 year-end genre chart groups, with 10 entries per genre.

Each song was classified using an AI-assisted thematic coding process. The classification focused on publicly known song themes, lyrical narratives, and the apparent speaker/persona of each song. Lyrics were not reproduced in the dataset or repository.

Each entry was labeled across several fields, including:

- `primary_theme`
- `secondary_theme`
- `primary_emotion`
- `emotional_valence`
- `message_orientation`
- `message_score`
- `value_signal`
- `confidence_score`
- `human_review_needed`

I then manually reviewed the classifications for consistency and revised the taxonomy to better distinguish between similar concepts such as reflection vs. growth, suffering vs. resilience, and confidence vs. ego.

## Taxonomy Notes

### Emotional Valence

Emotional valence captures the dominant emotional tone:

- `-2`: strongly negative
- `-1`: somewhat negative
- `0`: mixed or neutral
- `1`: somewhat positive
- `2`: strongly positive

### Message Score

Message score captures whether the song’s apparent message is constructive, mixed, escapist, or concerning:

- `-2`: strongly concerning
- `-1`: somewhat concerning, escapist, unstable, or unresolved
- `0`: mixed, descriptive, reflective, or ambiguous
- `1`: somewhat constructive
- `2`: strongly constructive

### Value Signal

Value signal captures the main value, behavior, coping pattern, or worldview the song appears to normalize, chase, critique, or wrestle with.

Examples include:

- Connection
- Resilience
- Growth
- Self-Worth
- Joy/Pleasure
- Escape
- Status
- Ego/Power
- Revenge
- Avoidance
- Instability
- Survival

## Limitations

This project is interpretive. Song classification involves judgment, especially when songs use irony, persona, metaphor, genre conventions, or emotionally mixed narratives.

The dataset includes 50 chart entries, not every popular song from 2025. Each genre contributes 10 entries, so the project is best understood as a focused exploratory analysis rather than a complete study of popular music.

The analysis does not claim to measure listener beliefs, artist intent, social impact, or the psychological effects of music. It only classifies apparent themes and messages based on song narratives and public context.

## Repository Structure

```text
data/
  song_list.csv
  classified_unique_songs.csv
  analysis_dataset.csv

documentation/
  methodology.md
  working_log.md

prompts/
  classification_prompt.txt

scripts/
  build_year_end_dataset.py
  prepare_unique_songs.py
  create_classification_batches.py
  merge_classified_batches.py
  rebuild_analysis_dataset.py