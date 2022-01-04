ACCOUNT_ID = "1001000016"
PERMISSION_CODE = "根据公司资产配置安排"

TEMPLATES_FILE_LIST = {
    "input_order_inside": "00_交易指令单_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
    "input_order_outside": "01_投资管理总部交易指令单_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
    "traded_order": "02_当日成交_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
    "traded_order_summary": "03_当日成交汇总_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
    "position_details": "04_持仓情况明细表_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
    "pnl_summary": "05_盈亏情况明细表_股票可转债_{}_YYYYMMDD.xlsx".format(ACCOUNT_ID),
}

TRACKING_SID_LIST = ["002074.SZ"]

WAN_YUAN = 1e4
# BASE_YEAR_DATE = "20201231"  # change it when new year has come
BASE_YEAR_DATE = "20211231"  # change it when new year has come

SID_INFO = {
    "002074.SZ": {"CHS_NAME": "国轩高科"},
}

EXCHANGE_MAPPER = {
    "SZ": "深圳证券交易所",
    "SH": "上海证券交易所",
}
