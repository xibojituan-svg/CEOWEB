import pandas as pd
import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

path = '/Users/jiangdeming/Documents/work/Financial/喜播商品每日营收及退款数据（含线下录入数据）_商品维度每日统计_20260304_1744.xlsx'
df = pd.read_excel(path)

# Ensure columns exist and handle NaNs
df['当日营收'] = df['当日营收'].fillna(0)
df['当日退费金额'] = df['当日退费金额'].fillna(0)
df['date'] = df['下单时间/退款时间'].astype(str)

# Daily trend
daily_summary = df.groupby('date').agg({'当日营收': 'sum', '当日退费金额': 'sum'}).sort_index().reset_index()
daily_list = daily_summary.to_dict('records')

# SKU breakdown (Total for the period)
sku_summary = df.groupby(['商品名称', '产品线']).agg({'当日营收': 'sum', '当日退费金额': 'sum'}).reset_index()
top_skus = sku_summary.sort_values(by='当日营收', ascending=False).head(20).to_dict(orient='records')

# Product Line breakdown
line_summary = df.groupby(['产品线']).agg({'当日营收': 'sum'}).reset_index().sort_values('当日营收', ascending=False)
line_list = line_summary.to_dict('records')

data = {
    'daily': daily_list,
    'skus': top_skus,
    'lines': line_list,
    'total_revenue': float(df['当日营收'].sum()),
    'total_refund': float(df['当日退费金额'].sum()),
    'update_time': '2026-03-04 17:44'
}

with open('/Users/jiangdeming/Documents/work/Financial/revenue_summary.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, cls=NpEncoder, ensure_ascii=False, indent=2)

print("Data processing complete. Saved to revenue_summary.json")
