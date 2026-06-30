#!/usr/bin/env python3
"""
Spanish Word Photo Extractor
Extracts underlined Spanish words from photos and provides English translations
Format: Quizlet-compatible tab-separated values
"""

import sys
import base64
import json
from pathlib import Path


def encode_image_to_base64(image_path: str) -> str:
    """Read image file and encode to base64."""
    with open(image_path, "rb") as image_file:
        return base64.standard_b64encode(image_file.read()).decode("utf-8")


def get_image_media_type(image_path: str) -> str:
    """Determine media type from file extension."""
    ext = Path(image_path).suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp"
    }
    return media_types.get(ext, "image/jpeg")


def create_claude_prompt(image_path: str) -> dict:
    """Create a Claude API request for extracting Spanish words from the image."""

    base64_image = encode_image_to_base64(image_path)
    media_type = get_image_media_type(image_path)

    prompt = """Please analyze this image and extract ONLY the underlined Spanish words.

For each underlined Spanish word:
1. Extract the exact word as it appears
2. Provide the English translation
3. Format each pair on a new line as: SPANISH\tENGLISH

CRITICAL RULES:
- Only include words that are clearly underlined in the image
- Ignore any words that are not underlined
- Return ONLY the word pairs, no explanations or headers
- Use tab character (\\t) to separate Spanish from English
- One pair per line
- If no underlined words found, respond with: "NO_UNDERLINED_WORDS_FOUND"

Example output format:
gato\tcat
casa\thouse
perro\tdog"""

    return {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": base64_image,
                        },
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ],
            }
        ],
    }


def extract_words_from_photo(image_path: str) -> str:
    """
    Extract Spanish words from a photo using Claude's vision capabilities.

    Args:
        image_path: Path to the image file

    Returns:
        Quizlet-formatted string with Spanish-English word pairs
    """

    # Check if image exists
    if not Path(image_path).exists():
        return f"Error: Image file not found: {image_path}"

    # Create the API request
    request_data = create_claude_prompt(image_path)

    # Output the request as JSON for the wrapper to process
    print(json.dumps({
        "status": "ready",
        "request": request_data,
        "image_path": image_path
    }))


def format_quizlet_output(response_text: str) -> str:
    """
    Format Claude's response into Quizlet-compatible format.

    Args:
        response_text: Raw response from Claude

    Returns:
        Formatted string ready for Quizlet import
    """

    if "NO_UNDERLINED_WORDS_FOUND" in response_text:
        return "No underlined Spanish words found in the image."

    # Clean up the response
    lines = response_text.strip().split('\n')
    formatted_lines = []

    for line in lines:
        line = line.strip()
        if line and '\t' in line:
            # Ensure proper tab separation
            parts = line.split('\t')
            if len(parts) >= 2:
                spanish = parts[0].strip()
                english = parts[1].strip()
                formatted_lines.append(f"{spanish}\t{english}")

    return '\n'.join(formatted_lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_spanish_words.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    extract_words_from_photo(image_path)
