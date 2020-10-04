from time import sleep
from player2048 import Player2048
from utilities import *

player = Player2048()
sleep(2)

def evaluate_tiles():
    tile_container = player.browser.find_element_by_class_name('tile-container')
    positions, numbers = parse_string_regex(tile_container.get_attribute('innerHTML'))
    distinctify(positions, numbers)

    # A grid of all tiles by column
    player.grid_cols = [[pos for pos in positions if pos[0] == '1'], [pos for pos in positions if pos[0] == '2'],
                        [pos for pos in positions if pos[0] == '3'], [pos for pos in positions if pos[0] == '4']]

    # A grid of all tiles by row
    player.grid_rows = [[pos for pos in positions if pos[1] == '1'], [pos for pos in positions if pos[1] == '2'],
                        [pos for pos in positions if pos[1] == '3'], [pos for pos in positions if pos[1] == '4']]

    player.tile_mapping = {}
    for i in range(len(positions)):
        player.tile_mapping[positions[i]] = numbers[i]


while True:
    evaluate_tiles()

    if '2048' in player.tile_mapping.values():
        print('Bot won!')
        player.close()
    else:
        player.play_game()

