import tkinter as tk
import math
import random
import time

# 弹窗文字

messages = [
    "我喜欢你","愿你天天开心","❤️","遇见你真好","想你了","你很重要",
    "世界因你温柔","❤️","祝你幸福","Always with you","❤️","Love U",
    "希望你被温柔以待","今天也要笑呀","你是我的偏爱","❤️","万事顺遂",
    "愿你心想事成","遇见你是幸运","❤️","你值得所有美好",
    "愿快乐常伴你左右","平安喜乐","你真的很好",
    "生活因你闪光","未来可期","愿你被世界宠爱","❤️","你是光",
    "一切都会更好","请保持快乐","你在 就很好","愿你所愿皆所得",
    "❤️","温柔且坚定","祝你每天都有好心情",
    "你是独一无二的","愿幸福围绕你","❤️","记得照顾自己",
    "愿岁月温柔","你让我心动","所有美好都给你",
    "不止今天喜欢你","你是人间浪漫","❤️","愿你永远被爱","为你而来",
]

colors = [
    "#FF4D4D","#FF6F91","#FF9671","#FFC75F","#F9F871",
    "#FF9CEE","#FDCB9E","#FAB1A0","#E17055","#FD79A8",
    "#F78FB3","#CF6A87","#EA8685","#FF7979","#FDA7DF",
    "#D980FA","#F8A5C2","#FC427B","#E84393","#FFB8B8",
]

# 初始化
root = tk.Tk()
root.withdraw()

# 爱心坐标
points = []
num_points = 160
for i in range(num_points):
    t = i * (2 * math.pi / num_points)
    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )
    points.append((x, y))

center_x, center_y = 900, 400 #坐标
scale = 30 #大小
delay = 0.07 #速度

# 创建窗口并记录信息
windows = []

for i, (x, y) in enumerate(points):
    win = tk.Toplevel()
    win.overrideredirect(True)
    win.attributes("-topmost", True)

    label = tk.Label(
        win,
        text=messages[i % len(messages)],
        bg=random.choice(colors),
        fg="white",
        font=("微软雅黑", 15),
        padx=10,
        pady=6,
    )
    label.pack()

    px = int(center_x + x * scale)
    py = int(center_y - y * scale)
    win.geometry(f"+{px}+{py}")
    win.update()

    # 随机分散方向
    dx = random.randint(-8, 8)
    dy = random.randint(-8, 8)

    windows.append({
        "win": win,
        "x": px,
        "y": py,
        "dx": dx,
        "dy": dy
    })

    time.sleep(delay)

# 分散动画
def scatter():
    for w in windows:
        w["x"] += w["dx"]
        w["y"] += w["dy"]
        w["win"].geometry(f"+{w['x']}+{w['y']}")
    root.after(30, scatter)

# 关闭程序
def close_all():
    for w in windows:
        w["win"].destroy()
    root.quit()

# 时间线控制
root.after(1000, scatter)        # 分散 1
root.after(11000, close_all)    # 关闭（1 + 10）

root.mainloop()
