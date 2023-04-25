## 函数

* self.play(Homotopy(func, mob))
  按照func规则更改mob中心坐标
  `func(x,y,z,t):[x,y,z]` ：要求输入坐标+时间，返回时间
* self.play(MoveAlongPath(mob1,mob2))
  mob1围绕mob2运动
* self.play(mob.func,param)
  self.play(mob.move_to, DOWN)：mob移动到DOWN位置：动画呈现
* self.play(mob.apply_function,lambda ax : ndarray&ax)
  ax为mob的各个坐标点，返回坐标：做非线性变换

## 动画

下面展示的都是相对常用的效果

* Creation

  ShowCreation

  DrawBorderThenFill

  Write

  ShowSubmobjectsOneByOne

* Fade：淡入淡出

  FadeIn

  FadeOut

* Growing

  GrowArrow

* Indicate：强调

  FocusOn

  Indicate

  CircleIndicate

  ShowCreationThenDestructionAround

* Movement

  ShowCreationThenDestructionAround：(x,y,z,t)->(x',y',z')

  MoveAlongPath(mob1,mob2)

* Rotate

  Rotating：继承自Rotate：比较顺滑

* Number：动态数字

  ChangingDecimal

  ChangeDecimalToValue

* Composition：mob组动画

  AnimationGroup

  Succession

  LaggedStart

* Update

  UpdateFromFunc

  MaintainPositionRelativeTo

* Transform

  Transform：更改mob属性，而非替换为其他对象

  ReplacementTransform：替换为其他mob

  MoveToTarget：基本等价于self.play(mob.func, param)
  ```python
  class MoveToTargetExample(Scene):
    def construct(self):
      A = TextMobject("Text-A").to_edge(LEFT)
      A.generate_target()  # copyA自身形成A的target属性
      A.target.scale(3).shift(RIGHT*7+UP*2) # 操作A的target
      self.add(A)
      self.wait()
      self.play(MoveToTarget(A))
      self.wait()
  ```
* ApplyMethod(mob.func,param)
* ApplyFunction(func,mob)
* CyclicReplace(*mobs)

## Mobject

* SVGMobject
* TextMobject
* TexMobject
* Geometry