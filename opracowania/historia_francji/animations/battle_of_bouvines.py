from manim import *

class BouvinesBattleScene(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#FAF9F6"
        
        # Title
        title = Text("Bitwa pod Bouvines (27 lipca 1214 r.)", font_size=28, color="#1F3A60", font="Georgia", weight=BOLD)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title))
        self.wait(0.5)
        
        # Tactical Map borders/labels
        map_rect = Rectangle(width=10, height=4.5, stroke_color="#475569", stroke_width=2)
        map_rect.move_to(0.5 * DOWN)
        self.play(Create(map_rect))
        
        # Labels for North/South
        north_label = Text("PÓŁNOC (Koalicja)", font_size=12, color="#A6242A", font="Georgia", weight=BOLD).next_to(map_rect, UP, buff=0.1)
        south_label = Text("POŁUDNIE (Francja)", font_size=12, color="#1F3A60", font="Georgia", weight=BOLD).next_to(map_rect, DOWN, buff=0.1)
        self.play(FadeIn(north_label), FadeIn(south_label))
        
        # Create French Forces (Blue)
        french_color = "#1F3A60"
        fr_left = Rectangle(width=2.0, height=0.6, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(2 * LEFT + 1.8 * DOWN)
        fr_center = Rectangle(width=2.5, height=0.6, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(0 * LEFT + 1.8 * DOWN)
        fr_right = Rectangle(width=2.0, height=0.6, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(2 * RIGHT + 1.8 * DOWN)
        
        lbl_fr_left = Text("Champagne", font_size=10, color="#FFFFFF", font="Georgia").move_to(fr_left.get_center())
        lbl_fr_center = Text("Filip II August", font_size=10, color="#FFFFFF", font="Georgia", weight=BOLD).move_to(fr_center.get_center())
        lbl_fr_right = Text("Burgundia", font_size=10, color="#FFFFFF", font="Georgia").move_to(fr_right.get_center())
        
        french_group = VGroup(fr_left, fr_center, fr_right, lbl_fr_left, lbl_fr_center, lbl_fr_right)
        
        # Create Coalition Forces (Red)
        coalition_color = "#A6242A"
        co_right = Rectangle(width=2.0, height=0.6, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(2 * LEFT + 0.8 * UP)
        co_center = Rectangle(width=2.5, height=0.6, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(0 * LEFT + 0.8 * UP)
        co_left = Rectangle(width=2.0, height=0.6, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(2 * RIGHT + 0.8 * UP)
        
        lbl_co_right = Text("Boulogne / Salisbury", font_size=9, color="#FFFFFF", font="Georgia").move_to(co_right.get_center())
        lbl_co_center = Text("Cesarz Otton IV", font_size=10, color="#FFFFFF", font="Georgia", weight=BOLD).move_to(co_center.get_center())
        lbl_co_left = Text("Flandria", font_size=10, color="#FFFFFF", font="Georgia").move_to(co_left.get_center())
        
        coalition_group = VGroup(co_right, co_center, co_left, lbl_co_right, lbl_co_center, lbl_co_left)
        
        # Display forces
        self.play(FadeIn(french_group, shift=UP), FadeIn(coalition_group, shift=DOWN))
        self.wait(1)
        
        # Phase 1: Attack of French Right on Coalition Left (Flandria)
        explanation = Text("Faza 1: Atak prawego skrzydła francuskiego rozbija Flandrię", font_size=14, color="#1F3A60", font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation))
        
        arrow_r = Arrow(start=2*RIGHT + 1.2*DOWN, end=2*RIGHT + 0.2*UP, color="#1F3A60", stroke_width=4)
        self.play(GrowArrow(arrow_r))
        self.wait(0.5)
        
        # Move Burgundy up and Flandria breaks
        self.play(
            fr_right.animate.move_to(2 * RIGHT + 0.2 * UP),
            lbl_fr_right.animate.move_to(2 * RIGHT + 0.2 * UP),
            co_left.animate.move_to(3.5 * RIGHT + 1.5 * UP).set_opacity(0.4),
            lbl_co_left.animate.move_to(3.5 * RIGHT + 1.5 * UP).set_opacity(0.4),
            FadeOut(arrow_r),
            run_time=1.5
        )
        self.wait(1)
        
        # Phase 2: Central Clash
        self.play(FadeOut(explanation))
        explanation_2 = Text("Faza 2: Starcie w centrum. Otton IV ucieka z pola bitwy", font_size=14, color="#1F3A60", font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation_2))
        
        arrow_c1 = Arrow(start=0.3*LEFT + 1.2*DOWN, end=0.3*LEFT + 0.2*DOWN, color="#1F3A60", stroke_width=4)
        arrow_c2 = Arrow(start=0.3*RIGHT + 0.2*UP, end=0.3*RIGHT + 0.2*DOWN, color="#A6242A", stroke_width=4)
        self.play(GrowArrow(arrow_c1), GrowArrow(arrow_c2))
        self.wait(0.5)
        
        # Move centers to clash, then Otto IV retreats
        self.play(
            fr_center.animate.move_to(0 * LEFT + 0.5 * DOWN),
            lbl_fr_center.animate.move_to(0 * LEFT + 0.5 * DOWN),
            co_center.animate.move_to(0 * LEFT + 0.1 * UP),
            lbl_co_center.animate.move_to(0 * LEFT + 0.1 * UP),
            FadeOut(arrow_c1), FadeOut(arrow_c2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Emperor flees
        escape_arrow = Arrow(start=0.1*UP, end=3*UP, color="#A6242A", stroke_width=4)
        self.play(GrowArrow(escape_arrow))
        self.play(
            co_center.animate.move_to(3 * UP).set_opacity(0),
            lbl_co_center.animate.move_to(3 * UP).set_opacity(0),
            FadeOut(escape_arrow),
            run_time=1.5
        )
        self.wait(1)
        
        # Phase 3: Encirclement of Coalition Right (Boulogne)
        self.play(FadeOut(explanation_2))
        explanation_3 = Text("Faza 3: Skrzydło Boulogne zostaje otoczone i kapituluje", font_size=14, color="#1F3A60", font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation_3))
        
        # French Right (Burgundy) sweeps left
        arrow_sweep = ArcBetweenPoints(start=2*RIGHT + 0.2*UP, end=1*LEFT + 0.8*UP, color="#1F3A60", stroke_width=4)
        self.play(Create(arrow_sweep))
        
        self.play(
            fr_right.animate.move_to(1.5 * LEFT + 0.2 * UP),
            lbl_fr_right.animate.move_to(1.5 * LEFT + 0.2 * UP),
            fr_left.animate.move_to(2.5 * LEFT + 0.2 * UP),
            lbl_fr_left.animate.move_to(2.5 * LEFT + 0.2 * UP),
            FadeOut(arrow_sweep),
            run_time=1.5
        )
        
        self.play(
            co_right.animate.scale(0.8).set_color("#475569"),
            lbl_co_right.animate.scale(0.8).set_opacity(0.5),
            run_time=1.0
        )
        self.wait(1)
        
        # Final Summary
        self.play(FadeOut(explanation_3))
        summary = Text(
            "Zwycięstwo pod Bouvines umocniło monarchię kapetyńską\ni zapoczątkowało zjednoczenie ziem francuskich.", 
            font_size=15, 
            color="#1F3A60", 
            font="Georgia"
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(summary))
        self.wait(3.5)
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(map_rect),
            FadeOut(north_label),
            FadeOut(south_label),
            FadeOut(french_group),
            FadeOut(coalition_group),
            FadeOut(summary)
        )
        self.wait(0.5)
