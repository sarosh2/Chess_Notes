import chess
import chess.polyglot

board = chess.Board()

with chess.polyglot.open_reader("openings\Human-polyglot\Human.bin") as reader:
   for entry in reader.find_all(board):
       print(entry.move, entry.weight, entry.learn)