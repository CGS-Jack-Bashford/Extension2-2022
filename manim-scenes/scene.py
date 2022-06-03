from manim import *

class ExtensionTwo(Scene):
	def construct(self):

		variables = VGroup(MathTex("142"), MathTex("857")).arrange_submobjects().shift(UP)

		lines = [
			MathTex(r"{{142}}", r"{{857}}"),
			MathTex(r"{{142}}", r"\quad", r"{{857}}"),
			MathTex(r"{{142}}", r"\\\underline{857}")
		]

		differentLines = [
			MathTex(r"\overline{142857}"),
			MathTex(r"\overline{142\quad 857}"),
			MathTex(r"142\\\ \underline{+857}")
		]

		play_kw = { "run_time": 2 }

		# self.play(Write(lines[0]), **play_kw)

		# self.play(
		# 	TransformMatchingTex(
		# 		lines[0], lines[1],
		# 	),
		# 	**play_kw
		# )
		# self.wait()
		# self.play(
		# 	TransformMatchingTex(
		# 		lines[1], lines[2],
		# 		transform_mismatches=True
		# 	),
		# 	**play_kw
		# )

		self.play(Write(differentLines[0]), **play_kw)
		self.wait()
		self.play(
			TransformMatchingShapes(
				differentLines[0], differentLines[1], **play_kw,
				transform_mismatches=True
			)
		)
		self.wait()
		self.play(
			TransformMatchingShapes(
				differentLines[1], differentLines[2], **play_kw,
				transform_mismatches=True
			)
		)