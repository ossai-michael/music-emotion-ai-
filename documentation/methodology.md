# Methodology Draft

## Project Overview

This project analyzes the themes, emotions, and value signals present in selected high-performing songs from the Billboard 2025 year-end charts. The analysis uses a structured AI-assisted classification workflow and visualizes the results in Tableau.

## Research Question

What themes, emotions, and value signals appear most often among 2025’s highest-performing songs across selected Billboard year-end charts?

## Dataset

The dataset includes the top 10 songs from selected Billboard 2025 year-end charts. The comparison groups are Rap, R&B, Country, Rock & Alternative, and the Billboard Global 200.

The Global 200 is treated as a benchmark rather than a genre because it represents a broad global chart, not a genre-specific ranking.

## Classification Approach

Each unique song is classified once, even if it appears on more than one chart. The classification is then merged back onto all chart appearances.

The classification framework includes:

- Primary theme
- Secondary theme
- Primary emotion
- Emotional valence
- Agency
- Relationship focus
- Message orientation
- Message score
- Value signal
- Confidence score
- Human review flag
- One-sentence rationale

## Why Message Orientation Was Added

The project originally focused on theme and emotional tone. However, emotional valence alone cannot answer whether a song carries a constructive, escapist, reflective, or potentially concerning message.

For example, a song can be emotionally sad but still constructive if it emphasizes healing or resilience. A song can also sound joyful while centering excess, revenge, or destructive coping. For this reason, the project separates emotional tone from message orientation.

## Use of Claude

Claude is used to classify songs against a fixed taxonomy. The taxonomy was designed before classification and tested before being applied to the full dataset.

Claude is instructed not to quote lyrics and not to reproduce copyrighted lyric text. The model uses publicly available knowledge about the song, its general themes, artist context, and widely known interpretation.

## Human Validation

A sample of classifications will be manually reviewed. The human review will assess whether the selected themes, emotions, message orientation, and value signals are reasonable.

Any obvious classification errors will be corrected and documented.

## Limitations

This project does not measure listener beliefs, listener psychology, or whether listeners personally identify with a song’s message.

Chart success does not prove that a theme is culturally endorsed. It only shows that the song achieved high commercial performance.

The analysis is exploratory and interpretive. Song meanings can be ambiguous, metaphorical, ironic, or context-dependent.

The Global 200 is a benchmark rather than a genre, so comparisons involving it should be interpreted carefully.

The project does not store or reproduce full copyrighted lyrics.
