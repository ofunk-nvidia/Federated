#!/usr/bin/env python3
"""Conservative publication gate for this documentation-only repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
MAX_TEXT_BYTES = 2 * 1024 * 1024
MAX_IMAGE_BYTES = 5 * 1024 * 1024
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
IGNORED_PARTS = {".git", ".pages-site", ".pages-src"}
PROHIBITED_SUFFIXES = {
    ".7z", ".bin", ".ckpt", ".db", ".dmp", ".dump", ".env", ".fmb",
    ".gz", ".jks", ".keystore", ".onnx", ".p12", ".parquet", ".pem",
    ".pfx", ".pt", ".pth", ".rdf", ".safetensors", ".sqlite", ".tar", ".zip",
}
PROHIBITED_PARTS = {
    "adapters", "checkpoints", "client-data", "customer-data", "customer-projects",
    "datasets", "model-weights", "raw-data",
}
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "credential assignment": re.compile(
        r"(?i)\b(?:password|passwd|pwd|secret|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[^\s'\"<{]{8,}"
    ),
    "restricted marking": re.compile(
        r"\b(?:NVIDIA CONFIDENTIAL|CLIENT CONFIDENTIAL|INTERNAL USE ONLY|DO NOT DISTRIBUTE)\b"
    ),
}
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PRESENTATION_PAIRS = (
    ("README.md", "de/README.md"),
    ("docs/en/architecture.md", "docs/de/architecture.md"),
    ("docs/en/workflow.md", "docs/de/workflow.md"),
    ("docs/en/toolchain.md", "docs/de/toolchain.md"),
    ("docs/en/governance.md", "docs/de/governance.md"),
)


def check_language_paths(failures: list[str]) -> None:
    """Require parallel monolingual presentation paths with matching structure."""
    for english_name, german_name in PRESENTATION_PAIRS:
        english_path = ROOT / english_name
        german_path = ROOT / german_name
        if not english_path.is_file() or not german_path.is_file():
            failures.append(f"missing language pair: {english_name} <-> {german_name}")
            continue
        english = english_path.read_text(encoding="utf-8")
        german = german_path.read_text(encoding="utf-8")
        english_nav = next((line for line in english.splitlines()[:8] if line.startswith("[")), "")
        german_nav = next((line for line in german.splitlines()[:8] if line.startswith("[")), "")
        if english_nav.count("](") != german_nav.count("](") or english_nav.count("](") != 6:
            failures.append(f"navigation mismatch: {english_name} <-> {german_name}")
        if "Deutsch" not in english_nav or "English" not in german_nav:
            failures.append(f"language switch missing: {english_name} <-> {german_name}")
        if english.count("```mermaid") != german.count("```mermaid"):
            failures.append(f"Mermaid count mismatch: {english_name} <-> {german_name}")
        english_sections = sum(line.startswith(("## ", "### ")) for line in english.splitlines())
        german_sections = sum(line.startswith(("## ", "### ")) for line in german.splitlines())
        if english_sections != german_sections:
            failures.append(f"section-count mismatch: {english_name} <-> {german_name}")


def main() -> int:
    failures: list[str] = []
    check_language_paths(failures)
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        if IGNORED_PARTS.intersection(path.parts):
            continue
        rel = path.relative_to(ROOT)
        lowered_parts = {part.lower() for part in rel.parts}
        suffix = path.suffix.lower()
        size = path.stat().st_size

        if lowered_parts & PROHIBITED_PARTS:
            failures.append(f"{rel}: prohibited path")
            continue
        if suffix in PROHIBITED_SUFFIXES:
            failures.append(f"{rel}: prohibited file type")
            continue
        if suffix in IMAGE_SUFFIXES:
            if size > MAX_IMAGE_BYTES:
                failures.append(f"{rel}: image exceeds {MAX_IMAGE_BYTES} bytes")
            continue
        if size > MAX_TEXT_BYTES:
            failures.append(f"{rel}: file exceeds {MAX_TEXT_BYTES} bytes")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            failures.append(f"{rel}: unapproved binary file")
            continue
        if path.resolve() == SELF:
            continue
        for target in MARKDOWN_LINK.findall(content):
            clean_target = target.split("#", 1)[0]
            if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                continue
            if not (path.parent / clean_target).resolve().exists():
                failures.append(f"{rel}: broken relative link to {target}")
        for label, pattern in PATTERNS.items():
            if pattern.search(content):
                failures.append(f"{rel}: possible {label}")

    if failures:
        print("Publication gate failed:")
        for failure in failures:
            print(f"- {failure}")
        print("Human provenance and confidentiality review is required even after fixing these findings.")
        return 1

    print("Automated publication gate passed.")
    print("This does not replace human provenance, licence, confidentiality, and privacy review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
