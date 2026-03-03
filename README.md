# 🐍 Python Basics Exercises

这是一个记录 Python 学习历程的代码仓库。项目中包含了从基础语法、控制流、面向对象编程到简单数据分析和硬件通信的练习代码。

## 📂 项目结构与内容

目前仓库包含以下主要练习文件：

| 文件名                  | 类别      | 描述                                                                      |
| :---------------------- | :-------- | :------------------------------------------------------------------------ |
| **`G.py`**              | 算法      | 实现了冒泡排序（升序/降序）以及数字重组差值计算逻辑。                     |
| **`猜数字.py`**         | 游戏/逻辑 | 经典的猜数字小游戏，练习 `random` 库与 `if/else` 循环控制。               |
| **`股价计算小程序.py`** | 基础运算  | 模拟股票每日增长，练习变量定义与数学运算。                                |
| **`数据挖掘.py`**       | 数据分析  | 使用 `pandas` 和 `numpy` 进行简单的数据相关性分析。                       |
| **`串口调试.py`**       | 硬件通信  | 使用 `pyserial` 库进行串口通信的基础测试（如连接机械臂）。                |
| **`love_generator.py`** | 创意/图形 | 使用 `tkinter` 绘制动态跳动的数学函数爱心动画。（可在 Releases 下载 exe） |
| **`test.py`**           | 语法综合  | 包含大量基础语法的练习笔记（字符串、列表、字典、JSON、类与对象等）。      |

## 🚀 环境依赖

本项目基于 Python 3.x 开发。

部分脚本依赖第三方库，如果运行报错，请使用 pip 安装对应依赖：

```bash
# 数据挖掘.py 需要
pip install pandas numpy

# 串口调试.py 需要
pip install pyserial
```

## 💡 快速开始

1. **克隆仓库**

   ```bash
   git clone https://github.com/NoExemption/py_basics_exercises.git
   ```

2. **运行脚本**
   例如，运行猜数字游戏：
   ```bash
   python 猜数字.py
   ```

### 📦 下载可执行程序

对于 `love_generator.py`，你可以在本仓库的 **Releases** 页面直接下载打包好的 `love_generator.exe` 文件，无需安装 Python 环境即可运行。

## 📝 学习笔记

- **基础语法**：通过 `test.py` 练习了 Python 的动态类型特性和各类字面量。
- **流程控制**：在 `猜数字.py` 中深入理解了 `while` 循环和条件判断的嵌套。
- **算法思维**：在 `G.py` 中尝试手写了排序算法，理解了列表操作。
- **库的使用**：初步接触了 Python 强大的生态系统（Pandas, Numpy, PySerial）。
- **GUI 编程**：通过 `love_generator.py` 学习了 `tkinter` 画布操作和数学函数在图形学中的应用。

---

_Keep Coding, Keep Learning!_
