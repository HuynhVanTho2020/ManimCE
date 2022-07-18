from manim import *
# import numpy as np
class intro(Scene):
	def construct(self):
		r = 2.3
		r_right = 6
		tri = Triangle(radius = r, stroke_width=2.5, fill_color=BLUE, fill_opacity=0.3)		
		A, B, C = tri.get_vertices()
		# A = tri.get_vertices()[0]
		# B = tri.get_vertices()[1]
		# C = tri.get_vertices()[2]
		# ---
		M =  Dot(radius=0.06)
		# ---
		I = Dot(fill_opacity=0)\
			.add_updater(lambda m: m.become(Dot(Line(B, C).get_projection(M.get_center()),fill_opacity=0)))
		J = Dot(fill_opacity=0)\
			.add_updater(lambda m: m.become(Dot(Line(C, A).get_projection(M.get_center()),fill_opacity=0)))
		K = Dot(fill_opacity=0)\
			.add_updater(lambda m: m.become(Dot(Line(A, B).get_projection(M.get_center()),fill_opacity=0)))
		# ---
		MI = Line(M.get_center(), I.get_center(), stroke_width=2, color=PURE_RED)\
			.add_updater(lambda m: m.become(Line(M.get_center(), I.get_center(), stroke_width=2, color=PURE_RED)))
		MI_r = Line(B+RIGHT*r_right,B+RIGHT*r_right+MI.get_length()*UP, stroke_width=2, color=PURE_RED)\
			.add_updater(lambda m: m.become(Line(B+RIGHT*r_right,B+RIGHT*r_right+MI.get_length()*UP, stroke_width=2, color=PURE_RED)))

		MJ = Line(M.get_center(), J.get_center(), stroke_width=2, color=YELLOW_C)\
			.add_updater(lambda m: m.become(Line(M.get_center(), J.get_center(), stroke_width=2, color=YELLOW_C)))
		MJ_r = Line(MI_r.get_end(),MI_r.get_end()+UP*MJ.get_length(), stroke_width=2, color=YELLOW_C)\
			.add_updater(lambda m: m.become(Line(MI_r.get_end(),MI_r.get_end()+UP*MJ.get_length(), stroke_width=2, color=YELLOW_C)))

			
		MK = Line(M.get_center(), K.get_center(), stroke_width=2, color=PURE_GREEN)\
			.add_updater(lambda m: m.become(Line(M.get_center(), K.get_center(), stroke_width=2, color=PURE_GREEN)))
		MK_r = Line(MJ_r.get_end(), MJ_r.get_end()+UP*MK.get_length(), stroke_width=2, color=PURE_GREEN)\
			.add_updater(lambda m: m.become(Line(MJ_r.get_end(), MJ_r.get_end()+UP*MK.get_length(), stroke_width=2, color=PURE_GREEN)))
		dotM = Dot(color = WHITE)
		# --- Các tam giác đều
		M1 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,B).get_unit_vector(), stroke_width=3)))
		M2 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,C).get_unit_vector(), stroke_width=3)))
		tri1 = Polygon(M.get_center(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,B).get_unit_vector(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,C).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE,stroke_width=3)
		tri1.add_updater(lambda t : t.become(Polygon(M.get_center(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,B).get_unit_vector(), M.get_center() + 2*MI.get_length()/np.sqrt(3)*Line(A,C).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE, stroke_width=3)))

		M3 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,A).get_unit_vector(), stroke_width=3)))
		M4 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,B).get_unit_vector(), stroke_width=3)))
		tri2 = Polygon(M.get_center(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,A).get_unit_vector(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,B).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE,stroke_width=3)
		tri2.add_updater(lambda t : t.become(Polygon(M.get_center(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,A).get_unit_vector(), M.get_center() + 2*MK.get_length()/np.sqrt(3)*Line(C,B).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE, stroke_width=3)))

		M5 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B,C).get_unit_vector(), stroke_width=3)))
		M6 = Line(stroke_width=3).add_updater(lambda l: l.become(Line(M.get_center(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B,A).get_unit_vector(), stroke_width=3)))
		tri3 = Polygon(M.get_center(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B,C).get_unit_vector(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B,A).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE,stroke_width=3)
		tri3.add_updater(lambda t : t.become(Polygon(M.get_center(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B,C).get_unit_vector(), M.get_center() + 2*MJ.get_length()/np.sqrt(3)*Line(B, A).get_unit_vector(), fill_opacity=0.2, fill_color=WHITE, stroke_width=3)))
		# self.add(NumberPlane())
		self.add(
				tri,
				# Dot(A), # Hướng 90 độ
				# MK,
				M,
				I,
				J,
				K,
				MI, 
				MI_r,
		)
		self.play(*[Create(i) for i in [MI, MI_r]], run_time=2)
		self.wait()
		self.add(MJ, MJ_r)
		self.play(*[Create(i) for i in [MJ, MJ_r]], run_time=2)
		self.wait()
		self.add(MK, MK_r)
		self.play(*[Create(i) for i in [MK, MK_r]], run_time=2)
		self.play(M.animate.shift(UP*2), run_time=3, rate_func=there_and_back)
		self.play(M.animate.shift(LEFT*1.1), run_time=3)
		self.play(M.animate.shift(2.1*Line(B,A).get_unit_vector()), run_time=3)
		self.play(M.animate.shift(3*Line(A,C).get_unit_vector()), run_time=3)
		self.play(M.animate.shift(LEFT*2.5+UP*0.5), run_time=3)
		self.play(M.animate.shift(RIGHT*1.5+UP*0.5), run_time=2)
		self.wait()
		# ---
		self.play(*[Create(i) for i in [M1, M2]], run_time=2)
		self.wait()
		# self.add(tri1)
		self.play(GrowFromEdge(tri1, UP), run_time = 2)
		self.wait()
		self.play(*[Create(i) for i in [M3, M4]], run_time=2)
		self.wait()
		self.play(GrowFromEdge(tri2, UP), run_time = 2)
		self.wait()
		self.play(*[Create(i) for i in [M5, M6]], run_time=2)
		self.wait()
		self.play(GrowFromEdge(tri3, UP), run_time = 2)
		self.wait()
		self.play(tri1.animate.shift(LEFT), run_time=2)
		self.wait()


		





