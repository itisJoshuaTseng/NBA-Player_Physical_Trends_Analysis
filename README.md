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

## 🧠 Conclusion

Although it is commonly believed that the NBA has become shorter in recent years due to the rise of faster-paced, small-ball playstyles, our data analysis reveals a more nuanced explanation. The decline in average player height during the mid-2010s coincides with the dominance of **Stephen Curry** and the Golden State Warriors, whose success popularized guard-heavy lineups and perimeter shooting. This era temporarily pulled average heights downward.

However, this trend is not strictly chronological. In earlier decades, the league was shaped by legendary centers such as **Shaquille O’Neal**, **Hakeem Olajuwon**, **David Robinson**, and **Patrick Ewing**—all towering at or above **213 cm**—who defined the game from the paint. In recent seasons, the resurgence of dominant big men like **Nikola Jokić** has renewed the league’s emphasis on interior presence, contributing to a rebound in average height.

> In conclusion, average player height in the NBA does not steadily decline or rise with time.  
> Instead, it reflects the influence of **era-defining superstars** who reshape how the game is played.

