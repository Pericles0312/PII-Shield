#!/bin/bash
# Spanish Word Photo Skill - Shell wrapper
# Usage: ./extract_words.sh <image_path>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/extract_spanish_words.py"

if [ $# -lt 1 ]; then
    echo "Usage: $0 <image_path>"
    echo "Example: $0 /path/to/spanish_words.jpg"
    exit 1
fi

IMAGE_PATH="$1"

# Check if image exists
if [ ! -f "$IMAGE_PATH" ]; then
    echo "Error: Image file not found: $IMAGE_PATH"
    exit 1
fi

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script not found: $PYTHON_SCRIPT"
    exit 1
fi

# Run the Python script
python3 "$PYTHON_SCRIPT" "$IMAGE_PATH"
