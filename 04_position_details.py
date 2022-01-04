from setup import *
from configure import *
from custom_funs import expand_date_format

report_date = sys.argv[1]
# report_date = "20210114"

report_name = "position_details"
start_row_num = 5
save_dir = os.path.join(OUTPUT_DIR, report_date[0:4], report_date)
check_and_mkdir(save_dir)

# --- load summary data
summary_file = "{}.summary.csv.gz".format(report_date)
summary_path = os.path.join(INTERMEDIARY_BY_DATE_DIR, report_date[0:4], summary_file)
summary_df = pd.read_csv(summary_path, encoding="gb18030")

# --- load report template
template_file = TEMPLATES_FILE_LIST[report_name]
template_path = os.path.join(TEMPLATES_DIR, template_file)
wb = xw.Book(template_path)
ws = wb.sheets["可转债"]
ws.range("A2").value = "统计日期：" + expand_date_format(report_date)

qty_sum = 0
cost_val_sum = 0
mkt_val_sum = 0
float_pnl_sum = 0
s = start_row_num
for ir in range(len(summary_df)):
    ws.range("A{}".format(s)).value = summary_df.at[ir, "chs_name"]
    ws.range("B{}".format(s)).value = summary_df.at[ir, "sid"]
    ws.range("C{}".format(s)).value = qty = summary_df.at[ir, "quantity"]
    ws.range("D{}".format(s)).value = summary_df.at[ir, "cost"]
    ws.range("E{}".format(s)).value = cost_val = summary_df.at[ir, "cost_val_tot"]
    ws.range("F{}".format(s)).value = summary_df.at[ir, "close"]
    ws.range("G{}".format(s)).value = mkt_val = summary_df.at[ir, "close_val_tot"]
    ws.range("H{}".format(s)).value = float_pnl = summary_df.at[ir, "close_val_tot"] - summary_df.at[ir, "cost_val_tot"]
    ws.range("I{}".format(s)).value = (summary_df.at[ir, "close_val_tot"] / summary_df.at[ir, "cost_val_tot"] - 1)

    # sum
    qty_sum += qty
    cost_val_sum += cost_val
    mkt_val_sum += mkt_val
    float_pnl_sum += float_pnl

    # for next
    s += 1
    ws.api.Rows(s).Insert()

# 合计
s += 2
ws.range("C{}".format(s)).value = qty_sum
ws.range("E{}".format(s)).value = cost_val_sum
ws.range("G{}".format(s)).value = mkt_val_sum
ws.range("H{}".format(s)).value = float_pnl_sum

# compared to prev year
realized_pnl_since_base = summary_df["realized_pnl_cum_since_base"].sum() / WAN_YUAN
unrealized_pnl_since_base = summary_df["unrealized_pnl_since_base"].sum() / WAN_YUAN
tot_pnl_since_base = summary_df["pnl_tot_since_base"].sum() / WAN_YUAN
pnl_sum_txt = "注：年初至今，实现盈利约{:.2f}万元，持仓盈亏{:.2f}万元，合计投资收益约{:.2f}万元。".format(
    np.round(realized_pnl_since_base, 2),
    np.round(unrealized_pnl_since_base, 2),
    np.round(tot_pnl_since_base, 2),
)
s += 1
ws.range("A{}".format(s)).value = pnl_sum_txt

# --- save as xlsx
save_file = template_file.replace("YYYYMMDD", report_date)
save_path = os.path.join(save_dir, save_file)
if os.path.exists(save_path):
    os.remove(save_path)
wb.save(save_path)
wb.close()
print("| {2} | {0} | {1} | generated |".format(report_name, save_file, dt.datetime.now()))
