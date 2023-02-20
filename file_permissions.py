from manim import *

class file_permissions(Scene):
    def construct(self):
        group = Title("Group 5", match_underline_width_to_text= True)
        file = SVGMobject("text.svg")
        file.shift(UP*1)

        self.add(group, file)

        Tex.set_default(font_size= 40, color= BLUE)
        per = Tex("rwxr - - r - -").next_to(file, DOWN)

        self.add(per)

        for i in per.submobjects[0][0:4]:
            one = Tex("1").shift(i.get_center())
            self.play(Transform(i, one))
        
        for i in per.submobjects[0][4:6]:
            zero = Tex("0").shift(i.get_center())
            self.play(Transform(i, zero))

        one = Tex("1").shift(per.submobjects[0][6].get_center())
        self.play(Transform(per.submobjects[0][6], one))

        for i in per.submobjects[0][7:9]:
            zero = Tex("0").shift(i.get_center())
            self.play(Transform(i, zero))