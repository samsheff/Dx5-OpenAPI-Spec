#!/usr/bin/env bash
set -euo pipefail
BASE="https://distillx5.com"
OUT="/Users/samsheff/code/archetype/dx5/artifacts/bundles"
mkdir -p "$OUT"
while IFS= read -r path; do
  [ -z "$path" ] && continue
  url="$BASE$path"
  fname="${path%%\?*}"
  fname="${fname#/}"
  fname="${fname//\//__}"
  echo "Downloading $url -> $fname"
  curl -sS -L --max-time 60 -o "$OUT/$fname" "$url" || echo "FAILED $url"
done
