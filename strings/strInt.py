class Solution:
    def myAtoi(self, str: str) -> int:
        if str == "":
            return 0
        str = str.strip()
        str_ = ""
        i = 0
        flag = 0
        minus_count = 0
        plus_count = 0
        if str == "":
            return 0
        j = 0
        while str != "" and (str[i] == "+"or str[i] == "-"):

            if str[i] == "-":
                minus_count = minus_count+1
            str = str[1:]
            j = j+1
        if j > 1:
            return 0
        if minus_count % 2 != 0:
            flag = 1

        if str == "":
            return 0
        if not str[0].isdigit():
            return 0
        else:

            while i < len(str) and str[i].isdigit():
                str_ = str_+str[i]
                i = i+1
            int_str = int(str_)
            if int_str > 2147483647:
                if flag != 0:
                    return 2147483648*(-1*flag)
                else:
                    return 2147483647

            else:
                if flag != 0:
                    return int_str*(-1*flag)
                else:
                    return int_str
