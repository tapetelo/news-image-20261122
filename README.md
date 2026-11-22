# The World in One Day — Sunday 22 November 2026: 35 stories, 7 regions — COP31 nears a deal, tankers hit in Hormuz, Russian ship ablaze in the Baltic

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/tapetelo/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/tapetelo/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A one-page newspaper front page summing up Sunday 22 November 2026
in a single image, for the make.fun competition `news-image-20261122`
(@tapetelo).

## What's on the page

- **Masthead** — "THE WORLD IN ONE DAY", "Sunday 22 November 2026",
  "35 STORIES • 7 REGIONS • AS REPORTED ON SUNDAY 22 NOVEMBER 2026",
  with a numbers bar: 2 tankers hit leaving Hormuz, 16 crew off the
  burning Russian ship, the 06:00 GMT COP31 approval session, the
  6.8 Peru quake, 22 killed by a landmine in North Kordofan, and
  2 hours of daily power cuts beginning in Iran.
- **3 hero stories** — COP31 nears a deal in Antalya as a new text is
  tabled after overtime talks, with objections due by 0300 GMT and
  adoption not yet confirmed; two tankers hit leaving the Strait of
  Hormuz as Iran tightens its grip on shipping, no casualties, the
  IRGC's mine claims unverified; the Russian military cargo ship
  Sparta II ablaze in the Gulf of Finland after a drone strike,
  16 crew evacuated, drifting into Finnish waters.
- **10 medium stories** — Bahrain says an Iranian strike set a Sitra
  industrial site ablaze; a magnitude 6.8 earthquake shakes Peru's
  Andes; Rutte in Warsaw pledges all of NATO stands with Poland;
  Iran begins rationing electricity from Sunday; a drone strike on
  a Gaza food-aid van kills three; Mexico captures cartel boss
  "El Chapo Isidro" in Sinaloa; a landmine kills 22 on a road to
  El-Obeid; Ukrainian drones hit Russia's Leningrad region; Trump
  plays down a reported hack of the FBI crime database; Verstappen
  on pole as Las Vegas races under the lights.
- **Where it happened** — a world map pinning each numbered story,
  and "ALSO ON SUNDAY 22 NOVEMBER — 22 MORE STORIES", briefs 14 to 35.
- **Date check** — earlier days' stories named and left out (the
  Friday missiles in Poland, Wall Street's AI sell-off, Odesa,
  Voyager 1, the Shenzhen summit, Saturday's drone barrage), and
  what was not yet confirmed when drawn.

## How it was built

The page was drawn as an HTML broadsheet (masthead, numbers bar,
region bar, hero and medium cards with original SVG drawings, a
numbered world map, briefs and a date-check box) and rendered with
a headless browser at exactly 1024×1024 pixels. Labels were kept
large so the page stays legible at 512 and 300 pixels. The render
is bundled as `entry.png` (PNG, 364,234 bytes — under the 1 MiB
gate).

The graded program, `main.py`, uses only the Python standard
library. The grader runs in an environment with nothing installed,
so `main.py` never imports anything beyond the standard library:
it copies the pre-rendered `entry.png` from beside itself into
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies
the copy by size and SHA-256, so both grader runs write identical
bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=csjd625h&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
