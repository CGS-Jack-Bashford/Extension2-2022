from manim import *
from manim.utils.color import Colors

class ExtensionTwo(Scene):

	def construct(self):

		MathTex.set_default(font_size=72)

		defaultTimeout = 3
		play_kw = { "run_time": 1.25, "transform_mismatches": True }

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

		self.play(Write(lines[0]), **play_kw)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[0], lines[1], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[1], lines[2], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[2], lines[3], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[3], lines[4], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[4].copy(), lines[5], **play_kw
			)
		)
		self.wait(3)
		self.play(
			TransformMatchingTex(
				VGroup(lines[4], lines[5]), lines[0], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[0], lines[6], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[6], lines[7], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[7], lines[8], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[8].copy(), lines[9], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			Unwrite(
				VGroup(lines[8], lines[9]), **play_kw
			)
		)
		self.wait(defaultTimeout)

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

		brace1 = Brace(lines[0], RIGHT, sharpness=1.0)

		self.play(
			Write(
				VGroup(lines[0], brace1, lines[1]), **play_kw
			)
		)
		self.wait(defaultTimeout)
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
		self.wait(defaultTimeout)
		self.play(
			FadeOut(
				VGroup(lines[2], lines[3], brace2, brace3), **play_kw, shift=DOWN
			)
		)

		# # Begin Midy's Theorem

		self.wait(defaultTimeout)
		lines = VGroup(
			Tex("Etienne Midy (1775-1846)").shift(UP * 3),
			MathTex(r"p \in \mathbb{P}"),
			MathTex(r"p \notin {2,5}"),
			MathTex(r"\frac{1}{p} = 0.\overline{a_{1}a_{2}a_{3}\ldots a_{2k}}"),
			MathTex(r"a_{1}a_{2}a_{3}a_{4}\ldots a_{k}\\ \underline{+a_{k+1}a_{k+2}\ldots a_{2k}}"),
			MathTex(r"m(10^k - 1)", color=BLUE_D).shift(DOWN * 1.8),
			MathTex(r"m(999\ldots 999), m \in \mathbb{N}", color=BLUE_D).shift(DOWN * 1.8),
			MathTex(r"142\\\ \underline{+857}").shift(LEFT * 4),
			MathTex(r"999", color=BLUE_D).shift(DOWN * 1.65, LEFT * 4),
			MathTex(r"52631578\\\ \underline{+947368421}").shift(RIGHT * 3),
			MathTex(r"9999999999", color=BLUE_D).shift(DOWN * 1.65, RIGHT * 3)
		)

		#lines.arrange(DOWN, buff=LARGE_BUFF)

		self.play(
			Write(
				lines[0], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			Write(
				lines[1], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[1], lines[2], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[2], lines[3], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[3], lines[4], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[4].copy(), lines[5], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[5], lines[6], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				VGroup(lines[6], lines[4]), VGroup(lines[7], lines[8], lines[9], lines[10]), **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			Unwrite(
				VGroup(lines[0], lines[7:11]), **play_kw
			)
		)
		self.wait(defaultTimeout)
		lines = VGroup(
			MathTex(r"\frac{a}{b},a<b").shift(LEFT * 4),
			MathTex(r"gcd(a,b)=1").shift(DOWN * 2, LEFT * 4),
			MathTex(r"0.a_{1}a_{2}\ldots a_{k}").shift(UP * 2, RIGHT * 3),
			MathTex(r"0.\overline{a_{1}a_{2}\ldots a_{k}}").shift(DOWN * 2, RIGHT * 3),
			MathTex(r"0.a_{1}a_{2}\ldots a_{k}").shift(UP * 3),
			MathTex(r"x=0.a_{1}a_{2}\ldots a_{k}").shift(UP * 3),
			MathTex(r"10^k\times x=a_{1}a_{2}\ldots a_{k}").shift(UP * 2),
			MathTex(r"x=\frac{a_{1}a_{2}\ldots a_{k}}{10^k}").shift(UP * 0.5),
			MathTex(r"a_{1}a_{2}\ldots a_{k}\in \mathbb{Z}\\ 10^k\in \mathbb{Z}").shift(DOWN * 1.5),
			MathTex(r"\Rightarrow x\in \mathbb{Q}").shift(DOWN * 1.3),
			MathTex(r"0.\overline{a_{1}a_{2}\ldots a_{k}}").shift(UP * 3),
			MathTex(r"x=0.\overline{a_{1}a_{2}\ldots a_{k}}").shift(UP * 3),
			MathTex(r"10^k\times x=a_{1}a_{2}\ldots a_{k}.\overline{a_{1}a_{2}\ldots a_{k}}").shift(UP * 2),
			MathTex(r"x(10^k - 1)=a_{1}a_{2}\ldots a_{k}").shift(UP * 0.5),
			MathTex(r"x=\frac{a_{1}a_{2}\ldots a_{k}}{10^k - 1}").shift(UP * 0.5),
			MathTex(r"a_{1}a_{2}\ldots a_{k}\in \mathbb{Z}\\ 10^k - 1\in \mathbb{Z}").shift(DOWN * 1.5),
			MathTex(r"\Rightarrow x\in \mathbb{Q}").shift(DOWN * 1.3),
			MathTex(r"\therefore 0.a_{1}a_{2}\ldots a_{k}\in \mathbb{Q},\\0.\overline{a_{1}a_{2}\ldots a_{k}}\in \mathbb{Q}")
		)

		self.play(
			Write(
				VGroup(lines[0], lines[1]), **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				VGroup(lines[0], lines[1]).copy(), VGroup(lines[2], lines[3]), **play_kw
			)
		)
		self.wait(defaultTimeout)
		frameBox1 = SurroundingRectangle(lines[2], buff=0.1)
		frameBox2 = SurroundingRectangle(lines[4], buff=0.1)

		self.play(
			Create(
				frameBox1, **play_kw
			),
		)
		self.wait(defaultTimeout)
		self.play(
			FadeOut(
				VGroup(lines[0], lines[1]), shift=LEFT, **play_kw
			),
			FadeOut(
				lines[3], shift=DOWN, **play_kw
			),
			ReplacementTransform(
				frameBox1, frameBox2, **play_kw
			),
			ReplacementTransform(
				lines[2], lines[4], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[4], lines[5], **play_kw
			),
			Uncreate(
				frameBox2, **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[5].copy(), lines[6], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[6].copy(), lines[7], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[7].copy(), lines[8], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[8], lines[9], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[9], lines[2], **play_kw
			),
			FadeOut(
				VGroup(lines[5], lines[6], lines[7]), shift=DOWN, **play_kw
			),
			FadeIn(
				lines[3], shift=UP, **play_kw
			),
			FadeIn(
				VGroup(lines[0], lines[1]), shift=RIGHT, **play_kw
			)
		)
		self.wait(defaultTimeout)
		frameBox1 = SurroundingRectangle(lines[3], buff=0.1)
		frameBox2 = SurroundingRectangle(lines[10], buff=0.1)

		self.play(
			Create(
				frameBox1, **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			FadeOut(
				VGroup(lines[0], lines[1]), shift=LEFT, **play_kw
			),
			FadeOut(
				lines[2], shift=UP, **play_kw
			),
			ReplacementTransform(
				frameBox1, frameBox2, **play_kw
			),
			ReplacementTransform(
				lines[3], lines[10], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			Uncreate(
				frameBox2, **play_kw
			),
			TransformMatchingTex(
				lines[10], lines[11], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[11].copy(), lines[12], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[12].copy(), lines[13], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[13], lines[14], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[14].copy(), lines[15], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[15], lines[16], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[16], lines[17], **play_kw
			),
			FadeOut(
				VGroup(lines[14], lines[12], lines[11]), shift=DOWN, run_time=(play_kw["run_time"]*2/3)
			)
		)
		self.wait(defaultTimeout)
		self.play(
			Unwrite(
				lines[17]
			)
		)
		self.wait(defaultTimeout)

		# Begin proof of prime number reciprocals

		lines = [
			MathTex(r"(a+1)^p"),
			MathTex(r"a^p + \binom{p}{1} a^{p-1} + \binom{p}{2} a^{p-2} + \ldots + \binom{p}{p-1} a^1 + 1", font_size=60).shift(UP),
			MathTex(r"(a+1)^p \equiv a^p + 1 \textrm{ } (\textrm{mod } p)").shift(UP),
			MathTex(r"(a+1)^p - (a+1) \equiv a^p - a \textrm{ } (\textrm{mod } p) \ast"),
			MathTex(r"\underline{(1^p - 1) | p}"),
			MathTex(r"(n^p - n) | p"),
			MathTex(r"\textrm{ }\ast (n+1)^p - (n+1) \equiv n^p - n \textrm{ } (\textrm{mod } p) \textrm{ }\ast").shift(DOWN),
			MathTex(r"\Rightarrow a^p - a \equiv 0 \textrm{ } (\textrm{mod } p)").shift(DOWN),
			MathTex(r"\therefore a^p \equiv a \textrm{ } (\textrm{mod } p)").shift(DOWN * 2)
		]

		self.play(
			Write(
				lines[0], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[0], lines[1], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[1], lines[2], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[2].copy(), lines[3], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[3], lines[4], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[4], lines[5], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[5].copy(), lines[6], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[6], lines[7], **play_kw
			)
		)
		self.wait(defaultTimeout)
		self.play(
			TransformMatchingTex(
				lines[7].copy(), lines[8], **play_kw
			)
		)
		self.wait(defaultTimeout)