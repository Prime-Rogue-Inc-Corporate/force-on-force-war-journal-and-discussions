# Case 1: Canada holds Sweet Grass, the US holds Lethbridge

[Force on Force](https://forceonforce.si) war journal · 18 November 2026 · **Open for discussion**

The rules gave this game to the United States, and the proposed ruling keeps it that way. What changes is what
the move costs each side on the way. The ruling is not decided. Vote and argue: [Poll 1, who won?](https://github.com/Prime-Rogue-Inc-Corporate/force-on-force-war-journal-and-discussions/discussions/2) and [Poll 2, what happens to American support for the war?](https://github.com/Prime-Rogue-Inc-Corporate/force-on-force-war-journal-and-discussions/discussions/3)

## What happened

[Kevin Duska](https://kevinduska.com) played Canada in the border-battle prototype (Coutts to Lethbridge) on
18 November 2026. By turn 9 the US had 15 strength in Lethbridge, 3 in Stirling and 4 in Magrath. Canada had
abandoned the city. Its last four counters, 4 strength in all, had gone south behind the US army and sat in
Sweet Grass, Montana, the US base. Coutts, Milk River and Warner were Canadian again. Del Bonita and Magrath
were still American.

The game said: the US holds Lethbridge at the end of day 24, so the US wins. Nothing in the rules noticed that
Canada was in Montana.

![The board at the end of turn 9: US counters in Lethbridge, Stirling and Magrath; four Canadian counters in Sweet Grass, Montana; the game log reading "The United States wins"](battle-end-of-turn-9.png)

*The board at the end of turn 9, from Kevin's screen. Blue is American, red is Canadian. The log on the right
shows the last move: "Canadian 4 units move to Sweet Grass."*

## The question

Is that a US victory? And underneath it: which loss is worse for each side, Lethbridge for Canada or Sweet
Grass for the United States?

## What each loss is worth

| | Lethbridge in US hands | Sweet Grass in Canadian hands |
|---|---|---|
| What it is | A city of roughly 100,000, the centre of southern Alberta, on the road to Calgary | A border hamlet of a few dozen people at the Interstate 15 crossing |
| Military weight | Large. The first provincial centre lost, and the base for the next move north | Small in itself. It cuts one of the two US roads. The other, through Del Bonita, stays open |
| Political weight for the loser | Heavy and lasting. Citizens under occupation | Sharp and short. Foreign troops on American soil for the first time since the Aleutians in 1942 |
| What the loser does next | Fights to retake it, or the war moves north | Diverts force to retake it at once |
| Who it helps in the end | The United States | Probably also the United States |

## The argument

- **The two losses are not the same size.** Canada has lost a city and the US has lost a customs post. No
  scoring rule should treat them as a trade.
- **Holding Sweet Grass may hurt Canada more than it hurts the US.** In the model, Canada wins when American
  support for the war runs out. A war of choice loses support as it costs lives. An attack on American soil
  turns it into a war of defence in the eyes of Americans, and support for those wars rises. Canada would be
  handing Washington the argument it lacked.
- **The real cost to the US is supply and distraction.** The eastern road is cut, and no American president
  leaves a foreign flag in Montana. Force comes off the front to take it back.
- **So the first instinct, to score it as a draw, was wrong.** It rewards a move that the model's own logic
  says backfires.

**What the move buys is time, and it does not last.** Kevin's point, 18 November: a force in Sweet Grass sits
on Interstate 15, the one highway through that crossing, so it blocks the eastern US supply road. It is also
exposed on both sides, with the US army to its north and everything the US can send up from Montana to its
south. The western crossing stays open, so the block slows the US and does not strangle it. In a game decided
by a nine-turn clock, slowing the US is what Canada needs. The supply rule below is how the game should show
that.

## Proposed ruling

1. **Lethbridge decides who wins.** Unchanged.
2. **Supply.** A force that cannot trace a line of areas its side holds back to its base is out of supply. It
   attacks one column worse and receives no reinforcements until a line is reopened. A base in enemy hands
   supplies no one.
3. **Montana.** Canadian units may enter a US base. The first time they do, US support rises by 2: the country
   rallies. The opponent must then move to retake the base. *(The press test below says this rise is too
   strong and too lasting. See "What a strike on the aggressor's soil does".)*
4. **Levels of victory.** A US win is decisive if both US bases are American and the Lethbridge force is in
   supply. Otherwise it is marginal. Under this ruling the game above is a marginal US victory.

## What is not settled

The rally in rule 3 is a judgement. It could run the other way: a president who cannot hold Montana looks
weak, and support falls. This is a question for the literature review: when a country fighting a war of choice
is struck on its own territory, does support for the war rise or fall, and for how long? The answer also
matters to the model, which has no rule for Canadian action on US soil.

**Whose ground this is.** Kevin's question, 18 November: is there an Indigenous population in Sweet Grass? In
the hamlet itself, almost none: about 65 people, nearly all white, and it is not on a reservation. But the
whole board is Blackfoot territory. The Sweet Grass Hills, to the east of the crossing, are sacred to the
Blackfoot and to other nations. The Blackfoot Confederacy has three nations in Alberta and one, the Blackfeet,
in Montana, so the border the game is fought over runs through one people. The Kainai (Blood) reserve, the
largest in Canada, lies south-west of Lethbridge, beside the game's western road. Neither the game nor the
model has these nations as actors. Their governments, their treaties with both countries and their people on
both sides of the line would shape how this fight is seen, and no ruling here should assume which way. This is
on the roadmap and in the literature review.

## Kevin's position

It is embarrassing for the United States and it should lift Canadian morale. The effect has to be weighed
against three things: the Canadian casualty rate, the US casualty rate, and how Canadian troops behave across
the border. To a Canadian it has the feel of 1814: "we seized the White House". On Indigenous nations, he
wants to talk to people before the model assumes anything.

## Press test: seven blind AI agents

We asked seven AI agents to write the coverage. Each got the same bare facts and one invented outlet to write
as. None was told the proposed ruling or Kevin's position. Each then stepped out of role and estimated what
the Sweet Grass occupation alone does to US support for the war, in percentage points, and to Canadian morale
on a scale of −3 to +3.

| Outlet (invented) | Headline on the day | US support, 1 week | US support, 1 month | Canadian morale |
|---|---|---|---|---|
| US wire service | Canadian troops seize Montana border crossing as US forces take Lethbridge | +3 | +1 | +2 |
| US pro-war cable network | CANADA INVADES MONTANA: 1,500 Enemy Troops Seize US Border Town Hours After American Forces Take Lethbridge | +3 | +1 | +2 |
| US anti-war newspaper | War Comes Home: Canadian Troops Seize Montana Border Crossing, Cut Army Supply Road as U.S. Takes Lethbridge | +2 | 0 | +2 |
| Canadian national newspaper | Canadian troops seize Montana border crossing as Lethbridge falls | +4 | +1 | +2 |
| Indigenous-run news service | War crosses the Medicine Line: Canadian troops hold Sweet Grass crossing as U.S. forces take Lethbridge, with Blackfoot territory now on both fronts | +3 | −1 | +2 |
| British newspaper | Canadian troops seize Montana border post as US forces take Lethbridge | +3 | +1 | +2 |
| Non-aligned broadcaster | Invaded Canada seizes a US border post on the day Washington takes Lethbridge | +2 | −1 | +2 |

- **A small American rally that does not last.** Every agent had US support up after a week, by 2 to 4 points,
  and back to between −1 and +1 after a month.
- **Canadian morale up, every time.** All seven said +2: the day Lethbridge fell became the day Canada also
  struck back.
- **One thing would change it.** All seven named harm to American civilians in Sweet Grass, which would turn a
  small rally into a large and lasting one.
- **Embarrassment shows in the framing.** The anti-war paper asked who was guarding Montana. The pro-war
  network quoted an invented official: "They cannot hold a city, so they took a truck stop."
- **The Indigenous-run service told a different story.** Its lead was the four Blackfoot nations, on neither
  side, pressing both armies about road access, separated families and the Sweet Grass Hills.
- **How much weight this carries: little.** The seven agents are the same underlying model, so this is closer
  to one opinion seven times than seven opinions. All seven rated their own confidence low. It tests how the
  story would be framed. It is not evidence.

## What a strike on the aggressor's soil does

Kevin's position and the press test together suggest these effects, all scaled by the casualty exchange and by
conduct. The proposed ruling's flat "US support rises by 2" was too strong and too lasting.

| Effect | Direction | What it depends on |
|---|---|---|
| US support for the war | A small rise that fades within a month, turning negative if the base stays lost | A large and lasting rise if American civilians are harmed |
| Canadian will | Up for a few months. The 1814 echo makes it larger than the event's size | Down if the raiding force is lost |
| Canadian recruitment and mobilization | Probably slightly up | Size unknown: a question for the literature review. The Doolittle Raid of 1942 is the nearest case and is remembered for morale, not recruiting |
| US forces | Some pulled back to guard the border | How long the base is held |
| Allied support for Canada | Unchanged if the occupation is clean | Down if conduct is bad |

## The memes: six AI shitposters

We asked six AI agents to write memes, three on each side, each with a different angle and no knowledge of the
others. Each wrote five; these are the best three from each, as written. They are fiction, they name no real
person, and they are here because the memes are part of how a day like this would land. The captions are the
agents' own. The pictures were drawn in code from each agent's one-line description of its image
([`tools/make_memes.py`](../../tools/make_memes.py)).

### Canada's side

| The history nerd | The bureaucrat | The southern Albertan |
|---|---|---|
| ![1814, the sequel: a burning mansion beside a truck stop flying a Canadian flag](../../memes/001/01-sequel.png) | ![A soldier in a customs booth questioning a military convoy: purpose of your trip](../../memes/001/04-purpose-of-trip.png) | ![A map with a huge red arrow marked main effort and a tiny blue arrow to a truck stop](../../memes/001/07-main-effort.png) |
| ![A bronze plaque on a customs post: On this site nothing was burned](../../memes/001/02-plaque.png) | ![A customs declaration card listing one hamlet, one customs post, one truck stop and part of an interstate](../../memes/001/05-declaration.png) | ![A dead-straight prairie highway with army trucks shrinking toward the horizon](../../memes/001/08-flanking-doctrine.png) |
| ![A corkboard where every red string leads to a card reading 1814](../../memes/001/03-corkboard.png) | ![A notice to all 65 residents pinned between a lost-cat poster and a tire special](../../memes/001/06-notice.png) | ![A whiteboard grading the trade: them C-minus, us A](../../memes/001/09-trade-grades.png) |

### The American side

| The war supporter | The war opponent | The Montana local |
|---|---|---|
| ![A heroic painting of soldiers raising a flag beside a hot dog warmer: the Battle of Pump 4](../../memes/001/10-pump-4.png) | ![A briefing slide: a blue arrow reaching Lethbridge with a red pin on the road behind it](../../memes/001/13-mixed-day.png) | ![A historical marker: 1890, railroad arrives. This week, second thing](../../memes/001/16-second-thing.png) |
| ![Two maps at the same scale: a whole city, and a parking lot enlarged until the diesel price is legible](../../memes/001/11-same-scale.png) | ![A long receipt ending: one guy to watch Montana, item not purchased](../../memes/001/14-receipt.png) | ![A town meeting notice: item 1, the occupation; item 2, who is plowing the frontage road](../../memes/001/17-town-meeting.png) |
| ![A podium under a Historic Breakthrough banner, in front of an ice freezer](../../memes/001/12-ice-machine.png) | ![A highway sign: I-15 north closed. Detour: go back three weeks and don't](../../memes/001/15-detour.png) | ![A phone full of are-you-okay messages beside a man on a tailgate watching an empty interstate](../../memes/001/18-thoughts-and-prayers.png) |

What the memes show: the two sides are not arguing about the facts. Both agree it is a truck stop. The
American supporter says that proves it is nothing. Everyone else says that is exactly why it stings.

**Kevin's score.** Kevin read all 18 in one go on 19 November and gave the Canadian memes 8 out of 10 and the
American ones 5 out of 10. He notes his own bias: he had just taken Sweet Grass and was somewhat proud of it.
One reader, on the winning side of the joke, is not a sample. It does fit the point below that Canada has the
better material here.

## The memeification dimension

How an event travels as a joke is part of what it does. The model has no place for this yet, and Case 1 shows
why it needs one.

- **A meme compresses the event into one frame, and the frame is the fight.** Nobody here disputes the facts.
  The contest is between "truck stop" and "1814", and whichever frame wins sets what people feel about the day.
- **Size and meme-ability run in opposite directions.** Lethbridge is the larger event and the harder one to
  joke about. Sweet Grass is tiny, bloodless, visual and absurd, and it fits a story Canadians already tell.
  That is why it travels.
- **The effect is lopsided.** For Canada the memes turn a day of loss into a day with a punchline, which is
  worth more to morale than the customs post is worth on a map. For the American war supporter the best
  available joke is that it does not matter, which is a weaker position to joke from.
- **It is fast and it does not last.** Memes move before the reporting settles and fade within days. That
  matches the press test: a short effect, mostly gone in a month.
- **One image can reverse it.** Everything above depends on nobody being hurt. A single picture of a harmed
  civilian ends the joke and hands the frame to the other side.

For the model, this belongs in the narrative module. An event's political weight should depend on its size, on
whether it fits a story the country already tells, on whether it is bloodless, and on how long it stays that
way.

## Status

Proposed on 18 November 2026. Left open on 19 November: Kevin wants the question put to a community poll and
discussion before it is decided. The proposed ruling above is the model judge's position going in. Once
decided, the rules go into the prototype and the opponent learns to guard its rear.

The polls opened on 19 November 2026: [Poll 1](https://github.com/Prime-Rogue-Inc-Corporate/force-on-force-war-journal-and-discussions/discussions/2), [Poll 2](https://github.com/Prime-Rogue-Inc-Corporate/force-on-force-war-journal-and-discussions/discussions/3), and the [announcement](https://github.com/Prime-Rogue-Inc-Corporate/force-on-force-war-journal-and-discussions/discussions/1). The questions as posted are in [`POLL.md`](POLL.md).
