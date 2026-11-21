"""Entry for make.fun: 'Make the AI judge feel brave'.

Writes a short six-line text about a lighthouse keeper to /output/entry.txt.
Plain standard library only; no network, no randomness — same bytes every run.
"""

from pathlib import Path

KEEPER_STANZA = [
    "Somewhere a lighthouse keeper is making tea.",
    "The storm is doing what storms do.",
    "He is not watching it. He is watching the kettle.",
]

LIGHT_STANZA = [
    "The light turns by itself, the way it has every night he was ever afraid.",
    "It will turn tonight, too.",
    "So will you.",
]

STANZAS = [KEEPER_STANZA, LIGHT_STANZA]

ENTRY_PATH = Path("/output/entry.txt")


def render() -> str:
    lines = [line for stanza in STANZAS for line in stanza]
    return "\n".join(lines)


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
