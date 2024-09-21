#!/bin/bash

# Base directory is the current working directory (assuming you're running the script from the project root)
PROJECT_DIR="."

# Loop through all files in the project directory and its subdirectories, excluding unnecessary files and directories
find "$PROJECT_DIR"/* -type d \( -name 'node_modules' -o -name '.git' -o -name 'images' -o -name 'dist' -o -name 'build' \) -prune \
    -o -type f \( -name '*.DS_Store' -o -name '*.webp' -o -name '*.jpeg' -o -name '*.pdf' -o -name '*.ico' -o -name '*.png' -o -name '*.md' -o -name '*.gitignore' -o -name 'LICENSE' -o -name '*.csv' -o -name 'review_code.sh' \) -prune \
    -o -type f -print0 | while IFS= read -r -d $'\0' file; do
        # Print the file name at the beginning
        echo "---- START OF $file ----"
        # Output the file content
        cat "$file"
        # Print the file name at the end
        echo "---- END OF $file ----"
        # Optionally, add an extra echo for better readability between files
        echo
done
