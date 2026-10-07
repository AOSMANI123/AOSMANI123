"""Rebuild til/README.md from the TIL entries.

Each entry is a Markdown file in a topic folder (til/<topic>/<slug>.md).
The title is the file's first "# " heading. The date is when the file was
first committed to git (falls back to today for uncommitted files).

Run: python3 til/build_index.py
"""

import datetime
import pathlib
import subprocess

TIL_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = TIL_DIR.parent


def first_commit_date(path: pathlib.Path) -> datetime.date:
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--follow", "--format=%as", "--", str(path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    dates = result.stdout.split()
    if dates:
        return datetime.date.fromisoformat(dates[-1])
    return datetime.date.today()


def title_of(path: pathlib.Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").capitalize()


def format_date(d: datetime.date) -> str:
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def main() -> None:
    entries = []
    for path in sorted(TIL_DIR.glob("*/*.md")):
        entries.append(
            {
                "topic": path.parent.name,
                "title": title_of(path),
                "link": path.relative_to(TIL_DIR).as_posix(),
                "date": first_commit_date(path),
            }
        )

    lines = [
        "# Today I Learned",
        "",
        "Short notes on what I learn while building agents, evals and AI products.",
        "Each one comes from a real build. This index rebuilds itself on every push.",
        "",
        f"**{len(entries)} entries**",
        "",
        "## Recent",
        "",
    ]
    for e in sorted(entries, key=lambda e: e["date"], reverse=True)[:5]:
        lines.append(f"- [{e['title']}]({e['link']}) · {e['topic']} · {format_date(e['date'])}")

    topics = sorted({e["topic"] for e in entries})
    for topic in topics:
        lines += ["", f"## {topic.capitalize()}", ""]
        for e in sorted((e for e in entries if e["topic"] == topic), key=lambda e: e["date"]):
            lines.append(f"- [{e['title']}]({e['link']}) · {format_date(e['date'])}")

    (TIL_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote index with {len(entries)} entries across {len(topics)} topics.")


if __name__ == "__main__":
    main()
