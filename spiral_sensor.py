from manim import *

class spiral_sensor(Scene):
    def construct(self):
        axes = Axes().scale(0.1).shift(LEFT)
        n= 0.25

        bits = [
            1, 1, 0, # permissions
            0, 1, 1, 1, 0, 1, 0, 1,  # u
            0, 1, 1, 1, 0, 1, 0, 0,  # s
            0, 1, 1, 0, 0, 1, 0, 1,  # e
            0, 1, 1, 1, 0, 0, 1, 1,  # r
            1, 0, 1, 0, 1, 0, 1, 0,
            1, 1, 1, 0, 1, 1, 1, 0,
            1, 0, 1, 0, 1, 0, 1, 1,
            1, 0, 1, 0, 1, 0, 1, 0,
            1, 1, 1, 0, 1, 1, 1, 0,
            1, 0, 1, 0, 1, 0, 1, 1,
        ]
        i = 0
        bits_tex = always_redraw(lambda: Tex(f"bit = {bits[i]}").to_edge(UL))
        self.add(bits_tex)

        r = 0
        radius = always_redraw(lambda: Tex(f"radius = {r}").next_to(bits_tex, DOWN))
        self.add(radius)

        paths = []
        for circles in range(1, 5):
            t = ValueTracker(0) 
            for i in range(0,len(bits)):
                def get_bit():
                    x = circles*5*np.cos(t.get_value())
                    y = circles*5*np.sin(t.get_value())
                    return axes.c2p(x, y, 0)
                
                pt = always_redraw(lambda: 
                    Dot(point=
                        axes.c2p(
                            circles*5*np.cos(t.get_value()),
                            circles*5*np.sin(t.get_value())
                        )
                    ).scale(1.5)
                )

                path = TracedPath(get_bit, stroke_width= 32)
                paths.append(path)
                self.add(t, path, pt)
                if bits[i] == 0:
                    path.set_color(color= YELLOW)
                    pt.set_color(color= YELLOW)
                    bits_tex.set_color(YELLOW)
                if bits[i] == 1:
                    path.set_color(color= BLUE)
                    pt.set_color(color= BLUE)
                    bits_tex.set_color(BLUE)
                r = np.sqrt((circles*5*np.cos(t.get_value()))**2 + (circles*5*np.sin(t.get_value()))**2)
                j = (PI/2)/r
                self.play(AnimationGroup(
                        t.animate.increment_value(
                            j
                            ), run_time=1
                    )
                )
                if t.get_value() >= 2*PI:
                    break


        paths = VGroup(*paths)
        self.play(Rotate(
            paths,
            angle= 4 * PI
        ), run_time= 5)