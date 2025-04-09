import pandas as pd

# # 讀取原始 CSV 檔案
# input_file = "nba_winrates.csv"
# output_file = "nba_winrates_normalized.csv"

# # 使用 pandas 讀取 CSV 檔案
# df = pd.read_csv(input_file)

# #win_rate_normalize.py
# # 將 win_rate 欄位的值除以 82 並四捨五入到小數點後兩位
# # 確保 win_rate 欄位存在並進行計算
# # if "win_rate" in df.columns:
# #     # 將 win_rate 除以 82，新增一個 normalized_win_rate 欄位
# #     df["normalized_win_rate"] = (df["win_rate"] / 82).round(2)
# #     #將原始的欄位改成win_game
# #     df.rename(columns={"win_rate": "win_game"}, inplace=True)
# # else:
# #     print("win_rate 欄位不存在，請檢查檔案格式。")

# # # 將結果儲存為新的 CSV 檔案
# # df.to_csv(output_file, index=False)

# # print(f"已將 win_rate 正規化並儲存至 {output_file}")


# 確保 avg_ht 和 avg_wt 欄位存在
# 並計算其最小值和最大值
# 讀取 CSV 檔案
# input_file = "nba_rosters_full_data.csv"

# # 使用 pandas 讀取 CSV 檔案
# df = pd.read_csv(input_file)

# if "avg_ht" in df.columns and "avg_wt" in df.columns:
#     # 找出 avg_ht 的最小值和最大值
#     min_avg_ht = df["avg_ht"].min()
#     max_avg_ht = df["avg_ht"].max()

#     # 找出 avg_wt 的最小值和最大值
#     min_avg_wt = df["avg_wt"].min()
#     max_avg_wt = df["avg_wt"].max()

#     # 打印結果
#     print(f"avg_ht 最小值: {min_avg_ht}, 最大值: {max_avg_ht}")
#     print(f"avg_wt 最小值: {min_avg_wt}, 最大值: {max_avg_wt}")
# else:
#     print("avg_ht 或 avg_wt 欄位不存在，請檢查檔案格式。")

# import pandas as pd

# # 讀取 CSV 檔案
# input_file = "nba_rosters_full_data.csv"

# # 使用 pandas 讀取 CSV 檔案
# df = pd.read_csv(input_file)

# # 確保必要的欄位存在
# if "team" in df.columns and "year" in df.columns and "avg_ht" in df.columns:
#     # 過濾 1990 到 2025 年的數據
#     filtered_df = df[(df["year"] >= 1990) & (df["year"] <= 2025)]

#     # 計算每支隊伍的 avg_ht 最大值和最小值
#     team_ht_changes = (
#         filtered_df.groupby("team")["avg_ht"]
#         .agg(["max", "min"])
#         .reset_index()
#     )
#     team_ht_changes["change"] = team_ht_changes["max"] - team_ht_changes["min"]

#     # 找出變化最多的四支隊伍
#     top_teams = team_ht_changes.nlargest(4, "change")

#     # 打印結果
#     print("1990 到 2025 年 avg_ht 變化最多的四支隊伍：")
#     print(top_teams[["team", "change"]])
# else:
#     print("必要的欄位不存在，請檢查檔案格式。")




import pandas as pd

# 讀取 CSV 檔案
input_file = "nba_rosters_full_data.csv"

# 使用 pandas 讀取 CSV 檔案
df = pd.read_csv(input_file)

# 確保必要的欄位存在
if "team" in df.columns and "year" in df.columns and "avg_wt" in df.columns:
    # 過濾 1990 到 2025 年的數據
    filtered_df = df[(df["year"] >= 1990) & (df["year"] <= 2025)]

    # 計算每支隊伍的 avg_wt 最大值和最小值
    team_wt_changes = (
        filtered_df.groupby("team")["avg_wt"]
        .agg(["max", "min"])
        .reset_index()
    )
    team_wt_changes["change"] = team_wt_changes["max"] - team_wt_changes["min"]

    # 找出變化最多的四支隊伍
    top_teams = team_wt_changes.nlargest(4, "change")

    # 打印結果
    print("1990 到 2025 年 avg_wt 變化最多的四支隊伍：")
    print(top_teams[["team", "change"]])
else:
    print("必要的欄位不存在，請檢查檔案格式。")