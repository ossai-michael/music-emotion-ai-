# Project Working Log

## Project Title

**Heartbroken, Hopeful, or Happy?**  
An AI-Assisted Analysis of Themes in 2025’s Highest-Performing Songs

---

## Current Research Question

What themes, emotions, and value signals appear most often among 2025’s highest-performing songs across selected Billboard year-end charts?

---

## Working Purpose

This project explores the emotional and value-oriented narratives present in commercially successful music. The goal is not to prove what listeners believe or how songs affect listeners psychologically. Instead, the project examines the themes and messages carried by songs that achieved major chart success.

---

## Major Project Decisions and Rationales

### 1. Shift from current weekly charts to 2025 year-end charts

**Original idea:**  
Use current chart leaders from Apple Music or Billboard genre charts.

**Problem:**  
Weekly charts can be unstable. A weekly top 10 may reflect a recent album release, viral moment, seasonal event, or short-term spike. That makes it harder to discuss broader patterns in popular music.

**Decision:**  
Use Billboard 2025 year-end charts instead.

**Rationale:**  
Year-end charts better reflect sustained commercial performance across a longer tracking period. This makes the project better suited for analyzing themes associated with highly successful songs rather than songs that happened to be popular during a single week.

**Important limitation:**  
Year-end chart success still does not prove that listeners personally relate to, endorse, or internalize a song’s themes.

---

### 2. Shift from five genre charts to four genre charts plus a global benchmark

**Original idea:**  
Compare five genres, including Christian/Gospel.

**Problem:**  
Christian/Gospel was likely to produce predictable themes such as faith, hope, worship, and gratitude. That would make the comparison less surprising and less analytically rich.

**Intermediate idea:**  
Replace Christian/Gospel with Afrobeats.

**Problem:**  
The Afrobeats year-end data was less certain and could create sourcing or comparability issues.

**Decision:**  
Use four genre charts plus the Billboard Global 200 as a benchmark.

**Current comparison groups:**
- Rap
- R&B
- Country
- Rock & Alternative
- Global 200 benchmark

**Rationale:**  
The Global 200 is not a genre, so it will be treated as a benchmark rather than a fifth genre. This allows the project to compare genre-specific patterns against a broader global-popularity reference point.

---

### 3. Shift from “what are people digesting?” to “what themes are carried by successful songs?”

**Original framing:**  
Explore what themes people are digesting, relating to, or absorbing through popular music.

**Problem:**  
Chart data does not directly measure listener interpretation, emotional identification, belief, or psychological influence.

**Decision:**  
Use more careful language.

**Current framing:**  
This project analyzes the themes, emotions, and value signals present in high-performing songs. It does not claim to measure listener beliefs, mental health, or personal identification.

**Rationale:**  
This keeps the project honest and defensible while still allowing meaningful cultural analysis.

---

### 4. Add a message/value layer to the taxonomy

**Original classification fields:**
- primary_theme
- secondary_theme
- primary_emotion
- emotional_valence
- agency
- relationship_focus
- confidence_score
- human_review_needed
- rationale

**Problem:**  
Emotional valence alone cannot answer whether songs carry constructive or concerning messages. A sad song may be healing and reflective. An upbeat song may still glorify excess, revenge, or unhealthy coping.

**Decision:**  
Add:
- message_orientation
- message_score
- value_signal

**Rationale:**  
These fields allow the analysis to distinguish emotional tone from value orientation. This supports a more thoughtful dashboard and interpretation.

---

## Taxonomy Rationale

### Theme

The theme field identifies what the song is mainly about. The categories are designed to cover major narratives common in commercially successful music while remaining small enough for Tableau visualization.

Current theme categories:
- Romantic Love & Devotion
- Heartbreak & Loss
- Desire & Intimacy
- Celebration & Pleasure
- Status/Wealth/Success
- Confidence/Boldness/Pride
- Identity & Self-Discovery
- Conflict/Revenge/Defiance
- Pain/Numbness/Escapism
- Hope/Healing/Resilience
- Social Struggle/Survival
- Other

### Emotion

The emotion field captures the dominant emotional feel of the song. It is separate from the message or moral orientation.

Current emotion categories:
- Joy
- Sadness
- Longing
- Anger
- Confidence
- Hope
- Anxiety
- Desire
- Numbness
- Mixed

### Emotional Valence

Emotional valence measures whether the song feels emotionally positive, negative, neutral, or mixed.

Scale:
- -2 = strongly negative
- -1 = somewhat negative
- 0 = mixed or neutral
- 1 = somewhat positive
- 2 = strongly positive

### Message Orientation

Message orientation classifies the apparent value direction of the song’s narrative.

Categories:
- Constructive/Encouraging
- Ambiguous/Mixed
- Pleasure/Escapist
- Potentially Concerning
- Critical/Reflective

This field is central to the project because it helps avoid the mistake of treating all sad songs as harmful or all upbeat songs as positive.

### Message Score

Message score gives a numeric version of message orientation for visualization.

Scale:
- -2 = strongly concerning
- -1 = somewhat concerning, escapist, or self-focused
- 0 = ambiguous, mixed, descriptive, or critical/reflective
- 1 = somewhat constructive or encouraging
- 2 = strongly constructive or encouraging

### Value Signal

Value signal captures the dominant value, behavior, or worldview emphasized by the song.

Categories:
- Love/Commitment
- Hope/Resilience
- Self-Worth
- Growth/Accountability
- Joy/Celebration
- Freedom/Escape
- Status/Materialism
- Desire/Pleasure
- Revenge/Conflict
- Numbness/Avoidance
- Confusion/Instability
- Survival/Struggle
- Other

---

## Methodology Draft

The project began as a small AI-assisted music analytics project designed to combine music, structured data, and visualization. The original version planned to collect songs from current genre charts and classify them by theme and emotional tone.

During project development, the methodology shifted toward Billboard 2025 year-end charts because year-end rankings better reflect sustained commercial success than a single weekly chart. This made the project more stable and defensible.

The project also shifted from a simple emotional analysis to a broader analysis of themes, emotions, and value signals. This change was made because emotional tone alone does not capture whether a song’s message is constructive, escapist, reflective, or potentially concerning.

The final workflow is:

1. Build a structured dataset of selected Billboard 2025 year-end chart entries.
2. Identify duplicate songs that appear across multiple charts.
3. Create a unique-song classification file so each song is classified once.
4. Use Claude to classify each unique song against a fixed taxonomy.
5. Validate a sample of classifications manually.
6. Merge classifications back onto the full chart-entry dataset.
7. Build Tableau visualizations showing theme distribution, emotional tone, message orientation, and value signals across comparison groups.
8. Document limitations and interpretation choices.

---

## Current Limitations to Include Later

- Billboard chart success does not prove listener agreement, identification, or psychological impact.
- Year-end rankings reflect a chart tracking period, not necessarily songs released during the calendar year.
- The Global 200 is a benchmark, not a genre.
- Song classification is interpretive and may vary depending on context.
- Claude may misclassify ambiguous songs, irony, metaphor, or songs with limited publicly available context.
- The project does not reproduce or store full copyrighted lyrics.
- The sample includes top 10 songs from selected charts, not every successful song of 2025.
- Message orientation is a structured interpretation, not an objective moral verdict.

---

## Notes for Storytelling Later

Potential dashboard/story angles:

1. **Mood vs Message**
   - Compare emotional_valence against message_score.
   - Look for songs that are emotionally negative but constructively reflective.
   - Look for songs that are emotionally positive but potentially concerning.

2. **What Values Dominate?**
   - Visualize value_signal across charts.
   - Compare Love/Commitment, Status/Materialism, Desire/Pleasure, Hope/Resilience, and Numbness/Avoidance.

3. **Genre Comparison**
   - Compare whether Rap, R&B, Country, and Rock & Alternative emphasize different dominant narratives.
   - Use Global 200 as a benchmark for the broader popular-music landscape.

4. **Constructive vs Concerning Narratives**
   - Use message_orientation and message_score to avoid simplistic “happy vs sad” analysis.
   - Emphasize that the analysis is interpretive and exploratory.

---

## Running Change Log

### Change 1
Moved from current weekly chart snapshot to 2025 year-end chart analysis.

### Change 2
Replaced Christian/Gospel with Global 200 benchmark to avoid predictable thematic results and create a stronger comparison point.

### Change 3
Changed the research framing from listener psychology to song-level thematic and message analysis.

### Change 4
Expanded the taxonomy to include identity crisis, confusion, boldness, pride, numbness, escapism, value signals, and message orientation.

### Change 5
Added message_score so Tableau can compare emotional tone against constructive/concerning message orientation.


### Change 6
Added lyric-level evidence as an allowed basis for classification, while deciding not to store, reproduce, or publish full lyrics.

**Rationale:**  
Lyrics are often the strongest evidence for identifying a song’s emotional themes, message orientation, and value signals. However, full lyrics are copyrighted works, and publicly available lyrics are not automatically free to copy into a public dataset or GitHub repository.

**Decision:**  
The project will allow Claude to use lyric-level understanding, public lyric sources, annotations, reviews, artist commentary, and widely known interpretation to inform classifications. However, the final project will not store or reproduce full lyrics. The dataset will contain only derived classifications, short paraphrased rationales, and an `evidence_basis` field.

**Impact on methodology:**  
The classification output now includes `evidence_basis` with four allowed values:

- Lyrics
- Lyrics + Context
- Context Only
- Limited Evidence

This improves transparency by showing whether each classification relied mainly on lyric-level understanding, broader public context, or limited available evidence.