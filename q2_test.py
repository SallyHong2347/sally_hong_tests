import q2


extreme_long1 = "555555555555555555555555555555555555555555555555555555555555"
extreme_long2 = "5"*(len(extreme_long1) - 1) + "3"
neg_long1 = "-93204839253203492"
long_float1 = "44444444444444444444.4444444444444"
long_float2 = long_float1 + "1"
neg_long_float = "-" + long_float1


test_cases = [
    (extreme_long1, extreme_long2, 1),
    (long_float1, long_float2, -1),
    ("-44444444444444444444.4444444444444444444444444444444444444", "-1.9", -1),
    (neg_long_float, "1", -1),
    (neg_long_float, neg_long1, -1),
    (neg_long1, neg_long1, 0),
    ("23.532", "-9.532", 1),
    ("-324", "12", -1),
    ("-0.", "0", 0)

]

for s1, s2, answer in test_cases:
    try:
        result = q2.CompStrVal(s1, s2)
        assert result == answer, f"expected {answer}, but got {result}"
    except Exception as e:
        print(f"An error occurred for {s1} and {s2}: {e}")
    else:
        print("test passes")


