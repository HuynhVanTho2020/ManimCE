from manim import *

class Table_Mobject_v2(MovingCameraScene):
    def construct(self):
        text_tab = Text("Bảng nguyên hàm thường gặp", font= "Calibri (Body)").scale(0.5)
        text_tab.to_edge(UP, buff= 1)
        text_tab.set_color_by_gradient(PURE_GREEN, YELLOW_C)
        line_text_tab_1 = Underline(text_tab, buff=0.1, color = RED, stroke_width=1)
        line_text_tab_2 = Underline(text_tab, buff=0.13, color = RED, stroke_width=1)

        k = 0.5
        f_1 = MathTex(r"\int 0\, \mathrm{d}x = C").scale(k)
        f_2 = MathTex(r"\int 1\, \mathrm{d}x = x+ C").scale(k)
        f_3 = MathTex(r"\int x^{\alpha}\, \mathrm{d}x =\frac{x^{\alpha+1}}{\alpha+1}+C, \,\alpha \ne -1").scale(k)
        f_4 = MathTex(r"\int \frac{1}{x}\, \mathrm{d}x = \ln |x| +C").scale(k)
        f_5 = MathTex(r"\int \frac{1}{x^2}\, \mathrm{d}x = -\frac{1}{x} +C").scale(k)
        f_6 = MathTex(r"\int \mathrm{e}^x\, \mathrm{d}x = \mathrm{e}^x +C").scale(k)

        ff_1 = MathTex(r"\int a^x\, \mathrm{d}x = \frac{a^x}{\ln a}+C, \, 0<a\ne 1").scale(k)
        ff_2 = MathTex(r"\int \frac{1}{2\sqrt{x}}\, \mathrm{d}x = \sqrt{x} +C").scale(k)
        ff_3 = MathTex(r"\int \cos x\,  \mathrm{d}x = \sin x+ C").scale(k)
        ff_4 = MathTex(r"\int \sin x\,  \mathrm{d}x = -\cos x+C").scale(k)
        ff_5 = MathTex(r"\int \frac{1}{\cos^2 x}\, \mathrm{d} x = \tan x +C").scale(k)
        ff_6 = MathTex(r"\int \frac{1}{\sin^2 x}\, \mathrm{d} x = -\cot x +C").scale(k)

        tab = MobjectTable(
            [
            [MathTex("1").scale(k), f_1, MathTex("7").scale(k), ff_1],
            [MathTex("2").scale(k), f_2, MathTex("8").scale(k), ff_2],
            [MathTex("3").scale(k), f_3, MathTex("9").scale(k), ff_3],
            [MathTex("4").scale(k), f_4, MathTex("10").scale(k), ff_4],
            [MathTex("5").scale(k), f_5, MathTex("11").scale(k), ff_5],
            [MathTex("6").scale(k), f_6, MathTex("12").scale(k), ff_6],
            ], include_outer_lines = True,
            v_buff = 0.3,
            h_buff = 0.5,
            line_config={"stroke_width": 1.5},
            arrange_in_grid_config={"cell_alignment": LEFT}
        )
        tab.set_column_colors([RED,BLUE,GREEN], [PURE_GREEN, YELLOW_C], [RED,BLUE,GREEN], [PURE_GREEN, YELLOW_C])
        tab.next_to(text_tab,DOWN, buff=0.5)
        # for i in range(0,4):
        tab.get_vertical_lines().set_color(BLUE_C)
        tab.get_horizontal_lines().set_color(TEAL_D)

        background = Rectangle(width=tab.get_width(), height= tab.get_height(), stroke_width=0)
        background.set_fill(opacity=0.1)
        background.set_color_by_gradient([GREEN_C, RED_A, WHITE, YELLOW_C])
        background.move_to(tab)
        self.add(background)

        self.play(Write(text_tab), Create(line_text_tab_1), Create(line_text_tab_2), run_time = 2)
        self.play(tab.create(), run_time = 20)
        self.wait()
        self.camera.frame.save_state()
        for i in [2, 4]:
            for j in range(1,7):
                self.play(self.camera.frame.animate.move_to(tab.get_cell((j,i)).get_center()).set(width = 4))
                self.wait(1.5)
        self.play(Restore(self.camera.frame))        


        
        
        # self.play(self.camera.frame.animate.move_to(tab.get_cell((2,2)).get_center()).set(width =tab.get_cell((2,2)).get_width()*2))
        # self.wait(0.5)

        
