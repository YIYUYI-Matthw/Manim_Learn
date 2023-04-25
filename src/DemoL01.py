from os import system

from manimlib.imports import *


class Square2Circle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        square.flip(axis=LEFT)
        square.rotate(PI / 3)
        square.set_fill(GREEN, opacity=0.5)
        self.play(ShowCreation(square), run_time=2)  # self.add就没有动画效果了
        circle.set_fill(RED, opacity=0.5)
        self.play(Transform(square, circle))
        self.wait(1)  # 停顿一秒
        self.play(FadeOut(square))  # 是square淡出，不是circle：改变的是square的属性，不是指向


class WriteForm(Scene):
    def construct(self):
        # 一般文字用TextMOB
        annotation = TextMobject(
            "the formula below shows how to find out the summation of 1 to 100",
            tex_to_color_map={"summation": RED}
        )
        # 公式用TexMOB
        formula = TexMobject(
            r'\sum_{x=1}^{100} x=\frac{(1+100)}{2}*100=5050',
            color=BLUE
        )
        # 向量对象组
        group = VGroup(annotation, formula)
        group.arrange(DOWN)  # 依次向下排列
        # 整体放缩
        group.set_width(FRAME_WIDTH * 2 / 3)
        # 调整相对位置
        annotation.move_to(UP / 2)
        formula.move_to(DOWN / 2)
        # 动画：还是分别写出来
        self.play(Write(annotation))
        self.play(Write(formula))
        # 停顿
        self.wait(1)


class Moving(Scene):
    def construct(self):
        num = DecimalNumber(
            0,
            show_ellipsis=True,  # 省略号
            num_decimal_places=3,  # 小数点保留三位
            include_sign=True,  # 显示正号
        )
        # to_edge：和这个边对齐
        square = Square().to_edge(DOWN)
        # 设置数字跟随
        num.add_updater(lambda x: x.next_to(square, RIGHT))  # 位置始终在右边一个
        num.add_updater(lambda item: item.set_value(square.get_center()[1]))
        # 添加物体
        self.add(square)
        self.add(num)
        # 更新square位置
        """
        self.play(
            square.to_edge, UP,  # 执行edge_to(UP)
            rate_func=there_and_back, # 执行完毕再返回
            run_time=5,
        )
        """
        self.play(
            square.to_edge, UP,  # 执行edge_to(DOWN)
            run_time=3,
        )
        self.wait(1)
        self.play(
            square.to_edge, DOWN,
            run_time=3,
        )
        # 等待
        self.wait(1)


class Grid_(Scene):
    def construct(self):
        grid = NumberPlane()  # 构建一个坐标平面
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)

        self.add(grid)  # 确保grid_title在grid上方
        self.play(
            Write(grid_title, run_time=2),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),  # 创建grid的动画，时长为3，延迟为10%
        )

        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        # move_to：移动到，可传入MOB、坐标、(MOB,坐标)
        # grid_transform_title.move_to(grid_title.get_center())  # 移动到grid_title处（center），其实相当于没动
        # grid_transform_title.move_to(grid_title)  # 移动到grid_title.center处，其实相当于没动
        grid.prepare_for_nonlinear_transform()  # 让grid准备进行非线性变换
        self.play(
            Transform(grid_title, grid_transform_title),
            # function, param : 类似lambda表达式吧
            grid.apply_function,  # 对grid施加一个函数，实现非线性变换
            lambda p: p + np.array([  # 输入值为一个点（三维坐标），返回值也为一个点
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()


if __name__ == '__main__':
    # system("python -m manim DemoL01.py Square2Circle --media_dir ../media\\ -p")
    system("python -m manim DemoL01.py Moving --media_dir ../media\\ -p")
