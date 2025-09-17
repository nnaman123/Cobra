#!/bin/bash

# Create hidden folder for Cobra
mkdir -p ~/.cobra

# Download interpreter + launcher from GitHub
curl -sSL https://raw.githubusercontent.com/nnaman123/Cobra/main/cobra.py -o ~/.cobra/cobra.py
curl -sSL https://raw.githubusercontent.com/nnaman123/Cobra/main/cobra -o ~/.cobra/cobra

# Make them executable
chmod +x ~/.cobra/cobra.py
chmod +x ~/.cobra/cobra

# Add to PATH if not already added
if ! grep -q 'export PATH="$HOME/.cobra:$PATH"' ~/.zshrc; then
    echo 'export PATH="$HOME/.cobra:$PATH"' >> ~/.zshrc
fi

# Reload shell
source ~/.zshrc

echo "✅ Cobra installed! Run with: cobra <file.cbr>"
