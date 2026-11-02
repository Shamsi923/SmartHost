#!/bin/bash
set -e

DEST="$HOME/SmartHost-backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$DEST"

tar -czf "$DEST/smarthost_$DATE.tar.gz" \
-C "$HOME" SmartHost

echo "Backup completed successfully!"
ls -lh "$DEST"
