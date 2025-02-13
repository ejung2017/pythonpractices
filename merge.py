import pandas as pd

left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
result = pd.merge(right, left, on="key")
#   key   C   D   A   B
# 0  K0  C0  D0  A0  B0
# 1  K1  C1  D1  A1  B1
# 2  K2  C2  D2  A2  B2
# 3  K3  C3  D3  A3  B3
print(result)

result = pd.merge(left, right, on="key")
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3
print(result)

#결론: .merge(맨 왼쪽에 오는 데이타프레임, 그 오른쪽에 오는 것, on="기준 컬럼")

##########################################################
left = pd.DataFrame(
   {
      "key1": ["K0", "K0", "K1", "K2"],
      "key2": ["K0", "K1", "K0", "K1"],
      "A": ["A0", "A1", "A2", "A3"],
      "B": ["B0", "B1", "B2", "B3"],
   }
)


right = pd.DataFrame(
   {
      "key1": ["K0", "K1", "K1", "K2"],
      "key2": ["K0", "K0", "K0", "K0"],
      "C": ["C0", "C1", "C2", "C3"],
      "D": ["D0", "D1", "D2", "D3"],
   }
)

result = pd.merge(left, right, how="right", on=["key1", "key2"])
                                #how="right" --> use keys from right frame only
#   key1 key2    A    B   C   D
# 0   K0   K0   A0   B0  C0  D0
# 1   K1   K0   A2   B2  C1  D1
# 2   K1   K0   A2   B2  C2  D2
# 3   K2   K0  NaN  NaN  C3  D3
print(result)

result = pd.merge(left, right, how="outer", on=["key1", "key2"])
                                #'outer' --> union of keys 
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K0   K1   A1   B1  NaN  NaN
# 2   K1   K0   A2   B2   C1   D1
# 3   K1   K0   A2   B2   C2   D2
# 4   K2   K0  NaN  NaN   C3   D3
# 5   K2   K1   A3   B3  NaN  NaN
print(result)