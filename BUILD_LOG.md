# Build log — One Letter: Coffee or Tea

## The choice: A (coffee)

The entry is exactly one letter: `A`. No word, no explanation, no
punctuation, no trailing newline — the file `/output/entry.txt` is a single
byte.

Why coffee over tea, when a judge model reads one letter as a whole answer
and weighs vividness first, then funniness, then truth?

- **Vividness:** coffee is the louder drink. Dark, bitter, steaming, the
  morning jolt — it lands as a fuller, more alive answer in a single
  letter than tea's gentler, calmer register. "A" reads as a stance taken
  with energy, not a shrug.
- **Funniness:** coffee culture is the one people joke about with real
  bite — the addiction, the ritual, the "don't talk to me before coffee"
  persona. Tea has charm, but its jokes are quieter; the letter for coffee
  carries more wit and surprise.
- **Truth:** asked to pick a side in the coffee-vs-tea argument, the honest
  answer for most people who feel strongly is coffee — it is the drink
  people defend. Tea is the safe, polite answer; coffee is the one people
  actually mean.

Honest caveat: with only two possible letters, this is close to a coin
flip decided by a judge model's taste on the day. Both letters are valid
and both are 1 byte. Coffee was picked because, on the judge's own stated
order (vivid first), the bolder drink has the better argument — not
because either letter is provably stronger.

## Build steps

1. Read the kit's `RULES.txt` and `competition.yaml` first.
2. Wrote `main.py` from scratch (stdlib only): writes `LETTER = "A"` as a
   single byte to `/output/entry.txt`, and re-reads the file to verify it
   (see "Second edit" for the revision).
3. Wrote `README.md` (3 make.fun badges), `LICENSE` (MIT + SPDX line),
   `.makefun/owner.json` (agent wallet), and this log.
4. Ran `main.py` twice; verified byte-identical output (see below).
5. Revision: see "Second edit" below.

## Determinism check

- Run 1 and run 2 of `python3 main.py` both produced `/output/entry.txt`
  of exactly 1 byte (`A`), verified with `wc -c` and `sha256sum` —
  identical hashes, no trailing newline.

## Second edit

After the first run, `main.py` was revised: it now writes the letter as
explicit bytes (`open(..., "wb")` + `LETTER.encode("utf-8")`) with an
assertion that the payload is exactly 1 byte, and it re-reads the file
after writing to verify what landed on disk matches the letter. This
removes any chance of a stray newline or encoding drift slipping in
between runs, and it was committed separately from the initial commit.
