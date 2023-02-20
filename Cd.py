from manim import *

class RotatingCanvas(Scene):
    def construct(self):
        group = Title("Group 5", match_underline_width_to_text= True).shift(UP*0.4)
        self.add(group)
        our_plane = Axes(x_range = [-3,3], y_range=[-3,3], x_length = 6, y_length=6).scale(0.5)
        #self.add(axes)
        #numberplane = NumberPlane(x_range= [-5,5,0.25], y_range= [-5,5,0.25], x_length= 10, y_length= 10)
        numberplane = NumberPlane(x_range = [-5,5,0.25], y_range=[-3,3,0.25], x_length = 6, y_length=6, tips=False).scale(0.5)
        cd = Circle(radius= 3.5, color= BLUE, fill_opacity= 0.5)
        self.add(cd)
        t=0

        dot = Dot(point= our_plane.c2p(t,0))

        dot_list = []

        # Value Tracker will tracker values from a starting point given as argument to the ValueTracker Function to anyvalue
        v = ValueTracker(0)
        
        line = always_redraw(lambda: Line(start= our_plane.c2p(0,0), end= our_plane.c2p(v.get_value(),0)))
        self.add(line)

        #self.add(numberplane, dot)
        self.add(dot)
        for t in np.linspace(0,2,250):

            point_ = always_redraw(lambda: Dot(point= our_plane.c2p(t,0)))

            dot = Dot(point= our_plane.c2p(t,0))

            dot_list.append(dot)

            dots_group = VGroup(*dot_list)

            self.play(
                AnimationGroup(
                    Create(point_),
                    Rotate(
                        dots_group,
                        angle= -PI/30,
                        about_point=ORIGIN,
                    ),
                    Rotate(
                        cd,
                        angle= -PI/30,
                        about_point=ORIGIN,
                    ),
                    v.animate.increment_value(t-v.get_value()), run_time= 0.1
                    )
            )
