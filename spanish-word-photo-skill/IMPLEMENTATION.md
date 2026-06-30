# Spanish Word Photo Skill - Implementation Guide

## Overview

This skill extracts underlined Spanish words from photos and generates Quizlet-formatted study lists with English translations.

## How the Skill Works

### Flow
1. User uploads a photo containing underlined Spanish vocabulary words
2. Claude analyzes the image using vision capabilities
3. Extracts only underlined words from the photo
4. Provides English translation for each word
5. Returns tab-separated format ready for Quizlet import

### Supported Formats
- **Input**: JPG, PNG, GIF, WebP images
- **Output**: Tab-separated values (TSV) for Quizlet

## Usage Instructions

### Method 1: Direct Claude Code Invocation (Recommended)

When you want to extract Spanish words from a photo, simply:

1. Tell Claude: "Extract Spanish words from this photo using the spanish-word-photo-skill"
2. Upload the photo containing underlined Spanish words
3. Claude will:
   - Analyze the image
   - Extract underlined words
   - Provide English translations
   - Format for Quizlet

### Method 2: Command Line

```bash
cd /home/user/PII-Shield/spanish-word-photo-skill
./extract_words.sh /path/to/your/image.jpg
```

### Method 3: Python Direct

```bash
python3 extract_spanish_words.py /path/to/your/image.jpg
```

## Quizlet Import Instructions

### To use the extracted words in Quizlet:

1. **Copy the output** from Claude
   - The format will be:
   ```
   palabra	word
   gato	cat
   casa	house
   perro	dog
   ```

2. **Import into Quizlet**:
   - Go to [Quizlet.com](https://quizlet.com)
   - Click "Create" → "Study Set"
   - Click "Import" or paste into the editor
   - Select "Tab or space separated" format
   - Paste your list
   - Click "Import"

3. **Verify** and save your study set

## Output Format Reference

### Standard Format
```
spanish_word	english_translation
```

### Example Output
```
gato	cat
casa	house
perro	dog
árbol	tree
libro	book
```

### Multiple Words (if photo has many)
```
palabra	word
tiempo	time
amigo	friend
familia	family
comida	food
```

## Technical Details

### What Claude Analyzes
- Scans the image for text
- Identifies underlined portions
- Extracts Spanish vocabulary words
- Provides accurate English translations

### What Gets Extracted
- ✅ Words that are visibly underlined
- ✅ Spanish language text
- ✅ Clear, readable text

### What Gets Ignored
- ❌ Non-underlined words
- ❌ Non-Spanish text
- ❌ Unclear or illegible text
- ❌ Handwritten text (if requested English handwritten translations)

## Tips for Best Results

### Photo Quality
- Use good lighting (natural light preferred)
- Minimize shadows and glare
- Frame so all words fit in the image
- Ensure underlines are clearly visible

### Document Preparation
- Use clear, printed text
- Ensure underlines are thick and visible
- Organize words in a vertical list (easier to extract)
- Don't crowd too many words together

### Example Good Photo
```
Spanish vocabulary list (underlined words shown):
- el gato (underlined)
- la casa (underlined)
- el perro (underlined)
```

## Troubleshooting

### No words extracted?
- Ensure words are clearly underlined in the photo
- Check that the image is readable
- Verify the photo includes the actual word content

### Wrong translations?
- Claude uses standard Spanish-English translations
- Technical or context-specific words might need manual adjustment in Quizlet
- You can edit translations directly in Quizlet after import

### Image quality issues?
- Take a new photo with better lighting
- Use a flat surface for the document
- Minimize glare and shadows

## Examples

### Example 1: Simple Vocabulary List
**Photo shows:**
```
Vocabulario:
- libro (underlined)
- mesa (underlined)
- silla (underlined)
```

**Output:**
```
libro	book
mesa	table
silla	chair
```

### Example 2: Multiple Words
**Photo shows:**
```
Spanish words to learn:
- agua (underlined)
- sol (underlined)
- luna (underlined)
- estrella (underlined)
```

**Output:**
```
agua	water
sol	sun
luna	moon
estrella	star
```

## Advanced Usage

### Batch Processing Multiple Photos
If you have multiple photos:
1. Process each photo separately
2. Copy the output for each
3. In Quizlet, create multiple study sets or one combined set
4. Paste all outputs combined (tab-separated format works for bulk import)

### Customizing Translations
After importing to Quizlet, you can:
- Edit any translation
- Add pronunciation
- Add images or context
- Organize into categories

## Integration with Other Tools

This skill works well with:
- **Quizlet**: Direct import compatibility
- **Anki**: Can convert tab-separated to Anki format
- **Google Sheets**: Can paste into spreadsheet (Ctrl+V)
- **Excel**: Paste and auto-format as table

## Limitations

- Works best with clearly printed text
- Handwritten text has lower accuracy
- Complex document layouts may need manual review
- Very small or stylized fonts might not be recognized

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify photo quality and underline visibility
3. Try again with a clearer photo
4. Report issues in the project repository

## Version

- **Skill Version**: 1.0
- **Last Updated**: 2026-06-30
- **Claude Model**: Claude 3.5 Sonnet
- **Languages**: Spanish/English (extendable to other languages)
