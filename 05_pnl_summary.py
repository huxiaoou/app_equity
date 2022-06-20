from setup import *
from configure import *
from custom_funs import expand_date_format

report_date = sys.argv[1]
# report_date = "20210114"

report_name = "pnl_summary"
start_row_num = 4
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

# --- update template
ws.range("A2").value = "日期：" + expand_date_format(report_date)
for s in range(start_row_num, start_row_num + 2):
    ws.range("B{}".format(s)).value = summary_df["quantity"].sum()
    ws.range("C{}".format(s)).value = summary_df["close_val_tot"].sum() / WAN_YUAN
    ws.range("D{}".format(s)).value = summary_df["unrealized_pnl_since_base"].sum() / WAN_YUAN
    ws.range("E{}".format(s)).value = summary_df["realized_pnl_cum_since_base"].sum() / WAN_YUAN
    ws.range("F{}".format(s)).value = summary_df["pnl_tot_since_base"].sum() / WAN_YUAN

# --- save as xlsx
save_file = template_file.replace("YYYYMMDD", report_date)
save_path = os.path.join(save_dir, save_file)
if os.path.exists(save_path):
    os.remove(save_path)
wb.save(save_path)
wb.close()
sleep(3)
print("| {2} | {0} | {1} | generated |".format(report_name, save_file, dt.datetime.now()))
