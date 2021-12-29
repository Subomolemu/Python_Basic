def analog_zip(object_1, object_2):
    desired_length = min(len(date_1), len(date_2))
    tpl = [(object_1[sym], object_2[sym])
           for i, sym in enumerate(range(desired_length))]
    return tpl


date_1 = '312'
date_2 = ('a', 'b', 12, 22)

print(analog_zip(date_1, date_2))
