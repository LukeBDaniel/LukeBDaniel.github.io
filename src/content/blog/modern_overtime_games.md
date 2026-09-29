---
title: "Modern NFL Overtime: Every Game So Far"
description: "A possession-by-possession look at every NFL game played under the modern overtime rules through September 20, 2026."
pubDate: 'Sep 21 2026'
thumbnail: "/assets/images/modern-overtime/opening-possession-results.png"
thumbnailAlt: "Chart comparing outcomes by the opening possession result in modern NFL overtime games"
thumbnailWidth: 1920
thumbnailHeight: 1024
---

# Modern NFL overtime: every game so far

**Scope and data.** This is a standalone descriptive look at the first-possession rules adopted for the **2022 postseason** and extended to the **2025 regular season**. I inspected the cached nflverse play-by-play through 2026 Week 1, then checked the [NFL's completed Week 2 results](https://www.nfl.com/news/2026-nfl-season-week-2-what-we-learned-from-sunday-s-games) for newer overtime games. The result is **20 games through Sunday, September 20, 2026** (three postseason, 17 regular season). The 2026 local file is partial; the two Week 2 rows below come from official team recaps. The opening kickoff identifies the receiving team; consecutive scrimmage possessions identify drives. Scoring includes the extra point or two-point try attached to a touchdown. Final scores were checked against each game's play-by-play result or official recap.

Under the [NFL's 2025 Rule 16](https://operations.nfl.com/the-rules/nfl-rulebook), both teams generally get one possession even if the first team scores a touchdown. A safety scored by the kicking team on the receiver's first possession is an exception. After the first pair, play becomes sudden death if tied. The regular-season period is capped at 10 minutes and can end in a tie; postseason play continues until a winner. The [2022 rule change](https://operations.nfl.com/media/5kvgzyss/2022-nfl-rulebook-final.pdf) applied the two-possession guarantee to postseason games first.

In the table, **receiver** means the team that possessed the ball first, and **kicker** means the team that kicked the opening overtime kickoff. `TD+1` and `TD+2` include the try; `TD+0` means a touchdown without added try points (including failed two-point tries or a walk-off touchdown). “Downs” includes a failed fourth down. A dash means the game ended before a third possession.

![Stacked bars showing receiver wins, kicker wins, and a tie after each opening-possession result: touchdown, field goal, or no points.](/assets/images/modern-overtime/opening-possession-results.png)

[Open the opening-possession chart full size](/assets/images/modern-overtime/opening-possession-results.png)

| Game | Receiver / kicker | First possession | Second possession | Later possessions | Result |
|---|---|---|---|---|---|
| 2023 postseason: SF–KC (Super Bowl) | SF / KC | SF FG | KC TD+0 | — | KC, kicker |
| 2025 W2: NYG–DAL | DAL / NYG | DAL punt | NYG punt | DAL punt → NYG INT → DAL FG | DAL, receiver |
| 2025 W4: GB–DAL | DAL / GB | DAL FG | GB FG | — | Tie, 40–40 |
| 2025 W5: SF–LA | SF / LA | SF FG | LA downs | — | SF, receiver |
| 2025 W9: JAX–LV | JAX / LV | JAX TD+1 | LV TD+0, failed 2 | — | JAX, receiver |
| 2025 W10: ATL–IND | ATL / IND | ATL punt | IND TD+0 | — | IND, kicker |
| 2025 W11: CAR–ATL | ATL / CAR | ATL punt | CAR FG | — | CAR, kicker |
| 2025 W11: WAS–MIA | WAS / MIA | WAS INT | MIA FG | — | MIA, kicker |
| 2025 W12: IND–KC | IND / KC | IND punt | KC FG | — | KC, kicker |
| 2025 W12: JAX–ARI | JAX / ARI | JAX FG | ARI downs | — | JAX, receiver |
| 2025 W12: NYG–DET | DET / NYG | DET TD+1 | NYG downs | — | DET, receiver |
| 2025 W13: DEN–WAS | DEN / WAS | DEN TD+1 | WAS TD+0, failed 2 | — | DEN, receiver |
| 2025 W14: PHI–LAC | LAC / PHI | LAC FG | PHI INT | — | LAC, receiver |
| 2025 W16: GB–CHI | GB / CHI | GB fumble | CHI TD+0 | — | CHI, kicker |
| 2025 W16: LA–SEA | LA / SEA | LA TD+1 | SEA TD+2 | — | SEA, kicker |
| 2025 postseason: BUF–DEN | DEN / BUF | DEN punt | BUF INT | DEN FG | DEN, receiver |
| 2025 postseason: LA–CHI | LA / CHI | LA punt | CHI INT | LA FG | LA, receiver |
| 2026 W1: NO–DET | DET / NO | DET TD+1 | NO TD+0, failed 2 | — | DET, receiver |
| [2026 W2: GB–NYJ](https://www.packers.com/news/in-game-updates-week-2-jets-2026) | NYJ / GB | NYJ punt | GB FG | — | GB, kicker |
| [2026 W2: IND–KC](https://www.chiefs.com/news/chiefs-defeat-colts-33-30-in-overtime-thriller-on-sunday-night-football) | KC / IND | KC FG | IND FG | KC FG | KC, receiver |

**What happened most often.** The opening possession produced five touchdowns, six field goals, and nine empty drives (seven punts, one interception, one fumble). Sixteen games ended within the first two possessions; three reached a third, and the NYG–DAL game reached a fifth. When the first team scored a touchdown, it won four of five games. The exception was LA–SEA: Seattle answered a seven-point touchdown with a touchdown and successful two-point try. When the first team kicked a field goal, it won four, lost one, and tied one. When it came away empty, it won three and lost six.

![Three-by-three chart counting games by the scoring result of the first and second overtime possessions.](/assets/images/modern-overtime/first-two-possessions.png)

[Open the possession-pair chart full size](/assets/images/modern-overtime/first-two-possessions.png)

**Did receiving or kicking have the advantage?** The receiver won **11**, the kicker won **8**, and **one** game tied. Among decisive games, that is **11/19 (58%)** for the receiver; a 95% Wilson interval is approximately **36%–77%**. This sample is much too small to establish an inherent advantage. Teams also choose whether to kick or receive after the toss, so these results are not a randomized comparison of the two strategies. The observed tradeoff is visible in the games: the second team knows the opening result and can choose its fourth-down and try strategy accordingly, while the first team gets the ball first in sudden death if the opening pair stays tied. In all four games that went beyond two possessions, the original receiver ultimately won.

**Method limit.** This maps observed possessions and scoring, not what would have happened had either team made the opposite coin-toss choice. Kickoff returns, field position, injuries, team strength, and late-clock decisions differ across games. The cached play-by-play files are in the separate `fourth-down-calc/.cache/pbp/` checkout; its full 2018–2026 cache was scanned for qualifying overtime games. The two Week 2 games were cross-checked with the linked Packers and Chiefs reports because they are absent from the local cache.
