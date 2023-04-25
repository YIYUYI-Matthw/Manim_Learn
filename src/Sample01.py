from math import cos, pi, sin
from os import system
from manimlib.imports import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # Circle继承自Mobject
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_stroke(BLUE, width=5)
        circle.set_fill(RED, opacity=0.5)  # BLUE报错，但是不耽误用
        # 添加内容
        # self.add(circle) # 只添加的话，不会有动画：animation
        # 设定创建动作：animation
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class Font(Scene):
    def construct(self):
        text1 = Text("This is ITALIC", slant=ITALIC)  # 意大利斜体
        text2 = Text("This is BOLD", weight=BOLD)  # 粗体
        text3 = Text("This is OBLIQUE", slant=OBLIQUE)  # 斜体
        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait()


class Static_(Scene):
    def construct(self):
        circle = Circle(
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=GREEN,
            stroke_opacity=0.9,
            stroke_width=2,
            gloss=1.0
        )
        self.add(circle)
        self.wait()  # mp4


class Arc_(Scene):
    def construct(self):
        arc1 = Arc(
            start_angle=0,  # 起始位置的角度：向上为0
            angle=PI,  # 弧的角度，为180度
            radius=3,  # 半径为3/FRAME_HEIGHT高
            arc_center=ORIGIN  # 弧的中心的坐标，为(0,0)向左移动一个单位长度
        )
        arc1.set_fill(BLUE, opacity=0.5)
        arc2 = Arc(
            start_angle=0,  # 起始位置的角度：向上为0
            angle=PI,  # 弧的角度，为180度
            radius=3,  # 半径为3/FRAME_HEIGHT高
            arc_center=LEFT  # 弧的中心的坐标，为(0,0)向左移动一个单位长度
        )
        arc2.set_fill(RED, opacity=0.5)
        self.wait()
        self.play(Write(arc1))
        self.wait()
        self.play(Write(arc2))
        self.wait()


class Move_(Scene):
    def construct(self):
        arc = Arc(
            start_angle=0,  # 起始位置的角度：向上为0
            angle=PI,  # 弧的角度，为180度
            radius=3,  # 半径为3/FRAME_HEIGHT高
            arc_center=LEFT
        )
        self.add(arc)
        self.wait()
        arc.move_to(LEFT * 2)
        self.play(Write(arc))


class FA(Scene):
    # 一个对象在Scene中只能同时拥有一个
    def construct(self):
        arc = Arc(
            start_angle=0,  # 起始位置的角度：向上为0
            angle=PI,  # 弧的角度，为180度
            radius=3,  # 半径为3/FRAME_HEIGHT高
            arc_center=LEFT
        )
        # 添加物体到场景
        self.add(arc)
        arc1 = Arc(
            start_angle=0,  # 起始位置的角度：向上为0
            angle=PI,  # 弧的角度，为180度
            radius=3,  # 半径为3/FRAME_HEIGHT高
            arc_center=LEFT
        )
        arc1.move_to(arc.get_arc_center() + RIGHT * 2)
        square = Square(side_length=2)

        def rr(x, y, z, t):
            x = x + 2 * cos(2 * pi * t)
            y = y + 2 * sin(2 * pi * t)
            z = 0
            return [x, y, z]

        # Homotopy：Homotopy is a function from (x, y, z, t) to (x', y', z')
        self.play(Homotopy(rr, arc), run_time=2, rate_func=linear)
        # 移动：从一个物体移动到另一个，可以是不同形状的物体
        self.play(Transform(arc, square))
        self.add(arc1)
        # 沿着物体移动：obj1沿着obj2
        self.play(MoveAlongPath(arc, arc1), run_time=2)
        # 淡入淡出：FadeIn
        for i in range(5):
            arc = Arc()  # 创建多个对象，就可以同时存在了
            arc.move_to(LEFT * i)  # move_to：移动到指定位置
            self.play(FadeIn(arc))
            self.add(arc)


if __name__ == "__main__":
    # 类名做参数指定渲染对象
    # --media_dir指定输出路径
    # Media will be written to ./media\. You can change this behavior with the --media_dir flag.
    # system("python -m manim Sample01.py SquareToCircle --media_dir ../media\\ -p")  # -p preview：预览-打开视频文件
    # system("python -m manim Sample01.py Font --media_dir ../media\\ -p -i")  # 输出为gif：好像失败了
    # system("python -m manim Sample01.py Static_ --media_dir ../media\\ -p")
    # system("python -m manim Sample01.py Arc_ --media_dir ../media\\ -p")
    system("python -m manim Sample01.py FA --media_dir ../media\\ -p")
