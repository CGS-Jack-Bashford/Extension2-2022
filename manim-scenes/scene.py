from manim import *
from manim.utils.color import Colors

class ExtensionTwo(Scene):

	def construct(self):

		MathTex.set_default(font_size=72)

		defaultTimeout = 0.5

		lines = [
			MathTex(r"\frac{1}{7}"),
			MathTex(r"\frac{1}{7}=0.142857142857142857\ldots"),
			MathTex(r"\frac{1}{7}=0.\overline{142857}"),
			MathTex(r"142 + 857"),
			MathTex(r"142\\\ \underline{+857}"),
			MathTex(r"999", color=BLUE_D).shift(DOWN * 1.65),
			MathTex(r"\frac{1}{19}", font_size=72),
			MathTex(r"0.\overline{052631578947368421}"),
			MathTex(r"52631578\\\ \underline{+947368421}"),
			MathTex(r"9999999999", color=BLUE_D).shift(DOWN * 1.65),
		]

		play_kw = { "run_time": 1.25, "transform_mismatches": True }

		# self.play(Write(lines[0]), **play_kw)
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[0], lines[1], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[1], lines[2], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[2], lines[3], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[3], lines[4], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[4].copy(), lines[5], **play_kw
		# 	)
		# )
		# self.wait(3)
		# self.play(
		# 	TransformMatchingTex(
		# 		VGroup(lines[4], lines[5]), lines[0], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[0], lines[6], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[6], lines[7], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[7], lines[8], **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[8].copy(), lines[9], **play_kw
		# 	)
		# )
		# self.play(
		# 	Unwrite(
		# 		VGroup(lines[8], lines[9]), **play_kw
		# 	)
		# )
		# self.wait(defaultTimeout)

		lines = [
			VGroup(
				MathTex(r"7"),
				MathTex(r"19")
			),
			MathTex(r"\in\mathbb{P}"),
			VGroup(
				MathTex(r"\frac{1}{7}=0.\overline{142857}"),
				MathTex(r"\frac{1}{19}=0.\overline{052631578947368421}")
			),
			VGroup(
				Tex(r"6 digits"),
				Tex(r"18 digits")
			)
		]

		lines[0].arrange(DOWN, buff=LARGE_BUFF).shift(LEFT * 4)
		lines[1].shift(LEFT * 2.35)
		lines[2].arrange(DOWN, buff=2, center=False, aligned_edge=LEFT).shift(LEFT * 3.2, UP * 1.5)
		#lines[2][1].align_to(lines[2][0])

		brace1 = Brace(lines[0], RIGHT, sharpness=1.0)

		self.play(
			Write(
				VGroup(lines[0], brace1, lines[1]), **play_kw
			)
		)
		
		brace2 = Brace(lines[2][0], UP, sharpness=1.0)
		brace3 = Brace(lines[2][1], UP, sharpness=1.0)

		brace2.put_at_tip(lines[3][0])
		brace3.put_at_tip(lines[3][1])

		self.play(
			TransformMatchingTex(
				lines[0][0], lines[2][0], **play_kw
			),
			TransformMatchingTex(
				lines[0][1], lines[2][1], **play_kw
			),
			TransformMatchingShapes(
				VGroup(lines[1], brace1), lines[3], **play_kw
			),
			Write(
				VGroup(brace2, brace3), run_time=play_kw["run_time"]*1.5
			)
		)

		self.play(
			FadeOut(
				VGroup(lines[2], lines[3], brace2, brace3), **play_kw, shift=DOWN
			)
		)