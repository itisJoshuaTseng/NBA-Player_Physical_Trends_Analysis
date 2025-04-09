import pandas as pd
import os

# 依照指定順序列出要讀取的球隊 CSV 檔案
team_order = [
    "oklahoma_city_thunder.csv",
    "houston_rockets.csv",
    "denver_nuggets.csv",
    "memphis_grizzlies.csv",
    "los_angeles_lakers.csv",
    "golden_state_warriors.csv",
    "minnesota_timberwolves.csv",
    "la_clippers.csv",
    "sacramento_kings.csv",
    "dallas_mavericks.csv",
    "phoenix_suns.csv",
    "portland_trail_blazers.csv"
]

# 對應每支球隊的勝率
win_percentages = [0.83, 0.63, 0.63, 0.63, 0.62, 0.58, 0.58, 0.55, 0.50, 0.48, 0.46, 0.43]

# 處理體重欄位：去掉 " lbs" 字串並轉換為整數，回傳平均體重
def process_weight_column(df):
    try:
        df.iloc[:, 5] = df.iloc[:, 5].str.replace(" lbs", "").astype(int)
        return df.iloc[:, 5].mean()
    except Exception as e:
        print(f"處理體重數據時發生錯誤: {e}")
        return None

# 將身高（例如 6'7"）轉換為公分
def height_to_cm(height):
    try:
        feet, inches = height.split("'")
        feet = int(feet.strip())
        inches = int(inches.replace('"', '').strip())
        return (feet * 12 + inches) * 2.54
    except:
        return None

data_records = []  # 儲存每支球隊的統計資料
max_columns = 4    # 初始最小欄位數（隊名、平均身高、平均體重、勝率）

# 依序處理每支球隊的資料
for i, file in enumerate(team_order):
    if not os.path.exists(file):
        print(f"檔案 {file} 不存在，跳過。")
        continue
    
    df = pd.read_csv(file)  # 讀取 CSV 檔案
    df.rename(columns={df.columns[0]: "Index"}, inplace=True)  # 將第一欄重新命名為 Index
    team_name = file.replace(".csv", "").replace("_", " ").title()  # 產生隊名，例如 Oklahoma City Thunder

    avg_weight = process_weight_column(df)  # 計算平均體重
    df["Height_cm"] = df.iloc[:, 4].apply(height_to_cm)  # 將身高轉換為公分並新增欄位
    avg_height = df["Height_cm"].mean()  # 計算平均身高

    # 取得勝率，若超過提供的勝率數量則設定為 None
    win_percentage = win_percentages[i] if i < len(win_percentages) else None

    # 組合球隊的基本資料
    team_record = [team_name, avg_height, avg_weight, win_percentage]

    # 加入每位球員的身高與體重資料
    for index, row in df.iterrows():
        team_record.append(row["Height_cm"])
        team_record.append(row.iloc[5])  # 第 6 欄為處理過的體重欄

    # 更新最大欄位數（為了確保所有球隊資料對齊）
    max_columns = max(max_columns, len(team_record))
    data_records.append(team_record)

# 將每筆球隊資料補齊到相同欄位數，缺值用 None 補上
for record in data_records:
    while len(record) < max_columns:
        record.append(None)

# 建立欄位名稱（前四欄固定，後續依球員數生成）
columns = ["Team Name", "Avg Height (cm)", "Avg Weight (lbs)", "Win Percentage"]
for i in range((max_columns - 4) // 2):
    columns.append(f"Player_{i+1}_Height_cm")
    columns.append(f"Player_{i+1}_Weight_lbs")

# 建立最終的 DataFrame 並輸出成 CSV 檔
output_df = pd.DataFrame(data_records, columns=columns)
output_df.to_csv("nba_team_summary.csv", index=False)

print("所有數據已存入 nba_team_summary.csv，並新增勝率欄位")
