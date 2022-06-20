import os
import sys
import datetime as dt
import numpy as np
import pandas as pd
from skyrim.winterhold import check_and_mkdir
from skyrim.whiterun import CCalendar
import xlwings as xw
from time import sleep

pd.set_option("display.width", 0)
pd.set_option("display.float_format", "{:.2f}".format)

SEP_LINE = "=" * 120

INPUT_DIR = os.path.join("E:\\", "Works", "Trade", "Reports_Equity", "input")
OUTPUT_DIR = os.path.join("E:\\", "Works", "Trade", "Reports_Equity", "output")
TEMPLATES_DIR = os.path.join("E:\\", "Works", "Trade", "Reports_Equity", "templates")
INTERMEDIARY_DIR = os.path.join("E:\\", "Works", "Trade", "Reports_Equity", "intermediary")
INTERMEDIARY_BY_SID_DIR = os.path.join(INTERMEDIARY_DIR, "by_sid")
INTERMEDIARY_BY_DATE_DIR = os.path.join(INTERMEDIARY_DIR, "by_date")
