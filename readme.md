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