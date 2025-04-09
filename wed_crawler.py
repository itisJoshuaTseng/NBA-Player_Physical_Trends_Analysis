from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os

# NBA 球隊的 ESPN 網址列表
team_urls = {
    "Dallas Mavericks": "https://www.espn.com/nba/team/roster/_/name/dal/dallas-mavericks",
    "Golden State Warriors": "https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors",
    "Houston Rockets": "https://www.espn.com/nba/team/roster/_/name/hou/houston-rockets",
    "Memphis Grizzlies": "https://www.espn.com/nba/team/roster/_/name/mem/memphis-grizzlies",
    "Oklahoma City Thunder": "https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder",
    "Minnesota Timberwolves": "https://www.espn.com/nba/team/roster/_/name/min/minnesota-timberwolves",
    "Denver Nuggets": "https://www.espn.com/nba/team/roster/_/name/den/denver-nuggets",
    "Los Angeles Lakers": "https://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers",
    "LA Clippers": "https://www.espn.com/nba/team/roster/_/name/lac/la-clippers",
    "Sacramento Kings": "https://www.espn.com/nba/team/roster/_/name/sac/sacramento-kings",
    "Phoenix Suns": "https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns", 
    "Portland Trail Blazers": "https://www.espn.com/nba/team/roster/_/name/por/portland-trail-blazers",    
}
# Selenium settings
driver = webdriver.Chrome()
# full url: baseurl + team_abbr + / + year + .html
team_abbr =  ["OKC", "HOU", "DEN", "MEM", "LAL", "GSW", "MIN", "LAC", "SAC", "DAL", "PHO", "POR"]
base_url = 'https://www.basketball-reference.com/teams/'
base_folder = "nba_rosters"
years = [i for i in range(1990, 2026)]
# 下載並存儲多個球隊的數據
def fetch_and_save_roster(url, team_name, year):
    try:
        driver.get(url)
        tbl = driver.find_element(By.ID, "div_roster").get_attribute("outerHTML")
        dfs = pd.read_html(tbl)
        if dfs:
            df = dfs[0]
            folder = team_name
            file_name = f"{base_folder}/{team_name}/{team_name}_{year}.csv"
            df.to_csv(file_name, index=False)
            print(f"{team_name} 名單已儲存至 {file_name}")
            return df
    except Exception as e:
        print(f"無法抓取 {team_name} 的數據: {e}")
    return None

# 存儲所有球隊的 DataFrame
dfs = []
for team in team_abbr:
    if team != 'PHO': continue
    if not os.path.exists(f"{base_folder}/{team}"):
        os.makedirs(f"{base_folder}/{team}")
    for year in years:
        if (team == 'OKC' and year < 2009 )or (team == 'MEN' and year < 2002): 
            continue
        df = fetch_and_save_roster(base_url+team+'/'+str(year)+'.html', team, year)
        time.sleep(10)
        if df is not None:
            dfs.append(df)


# 合併所有球隊的數據
if dfs:
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv("nba_combined_rosters.csv", index=False)
    print("所有球隊數據已合併儲存至 nba_combined_rosters.csv")
