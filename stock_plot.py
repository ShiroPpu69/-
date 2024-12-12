import pandas as pd
import matplotlib.pyplot as plt

# 设置matplotlib支持中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取数据
data_star50 = pd.read_excel('科创50.xlsx')
data_hushen300 = pd.read_excel('沪深300.xlsx')
data_shanghai = pd.read_excel('上证指数.xlsx')
# 将日期列转换为datetime格式
data_star50['日期Date'] = pd.to_datetime(data_star50['日期Date'], format='%Y%m%d', errors='coerce')
data_hushen300['日期Date'] = pd.to_datetime(data_hushen300['日期Date'], format='%Y%m%d', errors='coerce')
data_shanghai['日期Date'] = pd.to_datetime(data_shanghai['日期Date'], format='%Y%m%d', errors='coerce')
# 设置日期为索引
data_star50.set_index('日期Date', inplace=True)
data_hushen300.set_index('日期Date', inplace=True)
data_shanghai.set_index('日期Date', inplace=True)

# 绘制每日收盘价和成交金额折线图
plt.figure(figsize=(14, 6))

# 绘制每日收盘价折线图
plt.subplot(1, 2, 1)
plt.plot(data_shanghai.index, data_shanghai['收盘Close'], label='上证指数', color='blue')
plt.plot(data_star50.index, data_star50['收盘Close'], label='科创50指数', color='orange')
plt.plot(data_hushen300.index, data_hushen300['收盘Close'], label='沪深300指数', color='green')
plt.title('每日收盘价')
plt.xlabel('日期')
plt.ylabel('收盘价')
plt.legend()
plt.grid()

# 绘制每日成交金额折线图
plt.subplot(1, 2, 2)
plt.plot(data_shanghai.index, data_shanghai['成交金额（亿元）Turnover'], label='上证指数', color='blue')
plt.plot(data_star50.index, data_star50['成交金额（亿元）Turnover'], label='科创50指数', color='orange')
plt.plot(data_hushen300.index, data_hushen300['成交金额（亿元）Turnover'], label='沪深300指数', color='green')
plt.title('每日成交金额')
plt.xlabel('日期')
plt.ylabel('成交金额（亿元）')
plt.legend()
plt.grid()

plt.tight_layout()

# 绘制每月收盘价和成交金额的柱状图
data_shanghai_monthly = data_shanghai.resample('ME').last()
data_star50_monthly = data_star50.resample('ME').last()
data_hushen300_monthly = data_hushen300.resample('ME').last()

plt.figure(figsize=(14, 6))

# 绘制每月收盘价柱状图
plt.subplot(1, 2, 1)
plt.bar(data_shanghai_monthly.index, data_shanghai_monthly['收盘Close'], label='上证指数', color='blue', width=5)
plt.bar(data_star50_monthly.index, data_star50_monthly['收盘Close'], label='科创50指数', color='orange', width=5)
plt.bar(data_hushen300_monthly.index, data_hushen300_monthly['收盘Close'], label='沪深300指数', color='green', width=5)
plt.title('每月收盘价')
plt.xlabel('日期')
plt.ylabel('收盘价')
plt.legend()
plt.grid()

# 绘制每月成交金额柱状图
plt.subplot(1, 2, 2)
plt.bar(data_shanghai_monthly.index, data_shanghai_monthly['成交金额（亿元）Turnover'], label='上证指数', color='blue', width=5)
plt.bar(data_star50_monthly.index, data_star50_monthly['成交金额（亿元）Turnover'], label='科创50指数', color='orange', width=5)
plt.bar(data_hushen300_monthly.index, data_hushen300_monthly['成交金额（亿元）Turnover'], label='沪深300指数', color='green', width=5)
plt.title('每月成交金额')
plt.xlabel('日期')
plt.ylabel('成交金额（亿元）')
plt.legend()
plt.grid()


# 计算每月的最高价和最低价
data_star50_monthly = data_star50.resample('M').agg({'最高High': 'max', '最低Low': 'min'})
data_hushen300_monthly = data_hushen300.resample('M').agg({'最高High': 'max', '最低Low': 'min'})
data_shanghai_monthly = data_shanghai.resample('M').agg({'最高High': 'max', '最低Low': 'min'})

# 计算每月的波动幅度
data_star50_monthly['波动幅度'] = (data_star50_monthly['最高High'] - data_star50_monthly['最低Low']) / data_star50_monthly['最低Low']
data_hushen300_monthly['波动幅度'] = (data_hushen300_monthly['最高High'] - data_hushen300_monthly['最低Low']) / data_hushen300_monthly['最低Low']
data_shanghai_monthly['波动幅度'] = (data_shanghai_monthly['最高High'] - data_shanghai_monthly['最低Low']) / data_shanghai_monthly['最低Low']

# 绘制波动幅度图
plt.figure(figsize=(10, 6))
plt.plot(data_shanghai_monthly.index, data_shanghai_monthly['波动幅度'], label='上证指数', color='blue')
plt.plot(data_star50_monthly.index, data_star50_monthly['波动幅度'], label='科创50指数', color='orange')
plt.plot(data_hushen300_monthly.index, data_hushen300_monthly['波动幅度'], label='沪深300指数', color='green')
plt.title('每月波动幅度')
plt.xlabel('日期')
plt.ylabel('波动幅度')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()