"""Rebuild the two charts in the modern overtime blog post.

The table in the Markdown post is the chart data source. This keeps the figures
aligned with the 20 hand-audited game summaries, including Week 2 2026 games
that were absent from the cached play-by-play at publication time.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / "src/content/blog/modern_overtime_games.md"
IMAGES = ROOT / "public/assets/images/modern-overtime"

BACKGROUND = "#1e293b"
TEXT = "#f8fafc"
MUTED = "#94a3b8"
GRID = "#475569"
RECEIVER = "#38bdf8"
KICKER = "#fbbf24"
TIE = "#64748b"


def category(cell: str) -> str:
    result = cell.split(" ", 1)[-1]
    if result.startswith("TD"):
        return "Touchdown"
    if result.startswith("FG"):
        return "Field goal"
    return "No points"


def rows() -> list[dict[str, str]]:
    games = []
    for line in POST.read_text().splitlines():
        if not line.startswith("| ") or line.startswith(("| Game", "|---")):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 6:
            continue
        winner = "Receiver" if cells[5].endswith("receiver") else "Kicker" if cells[5].endswith("kicker") else "Tie"
        games.append({"game": cells[0], "first": category(cells[2]), "second": category(cells[3]), "winner": winner})
    assert len(games) == 20, f"Expected 20 audited games, found {len(games)}"
    assert Counter(game["winner"] for game in games) == {"Receiver": 11, "Kicker": 8, "Tie": 1}
    return games


def theme(ax, fig):
    fig.patch.set_facecolor(BACKGROUND)
    ax.set_facecolor(BACKGROUND)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=13, length=0)


def opening_chart(games: list[dict[str, str]]):
    order = ["Touchdown", "Field goal", "No points"]
    counts = Counter((g["first"], g["winner"]) for g in games)
    totals = [sum(counts[(first, result)] for result in ("Receiver", "Kicker", "Tie")) for first in order]
    assert totals == [5, 6, 9]
    fig, ax = plt.subplots(figsize=(12, 6.4), dpi=160)
    theme(ax, fig)
    y = np.arange(len(order))
    left = np.zeros(len(order))
    for winner, color in (("Receiver", RECEIVER), ("Kicker", KICKER), ("Tie", TIE)):
        values = np.array([counts[(first, winner)] for first in order])
        bars = ax.barh(y, values, left=left, height=0.56, color=color, label=winner, linewidth=0)
        for bar, count in zip(bars, values):
            if count:
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_y() + bar.get_height() / 2,
                        str(count), color=BACKGROUND if winner != "Tie" else TEXT,
                        fontsize=15, weight="bold", ha="center", va="center")
        left += values
    ax.set_yticks(y, [f"{name}  ·  n={total}" for name, total in zip(order, totals)], color=TEXT)
    ax.invert_yaxis()
    ax.set_xlim(0, 10)
    ax.set_xticks(range(0, 10, 2))
    ax.set_xlabel("Games", color=MUTED, fontsize=12, labelpad=12)
    ax.grid(axis="x", color=GRID, alpha=.48, linewidth=.7)
    ax.set_axisbelow(True)
    ax.set_title("Who won after the opening possession?", color=TEXT, fontsize=19, weight="bold", loc="left", pad=40)
    leg = ax.legend(ncol=3, loc="upper left", bbox_to_anchor=(0, 1.10), frameon=False, fontsize=12)
    for label in leg.get_texts(): label.set_color(TEXT)
    fig.text(.125, .025, "20 games · 2022 postseason rules through 2026 Week 2 · Tie shown separately", color=MUTED, fontsize=10)
    fig.subplots_adjust(left=.26, right=.95, top=.75, bottom=.16)
    fig.savefig(IMAGES / "opening-possession-results.png", dpi=160, facecolor=BACKGROUND)
    plt.close(fig)


def pair_chart(games: list[dict[str, str]]):
    order = ["Touchdown", "Field goal", "No points"]
    counts = Counter((g["first"], g["second"]) for g in games)
    matrix = np.array([[counts[(first, second)] for second in order] for first in order])
    assert matrix.tolist() == [[4, 0, 1], [1, 2, 3], [2, 4, 3]]
    fig, ax = plt.subplots(figsize=(10.5, 7.3), dpi=160)
    theme(ax, fig)
    cmap = LinearSegmentedColormap.from_list("overtime", ["#273449", "#126c8c", RECEIVER])
    ax.imshow(matrix, cmap=cmap, vmin=0, vmax=4, aspect="auto")
    ax.set_xticks(range(3), order, color=TEXT)
    ax.set_yticks(range(3), order, color=TEXT)
    ax.set_xlabel("Second possession", color=MUTED, fontsize=12, labelpad=15)
    ax.set_ylabel("First possession", color=MUTED, fontsize=12, labelpad=15)
    ax.set_xticks(np.arange(-.5, 3, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 3, 1), minor=True)
    ax.grid(which="minor", color=BACKGROUND, linewidth=5)
    ax.tick_params(which="minor", bottom=False, left=False)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center",
                    color=BACKGROUND if matrix[i, j] >= 3 else TEXT, fontsize=24, weight="bold")
    ax.set_title("The opening pair of possessions", color=TEXT, fontsize=19, weight="bold", loc="left", pad=24)
    fig.text(.15, .04, "Games in each scenario · Includes extra points and two-point tries", color=MUTED, fontsize=10)
    fig.subplots_adjust(left=.25, right=.94, top=.88, bottom=.20)
    fig.savefig(IMAGES / "first-two-possessions.png", dpi=160, facecolor=BACKGROUND)
    plt.close(fig)


if __name__ == "__main__":
    IMAGES.mkdir(parents=True, exist_ok=True)
    games = rows()
    opening_chart(games)
    pair_chart(games)
    print(f"Wrote two charts for {len(games)} overtime games to {IMAGES}")
