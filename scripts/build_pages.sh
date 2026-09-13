#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$repo_root/.pages-src"
site_dir="$repo_root/.pages-site"

case "$source_dir:$site_dir" in
  "$repo_root/.pages-src:$repo_root/.pages-site") ;;
  *) echo "Refusing unexpected Pages paths" >&2; exit 1 ;;
esac

if [[ -e "$source_dir" ]]; then rm -r -- "$source_dir"; fi
if [[ -e "$site_dir" ]]; then rm -r -- "$site_dir"; fi

mkdir -p "$source_dir/de" "$source_dir/docs"
cp -- "$repo_root/README.md" "$source_dir/README.md"
cp -- "$repo_root/PUBLICATION_POLICY.md" "$repo_root/OPEN_SOURCE_BASELINE.md" \
  "$repo_root/CONTRIBUTING.md" "$repo_root/THIRD_PARTY_NOTICES.md" \
  "$repo_root/SECURITY.md" "$repo_root/AGENTS.md" "$source_dir/"
cp -R -- "$repo_root/docs/en" "$repo_root/docs/de" "$source_dir/docs/"
cp -- "$repo_root/de/README.md" "$repo_root/de/PUBLICATION_POLICY.md" \
  "$repo_root/de/OPEN_SOURCE_BASELINE.md" "$repo_root/de/CONTRIBUTING.md" \
  "$repo_root/de/THIRD_PARTY_NOTICES.md" "$repo_root/de/SECURITY.md" "$source_dir/de/"

mkdocs build --strict --config-file "$repo_root/mkdocs.yml" --site-dir "$site_dir"
