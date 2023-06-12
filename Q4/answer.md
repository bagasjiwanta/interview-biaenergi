# Question #4 (performance)

The following method will find the intersection (duplicates) of two given sets.

CODE:

```py
def intersect(bagA, bagB):
    result = []
    for o in bagA:
        if o in bagB:
            result.append(o)
    return result
```

QUESTIONS:

What would be the effect on performance in these two cases:
| | bagA | bagB |
| ----- | --- | --- |
| Case 1 | Has LARGE number of elements | Has SMALL number of elements |
| Case 2 | Has SMALL number of elements | Has LARGE number of elements |

Do you have any recommendations to improve the performance? Feel free to change the above method.

Time complexity analysis:

| Operation          | Average Case   | Worst Case     |
| ------------------ | -------------- | -------------- |
| `for o in bagA`    | `O(len(bagA))` | `O(len(bagA))` |
| `if o in bagB`     | `O(1)`         | `O(len(bagB))` |
| `result.append(o)` | `O(1)`         | `O(1)`         |

In conclusion, this function's time complexity is:

| Average Case     | Worst Case                 |
| ---------------- | -------------------------- |
| `pyO(len(bagA))` | `O(len(bagA) * len(bagB))` |

if the terms SMALL and LARGE has an enormous difference, case 2 will always be faster than case 1 significantly.

To improve perfomance, we can use python's native `set.intersection()` function (which has similar time complexity) or we can add control flow to switch the bags

Variation 1:

```py
def intersect_v2(bagA: set, bagB: set) -> list:
    return list(set.intersection(bagA, bagB))
```

Variation 2:

```py
def intersect_v3(bagA: set, bagB: set) -> list:
    result = []
    if len(bagA) > len(bagB):
        [bagA, bagB] = [bagB, bagA]

    for o in bagA:
        if o in bagB:
            result.append(o)

    return result
```
