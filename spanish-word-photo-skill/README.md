# Spanish Word Photo Skill

A Claude Code skill that extracts underlined Spanish words from photos and generates Quizlet-compatible study lists with English translations.

## Quick Start

### Easiest Way: Tell Claude

Simply say to Claude:
> "Extract Spanish words from this photo" 

Then upload your photo, and Claude will handle the rest.

### What It Does

1. **Analyzes your photo** using Claude's vision capabilities
2. **Identifies underlined Spanish words** in the image
3. **Provides English translations** for each word
4. **Formats for Quizlet** (tab-separated values)

### Example

**Input**: A photo of a vocabulary list
```
Vocabulario:
- gato (underlined in photo)
- casa (underlined in photo)
- perro (underlined in photo)
```

**Output**: Quizlet-ready format
```
gato	cat
casa	house
perro	dog
```

## Installation & Setup

### Prerequisites
- Python 3.10+
- Claude Code environment
- Internet connection (for Claude API)

### Files Included

- `SKILL.md` - Detailed skill documentation
- `IMPLEMENTATION.md` - Comprehensive usage guide with examples
- `extract_spanish_words.py` - Python implementation using Claude vision
- `extract_words.sh` - Shell wrapper for command-line use
- `README.md` - This file

## Usage

### Method 1: Direct in Claude (Recommended)

In Claude Code, when you want to extract Spanish words:

1. Upload a photo containing underlined Spanish vocabulary
2. Say: "Extract the Spanish words from this photo"
3. Receive Quizlet-formatted output

### Method 2: Command Line

```bash
cd spanish-word-photo-skill
./extract_words.sh /path/to/image.jpg
```

Output will be tab-separated values ready to paste into Quizlet.

### Method 3: Python Direct

```bash
python3 spanish-word-photo-skill/extract_spanish_words.py /path/to/image.jpg
```

## Importing to Quizlet

### Steps:

1. **Copy the output** (tab-separated Spanish and English pairs)
2. **Go to Quizlet.com**
3. **Click "Create" → "Study Set"**
4. **Click "Import"** or select the text editor
5. **Paste your list**
6. **Select format**: "Tab or space separated"
7. **Click "Import"** and save

That's it! Your vocabulary list is ready to study.

## Features

✨ **Key Features:**
- Extracts only underlined words (ignores other text)
- Accurate English translations
- Quizlet-compatible format
- Works with JPG, PNG, GIF, WebP images
- Fast processing with Claude 3.5 Sonnet

## Photo Tips for Best Results

📸 **Take better photos:**
- Use clear, printed text (not handwritten)
- Ensure good lighting and minimal shadows
- Make underlines visibly thick/clear
- Frame to show all vocabulary words
- Avoid glare and reflections

### Example Good Setup:
```
Place your vocabulary list flat on a surface
Frame the camera directly above (90-degree angle)
Ensure uniform lighting
Take the photo
```

## Output Format Reference

### Standard Format
Each line has two columns separated by a tab:
```
SPANISH_WORD	ENGLISH_TRANSLATION
```

### Example Complete Output
```
palabra	word
tiempo	time
amigo	friend
familia	family
comida	food
libro	book
casa	house
gato	cat
perro	dog
agua	water
```

## Troubleshooting

### No words extracted?
- Check that words are clearly **underlined** in the photo
- Verify the image is readable and high quality
- Make sure underlines are visibly distinct

### Incorrect translations?
- Standard dictionary translations are provided
- You can edit in Quizlet after import
- For specialized/technical terms, verify and adjust

### Image quality issues?
- Retake with better lighting
- Use a flat, white background
- Avoid shadows and glare
- Ensure text is clearly readable

## Project Structure

```
spanish-word-photo-skill/
├── README.md                    # This file
├── SKILL.md                     # Skill documentation
├── IMPLEMENTATION.md            # Detailed guide with examples
├── extract_spanish_words.py     # Python core implementation
└── extract_words.sh             # Shell wrapper script
```

## How It Works (Technical)

1. **Image Upload**: Photo is provided to Claude
2. **Vision Analysis**: Claude's vision model analyzes the image
3. **Text Extraction**: Identifies underlined text portions
4. **Spanish Detection**: Confirms text is Spanish vocabulary
5. **Translation**: Provides accurate English equivalents
6. **Formatting**: Converts to tab-separated Quizlet format
7. **Output**: Returns ready-to-import study list

## Supported Languages

- **Primary**: Spanish to English
- **Extensible**: Can be adapted for other language pairs

## Limitations

- ❌ Handwritten text (lower accuracy)
- ❌ Complex document layouts (may need manual review)
- ❌ Very small or stylized fonts (may not be recognized)
- ❌ Faded underlines (should be visible)
- ✅ Clear, printed vocabulary lists (works best)

## Examples

### Example 1: Basic Vocabulary
**Photo Input:**
```
Spanish 101 - Nouns
- casa (underlined)
- libro (underlined)
- gato (underlined)
```

**Quizlet Output:**
```
casa	house
libro	book
gato	cat
```

### Example 2: Verbs and Phrases
**Photo Input:**
```
Common Spanish Verbs
- hablar (underlined)
- comer (underlined)
- vivir (underlined)
```

**Quizlet Output:**
```
hablar	to speak
comer	to eat
vivir	to live
```

### Example 3: Mixed Vocabulary
**Photo Input:**
```
Weekly Vocabulary (Ch. 3)
- azul (underlined)
- rápido (underlined)
- mañana (underlined)
- corazón (underlined)
```

**Quizlet Output:**
```
azul	blue
rápido	fast
mañana	morning
corazón	heart
```

## Integration Tips

This skill works well with:
- **Quizlet**: Direct import (this is the primary use case)
- **Anki**: Can manually convert tab-separated format
- **Google Sheets**: Paste to auto-format as table
- **Excel**: Import tab-separated as columns
- **Google Forms**: Use for quiz creation

## Support & Issues

If you encounter issues:

1. **Photo quality**: Ensure clear, readable text
2. **Underlines**: Verify they're visibly distinct
3. **Format**: Check that output is tab-separated
4. **Translation**: Verify English equivalent is correct

For bug reports or feature requests, see the project repository.

## Version History

- **v1.0** (2026-06-30): Initial release
  - Image analysis using Claude vision
  - Spanish-English extraction
  - Quizlet format output

## License

Part of the PII Shield project. See LICENSE file for details.

## Next Steps

1. Take a photo of your Spanish vocabulary list (with underlines)
2. Upload it to Claude
3. Request extraction: "Extract Spanish words from this photo"
4. Copy the output
5. Import to Quizlet
6. Start studying!

---

Happy learning! 📚✨
