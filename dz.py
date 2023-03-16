# gg = ([1,2,3],4)
# ff = gg[1]
# dd = gg[0]
# fff = 0
# fdd = 0
# f = 0
# g = 0
# for gf in range(0, 3):
#     fff = dd[gf]
#     for fd in range(0, 3):
#         fdd = dd[fd]
#         if fff + fdd == ff:
#             fs = dd.index(fff)
#             ad = dd.index(fdd)
#             print([fs, ad])

def dreff(sl, os, ts):
    f = 0
    fd = ""
    h = 0
    for gg in sl:
        f = f + 1
        if gg == os:
            break
    for hb in sl:
        h = h + 1
        if hb == ts:
            break
    fd = sl[f:h-1]
    print(fd)
    
dreff("пель(ме)ни", "(", ")")