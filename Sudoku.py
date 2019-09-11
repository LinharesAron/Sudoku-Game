from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from concurrent.futures import ThreadPoolExecutor
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
from Solver import Matrix, Print, Solve

delay = 10
size = 9
divs = Matrix(size)
sudoku = Matrix(size)

driver = webdriver.Firefox()
action = ActionChains(driver)

urlgame = 'https://www.sudokubum.com/'
driver.get(urlgame)

extreme = WebDriverWait(driver, delay).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'level'))
)

levels = extreme.find_elements_by_tag_name('li')
levels[len(levels) - 1].click()

time.sleep(5)

game_div = WebDriverWait(driver, delay).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'contwrap'))
            )
tables = game_div.find_elements_by_tag_name('table')

out_index = 0
for table in tables:
    if 'box b' in table.get_attribute('class'):
        spans = table.find_elements_by_tag_name('span')
        for index, span in enumerate(spans):
            row = int(out_index // (size/3) * 3 + (index // (size/3)))
            col = int(out_index % (size/3) * 3 + (index % (size/3)))
            value = span.text.strip()
            sudoku[row][col] = int(value) if value else 0
            divs[row][col] = span.find_element_by_xpath('../../..')
        out_index = out_index + 1

sucesso = Solve(sudoku)
Print(sudoku)

if sucesso:
    for r in range(size):
        for c in range(size):
            if 'user' in divs[r][c].get_attribute('class'):
                action.send_keys_to_element(divs[r][c], str(sudoku[r][c]))
    action.perform()
    time.sleep(10)
driver.close()