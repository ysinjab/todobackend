#!/bin/bash
# Activate virtual environment
. /appenv/bin/activate

# # Download requirements to build cache
pip download -d /build -r requirements.txt --no-input

# # Install application test requirements
pip install --no-index -f /build -r requirements.txt
#pip install -r requirements.txt
# Run test.sh arguments
echo "wawawawa"
/usr/local/bin/wait-for.sh db:5432 -- echo "looooooove"

exec $@