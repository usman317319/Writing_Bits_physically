# Author : @uwezi
# Find him at : https://github.com/uwezi?tab=repositories

from manim import *

class hdd(Scene):
    def construct(self):
        bitsPerCylinder = 64
        disc = VGroup(
            Circle(radius=3).set_fill(color=GRAY, opacity=1),
            Line(start=ORIGIN, end=[0,3,0],stroke_width=1,color=BLACK)
        )
        for r in np.linspace(start=1, stop=2.5, num=5, endpoint=True):
            cylinder = VGroup(
                *[Line(
                    start=[0, r, 0], 
                    end=[0, r+0.2, 0], 
                    stroke_width=7, 
                    color=YELLOW if np.random.uniform(0,1) > 0.5 else BLUE
                  ).rotate(angle=a, about_point=ORIGIN)
                  for a in np.linspace(start=0, stop=2*PI, num=bitsPerCylinder, endpoint=False)]
            )
            disc += cylinder
        def discUpdater(mobj, dt):
            # 3/15 of a second per bit, for nice rendering at 15 fps
            # 3*bitsPerCylinder/15 seconds per rotation
            # at 128 bits: 25.6 seconds/rotation
            mobj.rotate(dt*(2*PI*15)/(3*bitsPerCylinder))
        disc.add_updater(discUpdater)
        bitTxt = Tex(r"Bit \#:").to_edge(UL)
        bitNr = DecimalNumber(number = 0, num_decimal_places=0, edge_to_fix=LEFT).next_to(bitTxt)
        def bitNrUpdater(mobj,dt):
            val = mobj.get_value()
            val = val + (15/3)*dt
            if val >= bitsPerCylinder:
                val = 0
            mobj.set_value(val)    
        bitNr.add_updater(bitNrUpdater)

        self.add(disc,bitTxt,bitNr)

        self.wait(12.8)
