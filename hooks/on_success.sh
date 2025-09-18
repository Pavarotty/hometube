#!/bin/sh
# Example success hook script
# Usage: ON_DOWNLOAD_SUCCESS=sh /app/hooks/on_success.sh "$OUTPUT_PATH" "$URL" "$FILENAME" "$DEST_DIR"
OUTPUT_PATH="$1"
URL="$2"
FILENAME="$3"
DEST_DIR="$4"

MSG="[HOOK] SUCCESS ts=$(date +%s) path=$OUTPUT_PATH url=$URL file=$FILENAME dest=$DEST_DIR"
echo "$MSG" | tee -a /data/tmp/hooks_test.log
