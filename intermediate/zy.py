def split_value(day_rang, idx):
    arr = [x for x in day_rang.split(" - ")]
    return arr[idx]


def replace_vol(str_vol):
    arr = str_vol.split(".")
    digits = len(arr[1])
    if 'M' in arr[1]:
        if digits == 4:
            return float(str_vol.replace('.', '').replace('M', '000'))
        if digits == 3:
            return float(str_vol.replace('.', '').replace('M', '0000'))
        if digits == 2:
            return float(str_vol.replace('.', '').replace('M', '00000'))
    elif 'K' in arr[1]:
        if digits == 3:
            return float(str_vol.replace('.', '').replace('K', '0'))
        if digits == 2:
            return float(str_vol.replace('.', '').replace('K', '00'))
    else:
        if digits == 2:
            return float(str_vol.replace('.', '') + '0')
        if digits == 1:
            return float(str_vol.replace('.', '') + '00')


vol_m = '28.03M'  # 28 030 109
vol_k = '675.08K'  # 675 080
vol_k1 = '25.7K'  # 25 700

vol_1 = '675.08'  # 675 080
vol_2 = '25.7'  # 25 700

print(replace_vol(vol_2))
