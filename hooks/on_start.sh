#!/bin/sh
# Example start hook script
# Usage: ON_DOWNLOAD_START=sh /app/hooks/on_start.sh "$URL" "$FILENAME" "$DEST_DIR" "$TMP_DIR" "$RUN_SEQ"
URL="$1"
FILENAME="$2"
DEST_DIR="$3"
TMP_DIR="$4"
RUN_SEQ="$5"

# Log to container tmp volume and stdout
MSG="[HOOK] START ts=$(date +%s) url=$URL file=$FILENAME dest=$DEST_DIR run=$RUN_SEQ"
echo "$MSG" | tee -a /data/tmp/hooks_test.log
