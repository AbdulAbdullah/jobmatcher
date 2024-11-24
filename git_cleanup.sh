#!/bin/bash

# Script to remove already tracked files that should be ignored
echo "Removing cached files from git..."
git rm -r --cached .

echo "Re-adding all files according to new .gitignore..."
git add .

echo "Committing changes..."
git commit -m "Remove files that should be ignored"

echo "Cleanup complete!"