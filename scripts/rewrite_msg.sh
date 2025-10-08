#!/bin/bash

# Script to rewrite commit messages for conventional commits
# Makes lowercase and truncates to 60 chars

# Read from stdin
MSG=$(cat)

# Convert to lowercase
MSG=$(echo "$MSG" | tr '[:upper:]' '[:lower:]')

# Truncate to 60 chars (but keep first line)
FIRST_LINE=$(echo "$MSG" | head -n1 | cut -c1-60)
REST=$(echo "$MSG" | tail -n +2)

echo "$FIRST_LINE"
if [ -n "$REST" ]; then
    echo "$REST"
fi