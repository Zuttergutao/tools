import matplotlib.pyplot as plt
import matplotlib_colorschemes

# 注册颜色方案
matplotlib_colorschemes.register_schemes('colorschemes/example.yaml')

# 使用颜色方案1绘制折线图
plt.plot(x, y, color='Scheme1_0')

# 使用颜色方案2绘制散点图
plt.scatter(x, y, color='Scheme2_1')

# 显示图形
plt.show()
