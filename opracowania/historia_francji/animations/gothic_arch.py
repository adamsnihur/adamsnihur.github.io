from manim import *

class GothicArchScene(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#FAF9F6"
        
        # Colors
        french_color = "#1F3A60"
        coalition_color = "#A6242A" # used for forces
        neutral_color = "#475569"   # structure
        gold_color = "#D2A14E"      # highlighting
        glass_color = "#22C55E"     # stained glass / windows
        
        # Title
        title = Text("Mechanika Sklepienia Gotyckiego", font_size=26, color=french_color, font="Georgia", weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)
        
        # Ground line
        ground = Line(start=5*LEFT + 2.5*DOWN, end=5*RIGHT + 2.5*DOWN, color=neutral_color, stroke_width=3)
        self.play(Create(ground))
        
        # PART 1: Romanesque Arch (Łuk Romański)
        rom_label = Text("1. ŁUK ROMAŃSKI (półkolisty)", font_size=16, color=french_color, font="Georgia", weight=BOLD).to_edge(LEFT, buff=0.8).shift(1.5*UP)
        self.play(Write(rom_label))
        
        # Vertical walls/columns
        col_l = Rectangle(width=0.4, height=3.0, fill_color=neutral_color, fill_opacity=0.5, stroke_color=neutral_color).move_to(1.5*LEFT + 1.0*DOWN)
        col_r = Rectangle(width=0.4, height=3.0, fill_color=neutral_color, fill_opacity=0.5, stroke_color=neutral_color).move_to(1.5*RIGHT + 1.0*DOWN)
        
        # Semi-circular arch (span 3.0, so radius is 1.5)
        rom_arch = Arc(radius=1.5, start_angle=0, angle=PI, arc_center=0.5*UP, color=neutral_color, stroke_width=6)
        
        # Weight on top
        weight = Rectangle(width=2.0, height=0.6, fill_color=neutral_color, fill_opacity=0.8, stroke_color=neutral_color).move_to(2.3*UP)
        weight_lbl = Text("Ciężar muru/dachu", font_size=10, color="#FFFFFF", font="Georgia").move_to(weight.get_center())
        weight_group = VGroup(weight, weight_lbl)
        
        self.play(
            FadeIn(col_l), FadeIn(col_r),
            Create(rom_arch),
            FadeIn(weight_group)
        )
        self.wait(0.5)
        
        # Romanesque forces (Lateral thrust - rozpychanie)
        # Weight pushes down, lateral forces push out
        arrow_down = Arrow(start=2.0*UP, end=0.8*UP, color=coalition_color, stroke_width=4)
        arrow_left_thrust = Arrow(start=1.3*LEFT + 0.5*UP, end=2.8*LEFT + 0.1*UP, color=coalition_color, stroke_width=5)
        arrow_right_thrust = Arrow(start=1.3*RIGHT + 0.5*UP, end=2.8*RIGHT + 0.1*UP, color=coalition_color, stroke_width=5)
        
        force_text = Text("Duża siła boczna (rozpychanie murów)", font_size=12, color=coalition_color, font="Georgia").to_edge(DOWN, buff=0.8)
        
        self.play(GrowArrow(arrow_down))
        self.play(GrowArrow(arrow_left_thrust), GrowArrow(arrow_right_thrust), Write(force_text))
        self.wait(1.5)
        
        # Simulate slight tilting of columns to show instability
        self.play(
            col_l.animate.rotate(0.04, about_point=1.5*LEFT + 2.5*DOWN),
            col_r.animate.rotate(-0.04, about_point=1.5*RIGHT + 2.5*DOWN),
            arrow_left_thrust.animate.shift(0.2*LEFT),
            arrow_right_thrust.animate.shift(0.2*RIGHT),
            run_time=1.0
        )
        self.wait(1.5)
        
        # Fade out Romanesque components to prepare for Gothic
        self.play(
            FadeOut(rom_label),
            FadeOut(rom_arch),
            FadeOut(weight_group),
            FadeOut(arrow_down),
            FadeOut(arrow_left_thrust),
            FadeOut(arrow_right_thrust),
            FadeOut(force_text),
            col_l.animate.set_angle(0), # reset columns
            col_r.animate.set_angle(0)
        )
        
        # PART 2: Gothic Arch (Łuk Gotycki)
        got_label = Text("2. ŁUK GOTYCKI (ostrołuk)", font_size=16, color=french_color, font="Georgia", weight=BOLD).to_edge(LEFT, buff=0.8).shift(1.5*UP)
        self.play(Write(got_label))
        
        # Pointed Arch curves:
        # Left half of pointed arch: centered at 1.5*RIGHT (radius=3.0), from angle PI to 2*PI/3 (120 deg)
        # Apex is at (0, 0.5 + 2.598) = (0, 3.098)
        # Let's adjust coordinates to sit on the columns (which end at y=0.5).
        # Columns top is at y=0.5. So arc_center is at y=0.5.
        got_arch_l = Arc(radius=3.0, start_angle=PI, angle=-PI/3, arc_center=1.5*RIGHT + 0.5*UP, color=neutral_color, stroke_width=6)
        got_arch_r = Arc(radius=3.0, start_angle=0, angle=PI/3, arc_center=1.5*LEFT + 0.5*UP, color=neutral_color, stroke_width=6)
        got_arch = VGroup(got_arch_l, got_arch_r)
        
        # New weight on top (higher because pointed arch is taller)
        weight_got = Rectangle(width=2.0, height=0.6, fill_color=neutral_color, fill_opacity=0.8, stroke_color=neutral_color).move_to(3.4*UP)
        weight_got_lbl = Text("Ciężar muru/dachu", font_size=10, color="#FFFFFF", font="Georgia").move_to(weight_got.get_center())
        weight_got_group = VGroup(weight_got, weight_got_lbl)
        
        self.play(
            Create(got_arch),
            FadeIn(weight_got_group)
        )
        self.wait(0.5)
        
        # Gothic forces (Directed down)
        arrow_down_got = Arrow(start=3.1*UP, end=2.0*UP, color=coalition_color, stroke_width=4)
        
        # Force vectors flow downwards through the arch
        arrow_flow_l = Arrow(start=0.5*LEFT + 2.5*UP, end=1.4*LEFT + 0.8*UP, color=coalition_color, stroke_width=5)
        arrow_flow_r = Arrow(start=0.5*RIGHT + 2.5*UP, end=1.4*RIGHT + 0.8*UP, color=coalition_color, stroke_width=5)
        
        force_text_got = Text("Siła skierowana bardziej pionowo w dół", font_size=12, color=coalition_color, font="Georgia").to_edge(DOWN, buff=0.8)
        
        self.play(GrowArrow(arrow_down_got))
        self.play(GrowArrow(arrow_flow_l), GrowArrow(arrow_flow_r), Write(force_text_got))
        self.wait(1.5)
        
        # PART 3: Buttress System (System Przyporowy)
        self.play(
            FadeOut(got_label),
            FadeOut(force_text_got)
        )
        
        system_label = Text("3. SYSTEM PRZYPOROWY (odciążenie)", font_size=16, color=french_color, font="Georgia", weight=BOLD).to_edge(LEFT, buff=0.8).shift(1.5*UP)
        self.play(Write(system_label))
        
        # Add Buttress Piers (Filary Przyporowe)
        pier_l = Rectangle(width=0.5, height=2.4, fill_color=neutral_color, fill_opacity=0.6, stroke_color=neutral_color).move_to(3.8*LEFT + 1.3*DOWN)
        pier_r = Rectangle(width=0.5, height=2.4, fill_color=neutral_color, fill_opacity=0.6, stroke_color=neutral_color).move_to(3.8*RIGHT + 1.3*DOWN)
        
        # Add Flying Buttresses (Łuki Przyporowe)
        # connecting columns (around y=1.2) to piers (around y=0.1)
        fly_butt_l = ArcBetweenPoints(start=1.6*LEFT + 1.5*UP, end=3.55*LEFT + 0.1*UP, angle=0.25, color=neutral_color, stroke_width=5)
        fly_butt_r = ArcBetweenPoints(start=1.6*RIGHT + 1.5*UP, end=3.55*RIGHT + 0.1*UP, angle=-0.25, color=neutral_color, stroke_width=5)
        
        self.play(
            FadeIn(pier_l, shift=UP), FadeIn(pier_r, shift=UP),
            Create(fly_butt_l), Create(fly_butt_r)
        )
        self.wait(0.5)
        
        # Show remaining lateral forces flowing down the flying buttress
        arrow_fly_l = Arrow(start=1.8*LEFT + 1.3*UP, end=3.4*LEFT + 0.3*UP, color=gold_color, stroke_width=4)
        arrow_fly_r = Arrow(start=1.8*RIGHT + 1.3*UP, end=3.4*RIGHT + 0.3*UP, color=gold_color, stroke_width=4)
        
        arrow_pier_l = Arrow(start=3.8*LEFT + 0.1*UP, end=3.8*LEFT + 1.8*DOWN, color=gold_color, stroke_width=4)
        arrow_pier_r = Arrow(start=3.8*RIGHT + 0.1*UP, end=3.8*RIGHT + 1.8*DOWN, color=gold_color, stroke_width=4)
        
        force_text_sys = Text("Łuki przyporowe odprowadzają siły na filary zewnętrzne", font_size=12, color=gold_color, font="Georgia").to_edge(DOWN, buff=0.8)
        
        self.play(
            GrowArrow(arrow_fly_l), GrowArrow(arrow_fly_r),
            GrowArrow(arrow_pier_l), GrowArrow(arrow_pier_r),
            Write(force_text_sys)
        )
        self.wait(1.5)
        
        # Windows can now open!
        # Draw a beautiful glass window outline inside the thin walls
        window_l = RoundedRectangle(corner_radius=0.1, width=0.6, height=1.6, color=glass_color, fill_color=glass_color, fill_opacity=0.3).move_to(1.5*LEFT + 0.5*DOWN)
        window_r = RoundedRectangle(corner_radius=0.1, width=0.6, height=1.6, color=glass_color, fill_color=glass_color, fill_opacity=0.3).move_to(1.5*RIGHT + 0.5*DOWN)
        window_lbl = Text("Mury mogą posiadać olbrzymie witraże", font_size=12, color=glass_color, font="Georgia", weight=BOLD).to_edge(DOWN, buff=0.8)
        
        self.play(
            FadeOut(force_text_sys),
            FadeOut(arrow_down_got), FadeOut(arrow_flow_l), FadeOut(arrow_flow_r),
            FadeOut(arrow_fly_l), FadeOut(arrow_fly_r),
            FadeOut(arrow_pier_l), FadeOut(arrow_pier_r),
            col_l.animate.set_opacity(0.15),
            col_r.animate.set_opacity(0.15)
        )
        self.play(
            FadeIn(window_l, scale=0.5), FadeIn(window_r, scale=0.5),
            Transform(system_label, window_lbl)
        )
        self.wait(2.5)
        
        # Final Summary
        self.play(FadeOut(system_label), FadeOut(window_lbl))
        summary = Text(
            "Gotycka inżynieria zintegrowała fizykę z estetyką,\npozwalając na wznoszenie strzelistych, pełnych światła świątyń.", 
            font_size=14, 
            color=french_color, 
            font="Georgia"
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(summary))
        self.wait(4.0)
        
        # Fade out everything
        self.play(
            FadeOut(title),
            FadeOut(ground),
            FadeOut(col_l),
            FadeOut(col_r),
            FadeOut(got_arch),
            FadeOut(weight_got_group),
            FadeOut(pier_l),
            FadeOut(pier_r),
            FadeOut(fly_butt_l),
            FadeOut(fly_butt_r),
            FadeOut(window_l),
            FadeOut(window_r),
            FadeOut(summary)
        )
        self.wait(0.5)
