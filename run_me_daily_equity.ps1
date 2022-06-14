$trade_date = Get-Date -Format "yyyyMMdd"
python aux_intermediary.py $trade_date
python 03_traded_order_summary.py $trade_date
python 04_position_details.py $trade_date
python 05_pnl_summary.py $trade_date
Pause
