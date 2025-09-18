#!/bin/sh
# Example failure hook script
# Usage: ON_DOWNLOAD_FAILURE=sh /app/hooks/on_failure.sh "$STATUS" "$URL" "$FILENAME" "$DEST_DIR"
STATUS="$1"
URL="$2"
FILENAME="$3"
DEST_DIR="$4"

MSG="[HOOK] FAILURE ts=$(date +%s) status=$STATUS url=$URL file=$FILENAME dest=$DEST_DIR"
echo "$MSG" | tee -a /data/tmp/hooks_test.log
