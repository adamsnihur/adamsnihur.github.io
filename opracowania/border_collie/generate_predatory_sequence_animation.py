from manim import *

class PredatorySequenceScene(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#FAF9F6"
        
        # Title
        title = Text("Modyfikacja łańcucha łowieckiego", font_size=32, color="#5B21B6", font="Georgia")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)
        
        # Wolf Title
        wolf_title = Text("ŁAŃCUCH DZIKI (Wilk):", font_size=20, color="#1E293B", weight=BOLD, font="Georgia").move_to(2.0 * UP + 4.5 * LEFT)
        self.play(Write(wolf_title))
        
        # Wolf steps
        wolf_steps = ["Węszenie", "Oko (Eye)", "Podchód", "Pogoń", "Chwycenie", "Zabicie"]
        wolf_group = VGroup()
        for idx, step in enumerate(wolf_steps):
            box = Rectangle(width=1.8, height=0.8, stroke_color="#475569", fill_color="#E2E8F0", fill_opacity=0.8)
            label = Text(step, font_size=12, color="#1E293B", font="Georgia")
            label.move_to(box.get_center())
            step_v = VGroup(box, label)
            step_v.move_to(1.0 * UP + (idx * 2.2 - 5.5) * RIGHT)
            wolf_group.add(step_v)
            self.play(FadeIn(step_v, shift=DOWN), run_time=0.3)
            if idx < len(wolf_steps) - 1:
                arrow = Arrow(start=step_v.get_right(), end=step_v.get_right() + 0.4 * RIGHT, color="#475569", stroke_width=2)
                self.play(GrowArrow(arrow), run_time=0.2)
                
        self.wait(1)
        
        # Border Collie Title
        collie_title = Text("ŁAŃCUCH ZMODYFIKOWANY (Border Collie):", font_size=20, color="#0D9488", weight=BOLD, font="Georgia").move_to(1.0 * DOWN + 2.5 * LEFT)
        self.play(Write(collie_title))
        
        # Collie steps
        collie_group = VGroup()
        for idx, step in enumerate(wolf_steps):
            box = Rectangle(width=1.8, height=0.8, stroke_color="#475569", fill_color="#E2E8F0", fill_opacity=0.8)
            label = Text(step, font_size=12, color="#1E293B", font="Georgia")
            label.move_to(box.get_center())
            step_v = VGroup(box, label)
            step_v.move_to(2.0 * DOWN + (idx * 2.2 - 5.5) * RIGHT)
            collie_group.add(step_v)
            self.play(FadeIn(step_v, shift=DOWN), run_time=0.3)
            if idx < len(wolf_steps) - 1:
                arrow = Arrow(start=step_v.get_right(), end=step_v.get_right() + 0.4 * RIGHT, color="#475569", stroke_width=2)
                self.play(GrowArrow(arrow), run_time=0.2)
                
        self.wait(1)
        
        # Highlight herding adaptation (First 3 steps)
        self.play(
            collie_group[0][0].animate.set_stroke(color="#0D9488", width=3).set_fill(color="#CCFBF1", opacity=0.9),
            collie_group[1][0].animate.set_stroke(color="#0D9488", width=4).set_fill(color="#CCFBF1", opacity=0.9),
            collie_group[2][0].animate.set_stroke(color="#0D9488", width=4).set_fill(color="#CCFBF1", opacity=0.9),
        )
        # Add brace under herding steps
        brace = Brace(VGroup(collie_group[0], collie_group[1], collie_group[2]), DOWN, color="#0D9488")
        brace_text = Text("Głębokie wzmocnienie instynktu", font_size=14, color="#0D9488", font="Georgia")
        brace_text.next_to(brace, DOWN)
        self.play(Create(brace), Write(brace_text))
        self.wait(1)
        
        # Controlled Chase
        self.play(
            collie_group[3][0].animate.set_stroke(color="#D97706", width=2).set_fill(color="#FEF3C7", opacity=0.8),
        )
        chase_brace_text = Text("Pod kontrolą gwizdka", font_size=10, color="#D97706", font="Georgia").next_to(collie_group[3], DOWN, buff=0.1)
        self.play(Write(chase_brace_text))
        self.wait(0.5)
        
        # Crossing out Grab and Kill in Collie
        x_grab_1 = Line(collie_group[4].get_corner(UL), collie_group[4].get_corner(DR), color="#DC2626", stroke_width=4)
        x_grab_2 = Line(collie_group[4].get_corner(UR), collie_group[4].get_corner(DL), color="#DC2626", stroke_width=4)
        
        x_kill_1 = Line(collie_group[5].get_corner(UL), collie_group[5].get_corner(DR), color="#DC2626", stroke_width=4)
        x_kill_2 = Line(collie_group[5].get_corner(UR), collie_group[5].get_corner(DL), color="#DC2626", stroke_width=4)
        
        self.play(
            Create(x_grab_1), Create(x_grab_2),
            Create(x_kill_1), Create(x_kill_2),
            collie_group[4][0].animate.set_stroke(color="#DC2626").set_fill(color="#FEE2E2", opacity=0.8),
            collie_group[5][0].animate.set_stroke(color="#DC2626").set_fill(color="#FEE2E2", opacity=0.8),
        )
        
        inhibition_text = Text("Pełne wygaszenie (inhibicja)", font_size=14, color="#DC2626", font="Georgia").next_to(VGroup(collie_group[4], collie_group[5]), DOWN, buff=0.2)
        self.play(Write(inhibition_text))
        self.wait(3.5)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)
