from manim import *

def construct(self):
    self.quy_trinh_ban_hang()


class quy_trinh_ban_hang(Scene):
    def construct(self):
        w = 3
        start = Rectangle(width=1.8, height= 0.8, stroke_width =0, fill_color=GREEN, fill_opacity=0.5)
        start.round_corners(0.4).to_corner(UL).shift(1.3*RIGHT+UP*0.3)
        text_start =  Text("BẮT ĐẦU", font = "Calibri (Body)", stroke_width=0.5).scale(0.4)\
            .move_to(start)
        for char in text_start:
            char.set_color(random_bright_color())    
        group_start_text = VGroup(start, text_start)   

        # --- rectangle 1
        rec_1 = Rectangle(width = w, height=1.1, stroke_width = 2)\
            .next_to(start, DOWN, buff= 0.8)

        t_1_1 = Text("Danh sách khách hàng", font = "Calibri (Body)")\
            .scale(0.4)
        for char in t_1_1:
            char.set_color(random_bright_color())    
        t_1_2 = Text("tiềm năng", font = "Calibri (Body)")\
            .scale(0.4)
        for char in t_1_2:
            char.set_color(random_bright_color())    
        t_1_group = VGroup(t_1_1, t_1_2).arrange(DOWN, buff =0.12)\
            .move_to(rec_1)
        group_1 = VGroup(t_1_group, rec_1)\
            .next_to(start, DOWN, buff=1)            
        # ---- rectangle 2
        rec_2 = Rectangle(width = w, height=1.1, stroke_width = 2)\
            .next_to(rec_1, DOWN, buff= 0.8).round_corners(0.15)
        t_2 = Text("Danh sách chọn lọc", font="Calibri (Body)").scale(0.4)\
            .move_to(rec_2)
        group_2 = VGroup(rec_2, t_2)        
        # ---- rectangle 3
        rec_3 = Rectangle(width = w, height=1.1, stroke_width = 2)\
            .next_to(rec_2, DOWN, buff= 0.8).round_corners(0.15)
        t_3 = Text("Danh sách chưa chọn lọc", font="Calibri (Body)").scale(0.4)\
            .move_to(rec_3)
        group_3 = VGroup(rec_3, t_3)
        # ---- rectangle 4
        rec_4 = Rectangle(width = w, height=1.1, stroke_width = 0,fill_opacity=1, fill_color=YELLOW_B)\
            .next_to(rec_2, RIGHT, buff= 1.2).round_corners(0.15)
        t_4 = Text("Hẹn gặp khách hàng", font="Calibri (Body)").scale(0.4)\
            .move_to(rec_4).set_color(BLUE_E)
        group_4 = VGroup(rec_4, t_4)
        # ---- rectangle 5
        rec_5 = Rectangle(width = w, height=1.1, stroke_width = 0, fill_opacity=1, fill_color=YELLOW_B)\
            .next_to(rec_3, RIGHT, buff= 1.2).round_corners(0.15)
        t_5 = Text("Điện thoại tới khách hàng", font="Calibri (Body)").scale(0.4)\
            .move_to(rec_5).set_color(BLUE_E)
        group_5 = VGroup(rec_5, t_5)
        rec_6 = Square(side_length=1.6, stroke_width =0, fill_color=BLUE, fill_opacity =1)\
            .rotate(PI/4).next_to(rec_4, RIGHT*1.5, buff=1.5).shift(DOWN)
        t_6_1 = Text("Khác hàng có", font="Calibri (Body)").scale(0.4).set_color(YELLOW_C)
        t_6_2 = Text("mua?", font="Calibri (Body)")\
            .scale(0.4).next_to(t_6_1, DOWN, buff = 0.12).set_color(YELLOW_C)
        t_6_group = VGroup(t_6_1, t_6_2).move_to(rec_6)
        t_6_group.shift(DOWN*0.1)
        group_6= VGroup(rec_6, t_6_group)

        # --- arrow 1
        ar_1 = Arrow(
            start.get_bottom(), rec_1.get_top(), 
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.15
            )
        ar_2 = Arrow(
            rec_1.get_bottom(), rec_2.get_top(), 
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.17
            )
        ar_3 = Arrow(
            rec_2.get_bottom(), rec_3.get_top(), 
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.17
            )
        ar_4 = Arrow(
            rec_2.get_right(), rec_4.get_left(), 
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.15
            )
        ar_5 = Arrow(
            rec_3.get_right(), rec_5.get_left(), 
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.15
            )
        ar_6  = Arrow(
            rec_4.get_right(),rec_6.get_left()+UP*0.6+RIGHT*0.6,
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.05,
            path_arc = -0.7
            )
        ar_7  = Arrow(
            rec_5.get_right(),rec_6.get_left()+DOWN*0.6+RIGHT*0.6,
            stroke_width=2, buff=0,
            max_tip_length_to_length_ratio = 0.05,
            path_arc = 0.7
            )
        l_7_8 = Line(start.get_right(), [rec_6.get_top()[0], start.get_right()[1],0], stroke_width=2)        
        ar_8 = Arrow(
            [rec_6.get_top()[0], start.get_right()[1],0], rec_6.get_top(),
            stroke_width= 2, buff = 0, max_tip_length_to_length_ratio=0.035 
             )
        # --- Các LabeledDot
        dot_1 = LabeledDot(Tex(r"1", color = BLACK), color = RED)\
            .move_to(ar_1.point_from_proportion(0.5))\
            .scale(0.5)
        dot_2 = LabeledDot(Tex(r"2", color = BLACK), color = RED)\
            .move_to(ar_2.point_from_proportion(0.5))\
            .scale(0.5)    
        dot_3 = LabeledDot(Tex(r"3", color = BLACK), color = RED)\
            .move_to(ar_3.point_from_proportion(0.5))\
            .scale(0.5)
        dot_4 = LabeledDot(Tex(r"4", color = BLACK), color = RED)\
            .move_to(ar_4.point_from_proportion(0.5))\
            .scale(0.5)            
        dot_5 = LabeledDot(Tex(r"5", color = BLACK), color = RED)\
            .move_to(ar_5.point_from_proportion(0.5))\
            .scale(0.5)
        dot_6 = LabeledDot(Tex(r"6", color = BLACK), color = RED)\
            .move_to(ar_6.point_from_proportion(0.5))\
            .scale(0.5)            
        dot_7 = LabeledDot(Tex(r"7", color = BLACK), color = RED)\
            .move_to(ar_7.point_from_proportion(0.5))\
            .scale(0.5) 
        dot_8 = LabeledDot(Tex(r"8", color = BLACK), color = RED)\
            .move_to(RIGHT*rec_6.get_top()[0]+UP*start.get_left()[1])\
            .scale(0.5)       
        self.add(
            group_start_text,
            group_1, group_2, group_3, group_4, group_5, group_6,
            ar_1, ar_2, ar_3, ar_4, ar_5, ar_6, ar_7, ar_8, l_7_8,
            dot_1, dot_2, dot_3, dot_4, dot_5, dot_6, dot_7, dot_8
            )
        self.wait()