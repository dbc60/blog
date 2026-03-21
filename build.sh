#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLIC_DIR="$SCRIPT_DIR/public"

echo "Building site with clean destination..."
hugo --cleanDestinationDir --source "$SCRIPT_DIR"

echo "Restoring public/ submodule .git pointer..."
echo "gitdir: ../.git/modules/public" > "$PUBLIC_DIR/.git"

echo "Done. public/ is rebuilt and submodule is intact."
