**常用控件**

仅有窗口并不能实现交互，还需要控件，Tkinter 提供了各种控件，如按钮、标签和文本
框。在一个 GUI 应用程序中使用，这些控件通常被称为控件或者部件，目前有15种
Tkinter 部件，如下列表:

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2MzgyODk3Ni0xNDY0MzU0NzU1LnBuZw?x-oss-process=image/format,png)

**几何管理**

Tkinter 控件有特定的几何状态管理方法，管理整个控件区域组织，以下是 Tkinter 公开
的几何管理类：包、网格、位置。

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2MzkxODMxOC0xODUxMTUyMjk3LnBuZw?x-oss-process=image/format,png)

**Lable控件**标签控件，基本用法为： Lable(root, option...) ，即：Label(根对象, [属性列表])，
其中属性列表如下：

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2Mzk1MDYwMy0xNTU3MzYzNTAwLnBuZw?x-oss-process=image/format,png)

 **Button控件**

Button 控件是一个标准的 Tkinter 部件，用于实现各种按钮。按钮可以包含文本或图
像，还可以关联 Python 函数。
Tkinter 的按钮被按下时，会自动调用该函数。
按钮文本可跨越一个以上的行。此外，文本字符可以有下划线，例如标记的键盘快捷
键。默认情况下，使用 Tab 键可以移动到一个按钮部件，用法如下：
Entry(根对象, [属性列表])，即Entry(root, option...)
常用的属性列表如下：

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2NTExMzg3NC0yMTAzMjc3MzgzLnBuZw?x-oss-process=image/format,png)

 **Checkbutton控件**Checkbutton 是复选框，又称为多选按钮，可以表示两种状态。用法为： Checkbutton
( root, option, ... )， 其中可选属性 option 有很多，如下表所示：

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2NTYzMDQ5Mi0yMDM3NDgxODQ1LnBuZw?x-oss-process=image/format,png)

以下是这个小工具的常用方法：

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE2NTcwMDk4Mi0xNjQyMjExOTIxLnBuZw?x-oss-process=image/format,png)

**Radiobutton控件**

单选按钮是一种可在多个预先定义的选项中选择出一项的 Tkinter 控件 。单选按钮可显
示文字或图片，显示文字时只能使用预设字体，该控件可以绑定一个 Python 函数或方
法，当单选按钮被选择时，该函数或方法将被调用。
单选按钮（Radio Button）这个名字来源于收音机（Radio）上的调频按钮， 这些按钮用
来选择特定波段或预设电台，如果一个按钮被按下， 其他同类的按钮就会弹起，即同时
只有一个按钮可被按下。
一组单选按钮控件和同一个变量关联。点击其中一个单选按钮将把这个变量设为某个预
定义的值。一般用法为： Radiobutton(myWindow，options) ，其中 option 与
Checkbutton，Button 大多重合，用法一致。

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE3MDAwNDM0NS05NDQ3MDI1NzkucG5n?x-oss-process=image/format,png)

 **Menu控件**

Menu被用来创建一个菜单，创建Menu类的实例，然后使用add方法添加命令或者其他
菜单内容。使用方法如下：
Menu(root,option,…)
其中 option 列表如下：

**![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE3MDYyNzg4NC05OTg1NzU5MTIucG5n?x-oss-process=image/format,png)**

特有函数如下：

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE3MDY1MDQxMC0yMDkyMDA3MTQzLnBuZw?x-oss-process=image/format,png)

 Message控件

Message 控件用来展示一些文字短消息。Message 和 Label 控件有些类似， 但在展示文
字方面比 Label 要灵活，比如 Message 控件可以改变字体，而 Label 控件只能使用一种
字体，它提供了一个换行对象，以使文字可以断为多行。
它可以支持文字的自动换行及对齐，这里要澄清一下前面提到的 Message 控件可以改变
字体的说法: 这是说我们可以为单个控件设置任意字体, 控件内的文字都将显示为该字
体，但我们不能给单个控件内的文字设置多种字体，如果你需要这么做，可以考虑使用
Text 控件。

![img](http://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQyMTAzMS8yMDE4MTAvMTQyMTAzMS0yMDE4MTAxNTE3MTAyOTQ4MC05Mjk5MTgzOTUucG5n?x-oss-process=image/format,png)


