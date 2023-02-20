from manim import *

class spiral_circles(Scene):
    def construct(self):
        axes1 = Axes(x_range= [-70,70], x_length= 10,y_range= [-70,70], y_length= 10).shift(LEFT * 3)
        axes2 = Axes(x_range= [-50,50], x_length= 10,y_range= [-50,50], y_length= 10).shift(RIGHT * 3)
    
        Tex.set_default(font_size= 35)
        MathTex.set_default(font_size= 35)
        group = Title("Group 5", match_underline_width_to_text= True)
        spiral_tex = Tex(r"Spiral (t$\cdot$cos(t), t$\cdot$sin(t))").to_edge(UL)
        self.play(Write(group))
        self.wait(0.5)
        self.play(Write(spiral_tex))

        # For Spiral
        t = ValueTracker(0.01)
        dot = always_redraw(lambda:
            Dot(point= axes1.c2p(t.get_value()*np.cos(t.get_value()), t.get_value()*np.sin(t.get_value())))
        )
        def spiral():
            x = t.get_value()*np.cos(t.get_value())
            y = t.get_value()*np.sin(t.get_value())
            return axes1.c2p(x, y, 0)
        path = TracedPath(spiral, stroke_width= 3, stroke_color= RED)

        # self.add(dot, path)
        # self.play(t.animate.increment_value(5*2*PI), run_time= 10)

        # self.play(FadeOut(dot, path))

        # Circles
        circle_tex = Tex("Circles (cos(t), sin(t))").to_edge(UR)
        i = 0
        circle_val = always_redraw(lambda: Tex(rf"({i}$\cdot$cos(t), {i}$\cdot$sin(t))").next_to(circle_tex, DOWN))
        self.play(Write(circle_tex))
        self.wait(0.5)
        self.play(Write(circle_val))
        colors = [RED, YELLOW, BLUE, GREEN, PINK, GRAY, GOLD, PURPLE, TEAL, MAROON]
        for i in range(1,len(colors)):
            t1 = ValueTracker(0.01)
            dot1 = always_redraw(lambda:
                Dot(point= axes2.c2p(i*2*np.cos(t1.get_value()), i*2*np.sin(t1.get_value())))
            )
            dot1.set_color(colors[i])
            def spiral():
                x = i*2*np.cos(t1.get_value())
                y = i*2*np.sin(t1.get_value())
                return axes2.c2p(x, y, 0)
            path1 = TracedPath(spiral, stroke_width= 3, stroke_color= RED)
            path1.set_color(colors[i])
            
            self.add(dot1, path1)
            self.play(t1.animate.increment_value(2*PI), run_time= 5)


        fun = ParametricFunction(lambda t: axes1.c2p(t*np.cos(t), t*np.sin(t)), t_range= [0, 5*2*PI])
        fun.set_color(RED)

        self.add(fun)

        self.wait(1)