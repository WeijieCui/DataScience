import math

import numpy as np


def entropy(classes):
    cmap = {}
    result_string = ''
    for c in classes:
        if c in cmap:
            cmap[c] += 1
        else:
            cmap.setdefault(c, 1)
    t = len(classes)
    tmp = []
    for k, v in cmap.items():
        tmp.append(-v / t * math.log(v / t, 2))
        result_string += f'[{k}] -{v}/{t}*log({v}/{t})'
    result_string2 = '+'.join(str(i) for i in tmp)
    result = sum(tmp)
    return result_string, result_string2, result


def entropy_sub(data, class_column, attributes, es_val):
    t = len(data)
    best_gain, best_attr = -1, None
    for attr in attributes:
        print(f'Entropy col_{attr} = ', end='')
        amap = {}
        esas = []
        for v in data[attr]:
            if v in amap:
                amap[v] += 1
            else:
                amap.setdefault(v, 1)

        for a, count in amap.items():
            data_a = data[data[attr] == a]
            esa_s1, esa_s2, esa_val = entropy(data_a[class_column])
            print(f'{count}/ {t} * ({esa_s1}) + ', end='')
            esas.append((count, esa_val))
        esa_sum = 0
        print('=', end='')
        for count, esa_val in esas:
            print(f'{count}/{t}*{esa_val} + ', end='')
            esa_sum += count / t * esa_val
        print(f'={esa_sum}')
        gain = es_val - esa_sum
        best_gain, best_attr = (best_gain, best_attr) if gain <= best_gain else (gain, attr)
        print(f'Gain col_{attr}: {gain}')
    return best_attr


def entropy_iter(data, class_column, attributes):
    print(data)
    es_s1, es_s2, es_val = entropy(data[class_column])
    print(f'entropy start: {es_s1}={es_s2}={es_val}')
    best_attr = entropy_sub(data, class_column, attributes, es_val)
    new_attributes = [a for a in attributes if a != best_attr]
    if new_attributes:
        for val in set(data[best_attr]):
            print(f'************Attr_{best_attr}:{val}******************')
            entropy_iter(data[data[best_attr] == val], class_column, new_attributes)


def test():
    data = np.array([
        ('yes', 'yes', 'yes', 3),  # 0
        ('yes', 'yes', 'no', 2),
        ('yes', 'no', 'yes', 3),
        ('yes', 'no', 'no', 1),
        ('no', 'yes', 'yes', 3),  # 4
        ('no', 'yes', 'no', 2),
        ('no', 'no', 'yes', 3),
        ('no', 'no', 'no', 1),
    ], dtype=[('A', 'U10'), ('B', 'U10'), ('C', 'U10'), ('Class', 'i4')])
    class_column = 'Class'
    attributes = ['A', 'B', 'C']
    entropy_iter(data, class_column, attributes)


if __name__ == '__main__':
    test()
