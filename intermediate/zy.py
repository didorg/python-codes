def split_value(day_rang, idx):
    arr = [x for x in day_rang.split(" - ")]
    return arr[idx]



day_rang = '133.34 - 135.47'

low = split_value(day_rang, 0)
high = split_value(day_rang, 1)
vol = '68,710,681'
result = vol.replace(',', '')
fl = float(result)
print(fl)
print(type(fl))



