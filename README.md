# 🏀 NBA Player Physical Trends Analysis

This project analyzes the **average height** and **average weight** trends of selected NBA teams over time, focusing on key shifts like the rise of small ball in 2015. It visualizes player physique changes and fits **linear regression lines** to capture long-term trends.

## 📁 Dataset

- File: `nba_rosters_full_data.csv`
- Contains player-level roster data across multiple NBA seasons.
- Fields used: `year`, `team`, `avg_wt`, `avg_ht`

## 📊 Analysis Highlights

### ✅ Weight Trend
- Selected Teams: `GSW`, `PHO`, `DEN`, `LAC`
- Computed 3-year rolling average weight per team.
- Plotted team trends alongside **league average weight**.
- Added **linear regression line** to league average to show trend over time.
- Marked **2015** as a key moment when the Golden State Warriors won the championship and popularized the small-ball strategy.

### ✅ Height Trend
- Selected Teams: `DAL`, `LAL`, `GSW`, `HOU`
- Similar 3-year rolling average and league average analysis for height.
- Added a **linear regression line** to capture long-term height trends.

## 📈 Visualizations

All plots are generated using **Matplotlib**, with distinct colors for each team and clear labeling:

- Smoothed lines for each team (rolling average)
- Black dashed line for league average
- Red dotted line for trend (regression line)
- Vertical marker for significant historical events (e.g., 2015 GSW championship)
