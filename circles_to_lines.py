from manim import *

class rollOut2(Scene):                
    def construct(self):
        group = Title("Group 5", match_underline_width_to_text= True)
        ang = ValueTracker(0)
        circumferenceDifference = 3
        radiusDifference = circumferenceDifference/(2*PI)
        rad1 = 1
        rad2 = rad1 + radiusDifference

        arc1 = Circle(radius=rad1).move_to([-4,0,0], aligned_edge=DOWN)
        def arcUpdater1(mobj): 
            arc = Arc(
                    radius = rad1,
                    start_angle=ang.get_value(),
                    angle=2*PI-ang.get_value()
            ).rotate(1.5*PI-ang.get_value())
            arc.shift((rad1*ang.get_value() - arc.get_start()[0] - 4)*RIGHT - arc.get_start()[1]*UP)
            mobj.become(arc)
        arc1.add_updater(arcUpdater1)
        line1 = always_redraw(lambda:
                Line(
                    start=[-4,0,0],
                    end=[rad1*ang.get_value() - 4,0,0]
                )
        )

        arc2 = Circle(radius=rad2).move_to([-4,-radiusDifference,0], aligned_edge=DOWN)
        def arcUpdater2(mobj): 
            arc2 = Arc(
                    radius = rad2,
                    start_angle=ang.get_value(),
                    angle=2*PI-ang.get_value()
            ).rotate(1.5*PI-ang.get_value())
            arc2.shift((rad2*ang.get_value() - arc2.get_start()[0] - 4)*RIGHT - (arc2.get_start()[1]+radiusDifference)*UP)
            mobj.become(arc2)
        arc2.add_updater(arcUpdater2)
        line2 = always_redraw(lambda:
                Line(
                    start=[-4,-radiusDifference,0],
                    end=[rad2*ang.get_value() - 4,-radiusDifference,0]
                )
        )

        self.add(arc1,line1,arc2,line2, group)

        self.wait(3)

        self.play(
            ang.animate.set_value(2*PI),
            rate_func = rate_functions.linear,
            run_time = 2
        )
        self.wait(4)

        self.play(
            ang.animate.set_value(0),
            run_time = 2
        )