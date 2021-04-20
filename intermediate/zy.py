import sqlite3


def split_value(day_rang, idx):
    arr = [x for x in day_rang.split(" - ")]
    return arr[idx]


def replace_vol(str_vol):
    if 'M' in str_vol:
        return float(str_vol.replace('M', '0000').replace('.', ''))
    if 'K' in str_vol:
        return float(vol_k.replace('K', '0').replace('.', ''))


vol_m = '65.72M'  # 65720000
vol_k = '675.08K'  # 675080

# print(replace_vol(vol_k))

print(sqlite3.sqlite_version)
