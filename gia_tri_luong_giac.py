import math 
from manim import *

class add_update_3(Scene):
    def construct(self):
        # --- Hệ trục tọa độ 
        r = 2.5
        Ox = Arrow(LEFT*(r+1), RIGHT*(r+1.2), stroke_width = 2.5, max_tip_length_to_length_ratio=0.025, buff=0)
        Oy = Arrow(DOWN*(r+0.8), UP*(r+1.2), stroke_width =2.5, max_tip_length_to_length_ratio=0.025, buff=0)
        label_1 = Tex(r"$1$").scale(0.5).move_to(RIGHT*(r+0.15)+UP*0.18)
        label_x = Tex(r"$x$").scale(0.6).move_to(RIGHT*(r+1.2)+UP*0.2)
        label_y = Tex(r"$y$").scale(0.6).move_to(UP*(r+1.2)+RIGHT*0.2)
        label_O = Tex(r"$O$").scale(0.6).move_to(LEFT*0.2+DOWN*0.2)
        self.add(Ox, Oy, Dot(radius=0.06), label_1, label_x, label_y, label_O)
        self.wait(2)
        # # --- Đường tròn c        
        c = Circle(radius=r, stroke_width = 3, color=BLUE_D)
        # # -----
        k = 60
        tracker = ValueTracker(k)
        dot = Dot(color=YELLOW_C, radius=0.05).move_to(c.point_at_angle(k*PI/180)) # điểm M
        dot.add_updater(lambda d: d.move_to(c.point_at_angle(tracker.get_value()*PI/180)))
        # -- Label  M
        delta = 0.3
        label_M = MathTex(r"M").scale(0.6).move_to([(r+delta)*math.cos(k*PI/180),(r+delta)*math.sin(k*PI/180),0])
        label_M.add_updater(lambda m: m.move_to([(r+delta)*math.cos(tracker.get_value()*PI/180),(r+delta)*math.sin(tracker.get_value()*PI/180),0]))
        # --- line x 
        line_x = Line(dot.get_center(), RIGHT*dot.get_center()[0], stroke_width = 2, color = PURE_GREEN)
        line_x.add_updater(lambda l: l.put_start_and_end_on(c.point_at_angle(tracker.get_value()*PI/180), RIGHT*c.point_at_angle(tracker.get_value()*PI/180)[0]))
        # line_x.add_updater(lambda l: l.put_start_and_end_on(dot.get_center(), RIGHT*dot.get_center()[0]))
        # --- line y
        line_y = Line(dot.get_center(), RIGHT*dot.get_center()[0], stroke_width =2, color = RED)
        line_y.add_updater(lambda l: l.put_start_and_end_on(c.point_at_angle(tracker.get_value()*PI/180), UP*c.point_at_angle(tracker.get_value()*PI/180)[1]))
        # --- line OM 
        line_OM = Line(ORIGIN, dot, stroke_width = 2.5)
        line_OM.add_updater(lambda l:l.put_start_and_end_on(ORIGIN, c.point_at_angle(tracker.get_value()*PI/180)))
        # --- dot_cos
        dot_cos = Dot(radius=0.05, color = PURE_GREEN).move_to(c.point_at_angle(k*PI/180)[0]*RIGHT)
        dot_cos.add_updater(lambda d: d.move_to(c.point_at_angle(tracker.get_value()*PI/180)[0]*RIGHT))
        # --- dot_sin 
        dot_sin = Dot(radius=0.05, color = RED).move_to(c.point_at_angle(k*PI/180)[1]*UP)
        dot_sin.add_updater(lambda d: d.move_to(c.point_at_angle(tracker.get_value()*PI/180)[1]*UP))
        # --- cung ở tâm
        arc = Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, dot), radius= 0.5, stroke_width=2)
        arc.add_updater(
            lambda a: a.become(Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, c.point_at_angle(tracker.get_value()*PI/180)), radius =0.5, stroke_width=2))
        )
        # --- Label alpha
        dd = 0.7
        label_alpha = MathTex(r"\alpha").scale(0.5).move_to([dd*math.cos(k*PI/360),dd*math.sin(k*PI/360),0])
        label_alpha.add_updater(lambda l: l.move_to([dd*math.cos(tracker.get_value()*PI/360), dd*math.sin(tracker.get_value()*PI/360),0]))
        # --- func tạo nhãn các đơn vị
        def label_unit(point):
            dot = Dot(point, radius=0.05)
            self.add(dot)
        # --- value - cos
        value_cos = DecimalNumber().scale(0.5).set_color(PURE_GREEN)
        value_cos.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[0]*1/r))
        value_cos.add_updater(lambda m: m.next_to(RIGHT*c.point_at_angle(tracker.get_value()*PI/180)[0], DOWN, buff = 0.15))     
        # --- value_sin
        value_sin = DecimalNumber().scale(0.5).set_color(RED)
        value_sin.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[1]*1/r))
        value_sin.add_updater(lambda m: m.next_to(UP*c.point_at_angle(tracker.get_value()*PI/180)[1], LEFT, buff = 0.15))
        # --- label alpha copy
        # label_alpha_copy = MathTex(r"\alpha = ").scale(0.6).to_corner(UL).shift(RIGHT*0.6+DOWN)
        # label_cos_alpha = MathTex(r"\cos \alpha = ").scale(0.6).next_to(label_alpha_copy, DOWN , buff= 0.3)
        # label_sin_alpha = MathTex(r"\sin \alpha = ").scale(0.6).next_to(label_cos_alpha, DOWN, buff=0.3)

        label_alpha_copy = MathTex(r"\alpha = ").scale(0.6)
        label_cos_alpha = MathTex(r"\cos \alpha = ").scale(0.6)
        label_sin_alpha = MathTex(r"\sin \alpha = ").scale(0.6)
        
        VGroup(label_alpha_copy, label_cos_alpha, label_sin_alpha).arrange(DOWN, aligned_edge=LEFT, buff=0.4)\
            .to_corner(UL).shift(RIGHT*0.6+DOWN).set_color(TEAL_C)
        # --- get value and show
        get_value_alpha = DecimalNumber(unit="^\circ").scale(0.6).next_to(label_alpha_copy, RIGHT, buff= 0.1)
        # get_value_alpha.scale(0.6)
        get_value_alpha.scale(0.6).add_updater(lambda v: v.set_value(tracker.get_value()))

        get_value_cos = DecimalNumber().scale(0.6).next_to(label_cos_alpha, RIGHT, buff= 0.25).shift(DOWN*0.01)
        get_value_cos.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[0]*1/r))

        get_value_sin = DecimalNumber().scale(0.6).next_to(label_sin_alpha, RIGHT, buff= 0.25).shift(DOWN*0.01)
        get_value_sin.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[1]*1/r))
        # --- Label sin^2 + cos^2 =1 
        label_sin_sin_cos_cos = MathTex(r"\sin^2 \alpha +\cos^2 \alpha =1").scale(0.6)\
            .to_corner(DL).shift(UP*1+RIGHT*0.6).set_color(TEAL_C)    
        # --- 
        for i in [RIGHT*r, UP*r, LEFT*r, DOWN*r]:
            label_unit(i)
        # --------- Đường tròn lượng giác và các điểm
        self.play(
            *[Create(mob) for mob in [c, 
            arc,
            label_alpha,
            line_x,
            line_y,
            line_OM,
            dot,
            dot_cos,
            dot_sin, 
            label_M
            ]] , run_time = 4
        )
        self.wait()
        self.play(*[Write(mob) for mob in [value_cos, value_sin, label_alpha_copy, label_cos_alpha, label_sin_alpha, get_value_cos,get_value_sin, label_sin_sin_cos_cos, get_value_alpha]], run_time =2)
        # --- 
        self.wait()
        self.play(tracker.animate.set_value(10), run_time = 5)
        self.wait()
        self.play(tracker.animate.increment_value(350), run_time = 16, rate_func = there_and_back)
        self.play(tracker.animate.set_value(70))
        self.wait()
        # ---- Tạo giá trị tan và cot 
        label_tan = MathTex(r"\tan \alpha = {\sin \alpha \over \cos \alpha} = ").scale(0.6)\
            .to_corner(UR).shift(LEFT*0.8+DOWN*0.8).set_color(TEAL_C)
        label_cot = MathTex(r"\cot \alpha = {\cos \alpha \over \sin \alpha} = ").scale(0.6)\
            .next_to(label_tan, DOWN, buff = 0.5).set_color(TEAL_C)

        label_tan_cot = MathTex(r"\tan \alpha \cdot \cot \alpha = 1").scale(0.6)\
            .to_corner(DR).shift(UP*1+LEFT*0.6).set_color(TEAL_C)
        dieu_kien = Tex(r"với $\alpha \ne \dfrac{\pi}{2} + k \pi, k\in \mathbb Z$").scale(0.6)\
            .next_to(label_tan_cot, DOWN, buff= 0.4).set_color(TEAL_C)     

        value_tan = DecimalNumber().scale(0.6).next_to(label_tan, RIGHT, buff= 0.2)
        value_tan.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[1]/c.point_at_angle(tracker.get_value()*PI/180)[0]))        
        value_cot = DecimalNumber().scale(0.6).next_to(label_cot, RIGHT, buff= 0.2)
        value_cot.add_updater(lambda v: v.set_value(c.point_at_angle(tracker.get_value()*PI/180)[0]/c.point_at_angle(tracker.get_value()*PI/180)[1]))        

        # self.add(label_tan, label_cot, value_tan, value_cot)
        self.play(*[Write(mob) for mob in [label_tan, label_cot, value_tan, value_cot, label_tan_cot, dieu_kien] ], run_time = 2)
        self.play(tracker.animate.set_value(10), run_time=6)    
        self.wait()