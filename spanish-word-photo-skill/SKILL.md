---
name: spanish-word-photo-skill
description: "Extract underlined Spanish words from a photo and generate a Quizlet-formatted list with English translations. Upload a photo → Claude extracts underlined Spanish words → provides English equivalents → output in tab-separated format (Spanish\tEnglish) ready to copy-paste into Quizlet."
---

# Spanish Word Photo Extractor

Extract Spanish words from photos and create Quizlet study lists automatically.

## Quick Start

1. Invoke the skill with `/spanish-word-photo-skill` (or just upload a photo containing underlined Spanish words)
2. Upload a photo of Spanish vocabulary (underlined words)
3. Receive a Quizlet-formatted list (tab-separated Spanish and English)
4. Copy the list directly into Quizlet

## How It Works

The skill:
- **Analyzes your photo** to identify text using Claude's vision capabilities
- **Extracts underlined words** (those marked with underlines in the photo)
- **Translates to English** for each Spanish word
- **Formats for Quizlet**: One word pair per line, tab-separated
  - Format: `Spanish\tEnglish`
  - Example: `gato\tcat`

## Usage

### Basic Usage
Simply upload a photo containing underlined Spanish words, and the skill will process it automatically.

### Manual Invocation
```
/spanish-word-photo-skill
[Upload photo]
```

## Output Format

The skill returns tab-separated values (TSV) that you can directly import into Quizlet:

```
palabra\tword
gato\tcat
casa\thouse
perro\tdog
```

### To import into Quizlet:
1. Copy the entire list
2. Go to Quizlet.com → Create a new study set
3. Click "Import"
4. Paste the list
5. Select tab-separated format
6. Done!

## Supported Input

- **Photo formats**: JPG, PNG, GIF, WebP
- **Text in photo**: Clear, readable Spanish words with underlines
- **Language**: Spanish (en, es, other languages can be provided)

## Limitations

- Works best with clearly legible photos
- Underlines must be visually distinguishable
- Prefers digital text over handwritten text
- May require multiple passes for complex layouts

## Examples

### Input Photo
```
English vocabulary list:
- el gato
- la casa  
- el perro
```

### Output (Quizlet Format)
```
gato	cat
casa	house
perro	dog
```

## Tips

- Photograph with good lighting and minimal shadows
- Frame the photo to include all relevant words
- Ensure underlines are clearly visible
- The skill ignores non-underlined words automatically
