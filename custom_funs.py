def expand_date_format(x: str) -> str:
    return "{}-{}-{}".format(x[0:4], x[4:6], x[6:8])
