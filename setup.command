#!/bin/bash

# Install Homebrew if not already installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python if not already installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Installing Python3..."
    brew install python
fi

# Install required Python packages
echo "Installing required Python packages..."
pip3 install pydub SpeechRecognition

# Create the TranscriptionTool directory in the user's Documents folder
mkdir -p ~/Documents/TranscriptionTool

# Copy the scripts to the TranscriptionTool directory
cp Transcribe.py run_transcribe.command ~/Documents/TranscriptionTool/

# Make run_transcribe.command executable
chmod +x ~/Documents/TranscriptionTool/run_transcribe.command

# Create a symbolic link in the Applications directory
ln -s ~/Documents/TranscriptionTool/run_transcribe.command ~/Applications/Run_Transcribe

echo "Setup completed. You can now run the TranscriptionTool by clicking 'Run_Transcribe' in your Applications directory or by double-clicking 'run_transcribe.command' in your Documents/TranscriptionTool directory."
