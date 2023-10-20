"""
给你四个整数 length ，width ，height 和 mass ，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 类别 的字符串。

如果满足以下条件，那么箱子是 "Bulky" 的：
箱子 至少有一个 维度大于等于 104 。
或者箱子的 体积 大于等于 109 。
如果箱子的质量大于等于 100 ，那么箱子是 "Heavy" 的。
如果箱子同时是 "Bulky" 和 "Heavy" ，那么返回类别为 "Both" 。
如果箱子既不是 "Bulky" ，也不是 "Heavy" ，那么返回类别为 "Neither" 。
如果箱子是 "Bulky" 但不是 "Heavy" ，那么返回类别为 "Bulky" 。
如果箱子是 "Heavy" 但不是 "Bulky" ，那么返回类别为 "Heavy" 。
注意，箱子的体积等于箱子的长度、宽度和高度的乘积。

 
"""

def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        """
        bulky：
            1.至少一维度 >= 10^4
            2.体积 >= 10^9
        Heavy：
            1.mass >= 100
        """
        bulky_L = 10**4
        bulky_V = 10**9
        box_Vol = length * width * height
        is_bukly = False
        is_heavy = False
        # if length >= bulky_L or width >= bulky_L or height >= bulky_L \
        #  or box_Vol >= bulky_V
        if length|width|height >= bulky_L or box_Vol >= bulky_V:
            is_bukly = True
        if mass >= 100:
            is_heavy = True
        
        if is_bukly and is_heavy:
            return "Both"
        elif not is_bukly and not is_heavy:
            return "Neither"
        else:
            return "Bulky" if is_bukly else "Heavy"