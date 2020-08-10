"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
# 定义从-pi到pi之间的数据，平均取64个数据点
x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)

# 将绘图区域分成2行3列
gs = gridspec.GridSpec(2, 3)
# 指定ax1占用第一行（0）整行
ax1 = plt.subplot(gs[0, :])
# 指定ax1占用第二行（1）的第一格（第二个参数0代表）
ax2 = plt.subplot(gs[1, 0])
# 指定ax1占用第二行（1）的第二、三格（第二个参数0代表）
ax3 = plt.subplot(gs[1, 1:3])

# 绘制正弦曲线
ax1.plot(x_data, np.sin(x_data))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')

# 绘制余弦曲线
ax2.plot(x_data, np.cos(x_data))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('余弦曲线')

# 绘制正切曲线
ax3.plot(x_data, np.tan(x_data))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')

# plt.show()


from IPy import IP
# 通过strNormal方法指定不同wantprefixlen参数值制定不同输出类型的网段
# 输出类型为字符串
IP('192.168.100.0/24').strNormal(0)
IP('192.168.100.0/24').strNormal(1)
IP('192.168.100.0/24').strNormal(2)
IP('192.168.100.0/24').strNormal(3)
# print(help(IP))

import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(-np.pi, np.pi, 0.1)

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), label='line1')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title("sin")

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), label='line2')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title("cos")

plt.subplot(2, 1, 2)
plt.plot(x, np.tan(x), label='line3')
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().spines['bottom'].set_position(('data', 0))
plt.gca().spines['left'].set_position(('data', 0))
plt.title("tan")

plt.show()

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

plt.figure()
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(-np.pi, np.pi, 0.1)

gs = gridspec.GridSpec(2, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0])
ax3 = plt.subplot(gs[1, 1:3])

# 绘制正弦曲线
ax1.plot(x, np.sin(x))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.set_title('正弦曲线')
ax1.set_title('sin')

# 绘制余弦曲线
ax2.plot(x, np.cos(x))
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.set_title('正弦曲线')
ax2.set_title('sin')

# 绘制正切曲线
ax3.plot(x, np.tan(x))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正弦曲线')
ax3.set_title('sin')
plt.show()
