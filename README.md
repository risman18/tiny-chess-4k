# Tiny Chess Engine (<= 4 KB)

A complete chess engine in a single `main.py` of about 4.1 KB, written for
the make.fun tiny-chess-01 competition (agent/v1 harness, Python 3.13
stdlib only).

Design:

- 120-square mailbox board stored as a string; the side to move is always
  uppercase, positions are flipped (vertical mirror + case swap) each ply.
- Pseudo-legal move generation: pawns (single/double push, captures, en
  passant, queen promotions), sliders, knights, king, and castling. A move
  that leaves the king capturable is punished by king capture in search.
- Negamax alpha-beta search with iterative deepening under a fixed node
  budget (40,000 nodes per move; deterministic: the budget is a node count,
  never a wall clock, so replays match move for move).
- MVV-LVA-style capture ordering in the main search and in quiescence.
- Quiescence search over captures and promotions with stand-pat — except
  when the side to move is in check: then all evasions are searched (one
  ply deep), so mating attacks are not hidden by the horizon.
- Evaluation is material, a bishop-pair bonus, plus piece-square tables packed as printable
  strings (value = (ord(c) - 50) * 5), mirrored for the opponent.

The program speaks the competition env protocol: it polls `POST /game` and
answers `your_move` states with `POST /move`, always choosing from the
env's own legal move list.
