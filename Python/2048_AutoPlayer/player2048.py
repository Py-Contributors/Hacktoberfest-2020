import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Player2048:
    # Initialize all attributes
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://play2048.co/')
        self.browser.fullscreen_window()
        self.html = self.browser.find_element_by_tag_name('html')
        self.keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
        self.keys_hor = self.keys[2:]
        self.keys_ver = self.keys[:2]
        self.grid_rows = []
        self.grid_cols = []
        self.tile_mapping = {}

    # If there are two neighboring tiles in any column, press a vertical key
    def find_matching_col_tiles(self):
        for column in self.grid_cols:
            for tile in range(1, len(column) - 1):
                if int(self.tile_mapping[column[tile]]) == int(self.tile_mapping[column[tile - 1]]):
                    return True
        return False

    # If there are two neighboring tiles in any row, press a horizontal key
    def find_matching_row_tiles(self):
        for row in self.grid_rows:
            for tile in range(1, len(row) - 1):
                if int(self.tile_mapping[row[tile]]) == int(self.tile_mapping[row[tile - 1]]):
                    return True
        return False

    def play_game(self):
        if self.find_matching_row_tiles():
            self.html.send_keys(random.choice(self.keys_hor))

        elif self.find_matching_col_tiles():
            self.html.send_keys(random.choice(self.keys_ver))

        else:
            self.html.send_keys(random.choice(self.keys))
        sleep(0.5)

    def close(self):
        self.browser.quit()
