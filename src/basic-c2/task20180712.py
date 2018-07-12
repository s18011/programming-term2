for x in range(1, 10):
    str_line = ""
    for y in range(1, 10):
        ans_int = x * y
        ans_str = str(ans_int)
        ans_str = ans_str.rjust(3)
        str_line = str_line + ans_str
    print(str_line)
    print()
