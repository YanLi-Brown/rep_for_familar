import copy

src = [[1], [2]]
shallow = src.copy()           # 只复制最外层列表
deep = copy.deepcopy(src)      # 递归复制内部对象

shallow[0].append(9)
print(src)                     # [[1, 9], [2]]
print(deep)                    # [[1], [2]]
