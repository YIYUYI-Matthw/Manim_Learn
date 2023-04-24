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


if __name__ == "__main__":
    # 类名做参数指定渲染对象
    # --media_dir指定输出路径
    # Media will be written to ./media\. You can change this behavior with the --media_dir flag.
    system("python -m manim Sample01.py SquareToCircle --media_dir ../media\\ -p")  # -p preview：预览-打开视频文件
    system("python -m manim Sample01.py Font --media_dir ../media\\ -p -i")  # 输出为gif：好像失败了
