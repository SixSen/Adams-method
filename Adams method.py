# 阿当姆斯法
def f(ex, ey):
    return -ey + ex + 1


N = 11      # 求解次数
h = 0.1     # 步长
y = 1       # y(0)的值为0


def init(y0):
    n = 0
    x0 = 0
    ret = []
    while 3 > n:
        x1 = x0 + h
        k1 = f(x0, y0)
        k2 = f(x0 + h / 2, y0 + (h / 2) * k1)
        k3 = f(x0 + h / 2, y0 + (h / 2) * k2)
        k4 = f(x1, y0 + h * k3)
        y1 = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        print("x{0}={1:0.1f}\t\t\t y{0}={2:0.6f}".format(n+1, x1, y1))
        ret.append(y1)
        n = n + 1
        x0 = x1
        y0 = y1
    return ret


re = init(y)
ya = re[0]
yb = re[1]
yc = re[2]
i = 3
while i < N:
    x = i * h
    yex = yc + (h / 24) * (55 * f(x, yc) - 59 * f(x-h, yb) + 37*f(x-2*h, ya) - 9*f(x-3*h, y))
    yim = yc + (h / 24) * (9 * f(x, yex) + 19 * f(x - h, yc) - 5 * f(x - 2 * h, yb) + f(x - 3 * h, ya))
    print("x{0}={1:0.1f}\t 显式：y{0}={2:0.6f}\t 隐式：y{0}={3:0.6f}".format(i, x, yex, yim))
    y = ya
    ya = yb
    yb = yc
    yc = yim
    i = i + 1

