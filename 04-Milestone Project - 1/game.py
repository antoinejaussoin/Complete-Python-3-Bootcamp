print('Welcome to the TicTacToe Game')

game = [['', '', ''],['', '', ''],['', '', '']]

first_player_turn = True
first_symbol = 'X'
second_symbol = 'O'


def print_game(game):
  printout = ''
  for (row_index, row) in enumerate(game):
    for (cell_index, cell) in enumerate(row):
      printout += (' '+ cell if cell != '' else '  ') + (' |' if cell_index < len(row) - 1 else '')
    printout+= '\n-----------\n' if row_index < len(game) - 1 else '\n'
  print(printout)

def play(game, symbol, position):
  positions = { '1': (0,0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}
  if (position in positions):
    pos = positions[position]
    if game[pos[0]][pos[1]] == '':
      game[pos[0]][pos[1]] = symbol
      return True
  return False

def has_finished(game):
  for index in range(0, 3):
    if game[index][0] == game[index][1] == game[index][2]:
      return game[index][0]
    if game[0][index] == game[1][index] == game[2][index]:
      return game[0][index]
    if (game[0][0] == game[1][1] == game[2][2]):
      return game[0][0]
    if (game[0][2] == game[1][1] == game[2][0]):
      return game[0][2]

  return ''

def ask_turn(game):
  global first_player_turn
  player_name = 'Player 1' if first_player_turn else 'Player 2'
  player_symbol = first_symbol if first_player_turn else second_symbol
  coord = input(f"It's {player_name}'s turn to play. Enter a coordinate between 1 and 9:'")
  success = play(game, player_symbol, coord)
  if success:
    first_player_turn = not first_player_turn

print_game(game)
while has_finished(game) == '':
  ask_turn(game)
  print_game(game)

winner = 'Player 1' if has_finished(game) == 'X' else 'Player 2'
print(f'Bravo! The winner is {winner}')