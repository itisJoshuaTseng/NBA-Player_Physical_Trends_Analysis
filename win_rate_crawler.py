from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Selenium settings
options = Options()
options.add_argument('--disable-extensions')
options.add_argument('blink-settings=imageEnabled=false')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


# full url: baseurl + team_abbr + / + year + .html
team_abbr =  ["HOU", "DEN", "LAL", "GSW", "MIN", "LAC", "SAC", "DAL", "PHO", "POR"]
base_url = 'https://www.basketball-reference.com/teams/'
base_folder = "nba_rosters"
years = [i for i in range(1990, 2026)]


def fetch_win(url, team_name, year):
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        win_rate_elem = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="team_misc"]/tbody/tr[1]/td[1]'))
        )
        
        win_rate = win_rate_elem.text
        print(f"{team_name} {year} winrate: {win_rate}")
        
        driver.quit()  # Don't forget to quit the driver
        return {
            'team': team_name,
            'year': year,
            'win_rate': win_rate
        }

    except NoSuchElementException:
        print(f"{team_name} {year} ❌ can't be found")
    except Exception as e:
        print(f"{team_name} {year} ❗ other exceptions: {e}")
        driver.quit()
    return None
    

all_winrates = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = []
    
    for team in team_abbr:
        for year in years:
            url = base_url + f"{team}/{year}.html"
            futures.append(executor.submit(fetch_win, url, team, year))
    
    for future in futures:
        result = future.result()
        if result:
            all_winrates.append(result)

df = pd.DataFrame(all_winrates)
df.to_csv('nba_winrates.csv', index=False)
print("✅ All win rates are stored to nba_winrates.csv")

driver.quit()