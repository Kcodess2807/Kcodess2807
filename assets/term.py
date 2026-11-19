"""Draw the README's terminal cards.  python assets/term.py

Each card is a list of lines; a line is a list of (text, colour) spans. Lines
appear one after another, once, and stay. Edit CARDS and rerun.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

W, PAD, LH, TOP = 820, 28, 21, 62
FONT = "'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace"
INK, DIM, FAINT = "#E6EDF3", "#8B949E", "#6E7681"
LIME, GREEN, BLUE, AMBER, RED = "#C8F169", "#3FB950", "#79C0FF", "#E3B341", "#FF7B72"


def cmd(text: str) -> list:
    return [("$ ", GREEN), (text, INK)]


def out(*spans) -> list:
    return [s if isinstance(s, tuple) else (s, DIM) for s in spans]


CARDS = {
    "header": ("arush@karnatak: ~", [
        cmd("neofetch"),
        [],
        out((r"     ___    __ __ ", LIME), "     ", ("arush", LIME), "@", ("karnatak", LIME)),
        out((r"    /   |  / //_/ ", LIME), "     -----------------"),
        out((r"   / /| | / ,<    ", LIME), "     ", ("role      ", BLUE), ("AI engineer", INK)),
        out((r"  / ___ |/ /| |   ", LIME), "     ", ("focus     ", BLUE), ("agent infrastructure, memory for agents", INK)),
        out((r" /_/  |_/_/ |_|   ", LIME), "     ", ("shipped   ", BLUE), ("graphsight (PyPI), saadho (live)", INK)),
        out("                  ", "     ", ("learning  ", BLUE), ("inference engineering", INK)),
        out("                  ", "     ", ("school    ", BLUE), ("B.Tech IT, GGSIPU, class of 2027", INK)),
        out("                  ", "     ", ("wins      ", BLUE), ("5 national hackathon finals, 2 first places", INK)),
    ]),
    "stack": ("arush@karnatak: ~/stack", [
        cmd("tree agent-stack/ --status"),
        out(("agent-stack/", BLUE)),
        *[out(branch, (f"{name:<16}", colour), f"{what:<58}", (tag, tag_colour))
          for branch, name, colour, what, tag, tag_colour in [
              ("├── ", "orchestration/", INK, "LangGraph agents, MCP servers, a pure-Python framework", "[shipped]", GREEN),
              ("├── ", "memory/", LIME, "graph + episodic memory with provenance, measured", "[main focus]", LIME),
              ("├── ", "payments/", INK, "integration work, a smaller part of what I do", "[some]", DIM),
              ("└── ", "inference/", INK, "batching, quantization, KV cache, serving engines", "[learning]", AMBER),
          ]],
    ]),
    "graphsight": ("graphsight: python", [
        cmd("pip install graphsight graphsight-langgraph"),
        [],
        out((">>> ", GREEN), ('memory.remember("checkout-service", "owned by", "payments team", source="standup-12")', INK)),
        out((">>> ", GREEN), ('memory.remember("checkout-service", "owned by", "billing team",', INK)),
        out(("...                 ", GREEN), ('source="reorg-memo", replace=True)', INK)),
        out((">>> ", GREEN), ('router.route("who owns checkout-service?").facts', INK)),
        out(("  checkout-service OWNED_BY billing team", LIME), "   (remembered, source: reorg-memo)"),
        out(("  checkout-service OWNED_BY payments team", FAINT), "  ended, kept as history"),
        out(("  PR #4821 TOUCHES checkout-service", INK), "        read from GitHub"),
        [],
        cmd("python eval/run_memory.py --tasks memory_pytest   # 22 held-out tasks, exact match"),
        out("  none 5/22    episodic 14/22    ", ("graph memory 16/22", LIME), "    p=0.007 vs none"),
    ]),
    "saadho": ("saadho.arushk.tech  (a web app, shown here as a CLI)", [
        cmd('saadho plan --role "ML engineer" --interview 2026-12-10 --hours 2'),
        out(("  21 days, 300+ vetted resources in prerequisite order", INK)),
        out("  day 01  ", ("Transformers from scratch", INK), "       read 2, skip 1"),
        out("  day 02  ", ("Retrieval and RAG evals", INK), "         read 3"),
        out("  day 03  ", ("Agents and tool use", INK), "             read 2, skip 2"),
        out("  ...     ", ("company guide: how 200+ companies interview, round by round", DIM)),
        [],
        cmd("saadho practice --room group-discussion --voice"),
        out("  4 AI colleagues joined  ", ("●", RED), " live   scorecard quotes your own words"),
    ]),
}


def render(title: str, lines: list) -> str:
    h = TOP + LH * len(lines) + 22
    body = []
    for i, spans in enumerate(lines):
        if not spans:
            continue
        tspans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in spans)
        body.append(f'<text class="l" style="animation-delay:{i * 0.22:.2f}s" x="{PAD}" y="{TOP + LH * i}" xml:space="preserve">{tspans}</text>')
    cursor_y = TOP + LH * len(lines) - 13
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{escape(title)} terminal">
<style>
.l {{ font-family: {FONT}; font-size: 12.5px; opacity: 0; animation: show .01s linear forwards; }}
@keyframes show {{ to {{ opacity: 1 }} }}
.c {{ animation: blink 1.1s steps(2) infinite; }}
@keyframes blink {{ 50% {{ opacity: 0 }} }}
@media (prefers-reduced-motion: reduce) {{ .l {{ animation: none; opacity: 1 }} .c {{ animation: none }} }}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="10" fill="#0D1117" stroke="#30363D"/>
<path d="M.5 10.5a10 10 0 0 1 10-10h{W - 21}a10 10 0 0 1 10 10V34H.5z" fill="#161B22"/>
<line x1=".5" y1="34" x2="{W - .5}" y2="34" stroke="#30363D"/>
<circle cx="20" cy="17" r="5" fill="#FF7B72"/><circle cx="38" cy="17" r="5" fill="#E3B341"/><circle cx="56" cy="17" r="5" fill="#3FB950"/>
<text x="{W / 2}" y="21.5" text-anchor="middle" font-family="{FONT}" font-size="11.5" fill="{DIM}">{escape(title)}</text>
{chr(10).join(body)}
<text class="l" style="animation-delay:{len(lines) * 0.22:.2f}s" x="{PAD}" y="{TOP + LH * len(lines)}" font-family="{FONT}" fill="{GREEN}">$</text>
<rect class="c" x="{PAD + 17}" y="{cursor_y}" width="8" height="15" fill="{LIME}"/>
</svg>
"""


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    for name, (title, lines) in CARDS.items():
        target = here.parent / "header.svg" if name == "header" else here / f"{name}.svg"
        target.write_text(render(title, lines), encoding="utf-8")
        print(target.name, max(sum(len(t) for t, _ in spans) for spans in lines if spans), "cols")
