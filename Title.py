from manim import *

# ---- TEXT
class title(Scene):
    def construct(self):
        title = Text("Tam thức bậc hai", font= "Calibri (Body)")\
            .to_edge(UP, buff=0.5).scale(0.7)

        line_title = Line(ORIGIN, RIGHT*(title.get_width()+6), stroke_width = 1, color=RED)\
            .next_to(title, DOWN, buff=0.1)
        line_title_2 = line_title.copy()\
            .next_to(line_title, DOWN, buff=0.05)

        intro = Text("Chúng ta sẽ học về tam thức bậc hai, đồ thị của nó \n"\
            " và ứng dụng của tam thức bậc hai trong thực tế", 
            font = "UVN Banh Mi", line_spacing= 0.8)\
                .scale(0.4).next_to(line_title, DOWN, buff = 0.8)\
                .set_color([PURE_GREEN, YELLOW_C])       

        main = Paragraph(
            "NỘI DUNG CHÍNH:", 
            "\t1. Định nghĩa tam thức bậc hai",
            "\t2. Đồ thị", 
            "\t3. Trực đối xứng, đỉnh, bảng giá trị, đỉnh, cách vẽ đồ thị",
            "\t4. Thực hành vẽ",
            font = "Arial", line_spacing=0.8)\
                .scale(0.5).next_to(intro, DOWN, buff= 1)

        paragraph = Paragraph('this is a awesome', 'paragraph',
                      'With \nNewlines', '\tWith Tabs',
                      '  With Spaces', 'With Alignments',
                      'center', 'left', 'right')    

        self.add(title, line_title, line_title_2, intro)
        self.add(main)
        # self.add(paragraph)
        self.wait()