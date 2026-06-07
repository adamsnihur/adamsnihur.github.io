from manim import *

class AusterlitzBattleScene(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#FAF9F6"
        
        # Colors
        french_color = "#1F3A60"
        coalition_color = "#A6242A"
        neutral_color = "#475569"
        gold_color = "#D2A14E"
        pond_color = "#7DD3FC"
        
        # Title
        title = Text("Bitwa pod Austerlitz (2 grudnia 1805 r.)", font_size=26, color=french_color, font="Georgia", weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)
        
        # Tactical Map border
        map_rect = Rectangle(width=11, height=4.6, stroke_color=neutral_color, stroke_width=2)
        map_rect.move_to(0.4 * DOWN)
        self.play(Create(map_rect))
        
        # Key Terrain Features
        # Pratzen Heights (Center hill)
        pratzen_bg = Ellipse(width=3.5, height=1.8, stroke_color=gold_color, stroke_width=2, fill_color=gold_color, fill_opacity=0.15)
        pratzen_bg.move_to(0.5 * RIGHT + 0.2 * DOWN)
        pratzen_label = Text("Wzgórza Prackie", font_size=10, color=gold_color, font="Georgia", weight=BOLD).move_to(pratzen_bg.get_center())
        
        # Goldbach Stream (on the left side)
        goldbach_line = CurvedArrow(start_point=3.5*LEFT + 1.8*UP, end_point=3.8*LEFT + 2.5*DOWN, color=pond_color, stroke_width=4)
        goldbach_label = Text("potok Goldbach", font_size=9, color=neutral_color, font="Georgia", slant=ITALIC).next_to(goldbach_line, RIGHT, buff=0.1).shift(1.2*UP)
        
        # Frozen Ponds (bottom left)
        pond1 = Circle(radius=0.4, fill_color=pond_color, fill_opacity=0.6, stroke_color="#0284C7").move_to(3.2*LEFT + 1.8*DOWN)
        pond2 = Circle(radius=0.3, fill_color=pond_color, fill_opacity=0.6, stroke_color="#0284C7").move_to(2.4*LEFT + 2.0*DOWN)
        ponds_label = Text("zamarznięte stawy", font_size=8, color=neutral_color, font="Georgia").move_to(2.8*LEFT + 1.4*DOWN)
        
        self.play(
            FadeIn(pratzen_bg), FadeIn(pratzen_label),
            Create(goldbach_line), FadeIn(goldbach_label),
            FadeIn(pond1), FadeIn(pond2), FadeIn(ponds_label)
        )
        self.wait(0.5)
        
        # French Forces (Blue blocks, placed at the left/bottom-left)
        fr_lannes = Rectangle(width=1.6, height=0.5, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(3.5 * LEFT + 0.8 * UP)
        fr_soult = Rectangle(width=1.8, height=0.5, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(2.5 * LEFT + 0.6 * DOWN)
        fr_davout = Rectangle(width=1.2, height=0.5, fill_color=french_color, fill_opacity=0.8, stroke_color=french_color).move_to(3.4 * LEFT + 1.6 * DOWN)
        fr_guard = RegularPolygon(n=5, radius=0.3, fill_color=french_color, fill_opacity=0.9, stroke_color=gold_color).move_to(4.5 * LEFT + 0.8 * DOWN)
        
        lbl_fr_lannes = Text("Lannes", font_size=9, color="#FFFFFF", font="Georgia").move_to(fr_lannes.get_center())
        lbl_fr_soult = Text("Soult", font_size=9, color="#FFFFFF", font="Georgia", weight=BOLD).move_to(fr_soult.get_center())
        lbl_fr_davout = Text("Davout", font_size=8, color="#FFFFFF", font="Georgia").move_to(fr_davout.get_center())
        lbl_fr_guard = Text("N", font_size=10, color="#FFFFFF", font="Georgia", weight=BOLD).move_to(fr_guard.get_center())
        
        french_units = VGroup(fr_lannes, fr_soult, fr_davout, fr_guard, lbl_fr_lannes, lbl_fr_soult, lbl_fr_davout, lbl_fr_guard)
        
        # Coalition Forces (Red blocks, placed at the right/top-right)
        co_bagration = Rectangle(width=1.6, height=0.5, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(2.5 * RIGHT + 1.0 * UP)
        co_center = Rectangle(width=2.0, height=0.5, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(0.5 * RIGHT + 0.2 * DOWN) # on Pratzen
        co_left = Rectangle(width=1.8, height=0.5, fill_color=coalition_color, fill_opacity=0.8, stroke_color=coalition_color).move_to(2.0 * RIGHT + 0.8 * DOWN)
        
        lbl_co_bagration = Text("Bagration", font_size=9, color="#FFFFFF", font="Georgia").move_to(co_bagration.get_center())
        lbl_co_center = Text("Kutuzow", font_size=9, color="#FFFFFF", font="Georgia", weight=BOLD).move_to(co_center.get_center())
        lbl_co_left = Text("Buxhowden", font_size=9, color="#FFFFFF", font="Georgia").move_to(co_left.get_center())
        
        coalition_units = VGroup(co_bagration, co_center, co_left, lbl_co_bagration, lbl_co_center, lbl_co_left)
        
        self.play(FadeIn(french_units, shift=RIGHT), FadeIn(coalition_units, shift=LEFT))
        self.wait(1.0)
        
        # PHASE 1: Coalition Left attacks Davout (The Decoy Flank)
        explanation = Text("Faza 1: Kolumny koalicji schodzą ze Wzgórz, by rozbić słabego Davouta", font_size=13, color=french_color, font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation))
        
        arrow_allied_attack = Arrow(start=1.5*RIGHT + 0.7*DOWN, end=2.5*LEFT + 1.4*DOWN, color=coalition_color, stroke_width=4)
        self.play(GrowArrow(arrow_allied_attack))
        self.wait(0.5)
        
        # Move Buxhowden towards Davout
        self.play(
            co_left.animate.move_to(2.5 * LEFT + 1.4 * DOWN),
            lbl_co_left.animate.move_to(2.5 * LEFT + 1.4 * DOWN),
            fr_davout.animate.move_to(3.2 * LEFT + 1.4 * DOWN),
            lbl_fr_davout.animate.move_to(3.2 * LEFT + 1.4 * DOWN),
            FadeOut(arrow_allied_attack),
            run_time=2.0
        )
        self.wait(1.0)
        
        # PHASE 2: Soult attacks the empty Pratzen Heights
        self.play(FadeOut(explanation))
        explanation_2 = Text("Faza 2: Napoleon nakazuje korpusowi Soulta szturm na osłabione centrum", font_size=13, color=french_color, font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation_2))
        
        arrow_soult_attack = Arrow(start=1.8*LEFT + 0.4*DOWN, end=0.3*LEFT + 0.2*DOWN, color=french_color, stroke_width=4)
        self.play(GrowArrow(arrow_soult_attack))
        self.wait(0.5)
        
        # Move Soult to Pratzen Heights, Kutuzov retreats or is pushed
        self.play(
            fr_soult.animate.move_to(0.3 * LEFT + 0.2 * DOWN),
            lbl_fr_soult.animate.move_to(0.3 * LEFT + 0.2 * DOWN),
            co_center.animate.move_to(1.5 * RIGHT + 0.4 * UP).set_opacity(0.5),
            lbl_co_center.animate.move_to(1.5 * RIGHT + 0.4 * UP).set_opacity(0.5),
            FadeOut(arrow_soult_attack),
            run_time=2.0
        )
        self.wait(1.0)
        
        # PHASE 3: Encirclement and retreat through ponds
        self.play(FadeOut(explanation_2))
        explanation_3 = Text("Faza 3: Centrum rozbite. Soult okrąża lewe skrzydło koalicji przy stawach", font_size=13, color=french_color, font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        self.play(Write(explanation_3))
        
        # Soult sweeps down
        arrow_sweep = ArcBetweenPoints(start=0.3*LEFT + 0.2*DOWN, end=1.8*LEFT + 1.1*DOWN, color=french_color, stroke_width=4)
        self.play(Create(arrow_sweep))
        self.wait(0.5)
        
        self.play(
            fr_soult.animate.move_to(1.8 * LEFT + 1.1 * DOWN),
            lbl_fr_soult.animate.move_to(1.8 * LEFT + 1.1 * DOWN),
            co_left.animate.move_to(2.6 * LEFT + 1.9 * DOWN).scale(0.8),
            lbl_co_left.animate.move_to(2.6 * LEFT + 1.9 * DOWN).scale(0.8),
            FadeOut(arrow_sweep),
            run_time=2.0
        )
        
        # Breaking through ponds ice
        pond_break_text = Text("*pękanie lodu*", font_size=10, color=coalition_color, font="Georgia", slant=ITALIC).move_to(2.6*LEFT + 1.5*DOWN)
        self.play(Write(pond_break_text))
        
        # Fade out trapped allied unit
        self.play(
            co_left.animate.set_opacity(0),
            lbl_co_left.animate.set_opacity(0),
            FadeOut(pond_break_text),
            run_time=1.5
        )
        self.wait(1.0)
        
        # FINAL SUMMARY
        self.play(FadeOut(explanation_3))
        summary = Text(
            "Zwycięstwo pod Austerlitz przypieczętowało hegemonię Napoleona\ni doprowadziło do rozpadu III Koalicji Antyfrancuskiej.", 
            font_size=14, 
            color=french_color, 
            font="Georgia"
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(summary))
        self.wait(4.0)
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(map_rect),
            FadeOut(pratzen_bg),
            FadeOut(pratzen_label),
            FadeOut(goldbach_line),
            FadeOut(goldbach_label),
            FadeOut(pond1),
            FadeOut(pond2),
            FadeOut(ponds_label),
            FadeOut(french_units),
            FadeOut(co_bagration),
            FadeOut(lbl_co_bagration),
            FadeOut(co_center),
            FadeOut(lbl_co_center),
            FadeOut(summary)
        )
        self.wait(0.5)
