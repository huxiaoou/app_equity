set trade_date=%date:~0,4%%date:~5,2%%date:~8,2%
python aux_intermediary.py %trade_date%
python 03_traded_order_summary.py %trade_date%
python 04_position_details.py %trade_date%
python 05_pnl_summary.py %trade_date%
pause
