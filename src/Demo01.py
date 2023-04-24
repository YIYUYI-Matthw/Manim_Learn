import numpy
from manimlib.imports import *
from manimlib import constants

# https://zhuanlan.zhihu.com/p/379544971 这个教程不错

if __name__ == '__main__':
    mob = Mobject()
    # 使用ndarray定义三维坐标，2D场景，第三维度坐标设为0
    point = numpy.array([1, 1, 0])  # origin=numpy.array([0,0,0])
    # FRAME_HIGHT = 8.0：画面总高度为8个单位
    print(constants.FRAME_HEIGHT)
    # 画面宽度由高度&长宽比决定，约14
    print(constants.FRAME_WIDTH)
    # constants中定义了常见的方向向量LEFT：([1,0,0])
    print(constants.UP)  # 上下左右
    print(constants.UR)  # ([1,1,0])
    print(constants.TOP)  # ([max,1,0])
    print(constants.OUT)  # ([0,0,1]) 三维
    print(constants.UP + constants.RIGHT)  # 合成向量
    # shift(*vector)
