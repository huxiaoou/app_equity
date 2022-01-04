from setup import *
from configure import *

report_date = sys.argv[1]
# report_date = "20210114"

#  main loop
summary_data_list = []
for sid in TRACKING_SID_LIST:
    sid_details_file = "details.{}.xlsx".format(sid)
    sid_details_path = os.path.join(INTERMEDIARY_BY_SID_DIR, sid_details_file)
    sid_details_df = pd.read_excel(sid_details_path)
    sid_details_df["trade_date"] = sid_details_df["日期"].map(lambda z: z.strftime("%Y%m%d"))
    sid_details_df = sid_details_df.set_index("trade_date")

    if report_date in sid_details_df.index:
        sid_data = {
            "sid": sid,
            "chs_name": SID_INFO.get(sid).get("CHS_NAME"),
            "quantity": sid_details_df.at[report_date, "期末数量"],
            "cost": sid_details_df.at[report_date, "期末成本"],
            "cost_val_tot": sid_details_df.at[report_date, "期末成本总值"],
            "close": sid_details_df.at[report_date, "收盘价格"],
            "close_val_tot": sid_details_df.at[report_date, "期末市场总值"],

            "unrealized_pnl": sid_details_df.at[report_date, "浮动盈亏"],
            "realized_pnl": sid_details_df.at[report_date, "实现盈亏"],
            "realized_pnl_cum": sid_details_df.at[report_date, "累积实现盈亏"],
            "pnl_tot": sid_details_df.at[report_date, "累积总盈亏"],

            "unrealized_pnl_since_base": sid_details_df.at[report_date, "浮动盈亏"] - sid_details_df.at[BASE_YEAR_DATE, "浮动盈亏"],
            "realized_pnl_cum_since_base": sid_details_df.at[report_date, "累积实现盈亏"] - sid_details_df.at[BASE_YEAR_DATE, "累积实现盈亏"],
            "pnl_tot_since_base": sid_details_df.at[report_date, "累积总盈亏"] - sid_details_df.at[BASE_YEAR_DATE, "累积总盈亏"],
        }
        summary_data_list.append(sid_data)
    else:
        print("| {} | {} | {} | data are not found, please check details data again |".format(dt.datetime.now(), report_date, sid))

summary_df = pd.DataFrame(summary_data_list)
summary_file = "{}.summary.csv.gz".format(report_date)
summary_path = os.path.join(INTERMEDIARY_BY_DATE_DIR, report_date[0:4], summary_file)
summary_df.to_csv(summary_path, index=False, float_format="%.6f", compression="gzip", encoding="gb18030")
print("| {} | {} | data summarized |".format(dt.datetime.now(), report_date))
