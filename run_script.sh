#!/bin/bash

echo "Starting script at $(date)" >> /path/to/project/debug.log

# Navigate to the project directory
cd /path/to/project || { echo "Failed to change directory" >> /path/to/project/debug.log; exit 1; }

# Activate the virtual environment
source /path/to/project/.venv/bin/activate || { echo "Failed to activate virtual environment" >> /path/to/project/debug.log; exit 1; }

# Run the Python script
python /path/to/project/main.py >> /path/to/project/debug.log 2>&1

# Deactivate the virtual environment (optional, for clean-up)
deactivate

echo "Finished script at $(date)" >> /path/to/project/debug.log
