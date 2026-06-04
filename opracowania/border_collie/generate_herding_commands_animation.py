from manim import *

class HerdingCommandsScene(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#FAF9F6"
        
        # Title
        title = Text("Komendy kierunkowe w pracy pasterskiej", font_size=30, color="#5B21B6", font="Georgia")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)
        
        # Sheep flock (Center group of dots)
        sheep_group = VGroup()
        for pos in [ORIGIN, 0.3*UP+0.2*LEFT, 0.3*DOWN+0.2*RIGHT, 0.4*LEFT, 0.4*RIGHT, 0.2*UP+0.3*RIGHT, 0.2*DOWN+0.3*LEFT]:
            dot = Dot(pos, radius=0.15, color="#94A3B8")
            sheep_group.add(dot)
            
        sheep_label = Text("STADO OWIEC", font_size=14, color="#475569", font="Georgia", weight=BOLD).move_to(1.1 * UP)
        sheep = VGroup(sheep_group, sheep_label)
        self.play(Create(sheep_group), Write(sheep_label))
        
        # Handler (Bottom marker)
        handler_marker = Triangle(color="#1E293B", fill_color="#1E293B", fill_opacity=1.0).scale(0.2).move_to(3.0 * DOWN)
        handler_label = Text("PRZEWODNIK", font_size=12, color="#1E293B", font="Georgia", weight=BOLD).next_to(handler_marker, DOWN, buff=0.15)
        handler = VGroup(handler_marker, handler_label)
        self.play(Create(handler_marker), Write(handler_label))
        self.wait(1)
        
        # Flank radius
        flank_radius = 2.2
        
        # Come Bye (Clockwise)
        come_bye_arc = Arc(radius=flank_radius, start_angle=-90*DEGREES, angle=360*DEGREES, color="#0D9488", stroke_width=3)
        come_bye_arrow = Arrow(
            start=come_bye_arc.point_from_proportion(0.2),
            end=come_bye_arc.point_from_proportion(0.25),
            color="#0D9488",
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        come_bye_label = Text("COME BYE (zgodnie z ruchem wskazówek zegara)", font_size=16, color="#0D9488", font="Georgia", weight=BOLD).move_to(2.6 * UP)
        
        # Show Come Bye
        self.play(Write(come_bye_label))
        self.play(Create(come_bye_arc), run_time=2)
        self.play(GrowArrow(come_bye_arrow))
        
        # Dog marker running clockwise
        dog = Dot(color="#0D9488", radius=0.2).move_to(come_bye_arc.point_from_proportion(0.0))
        dog_label = Text("PIES", font_size=10, color="#0D9488", font="Georgia", weight=BOLD).next_to(dog, DOWN, buff=0.1)
        self.play(FadeIn(dog), FadeIn(dog_label))
        
        self.play(
            MoveAlongPath(dog, come_bye_arc),
            UpdateFromFunc(dog_label, lambda m: m.next_to(dog, UP if dog.get_y() < 0 else DOWN, buff=0.1)),
            run_time=3,
            rate_func=linear
        )
        self.wait(1.5)
        
        # Clean Come Bye assets
        self.play(
            FadeOut(come_bye_arc),
            FadeOut(come_bye_arrow),
            FadeOut(come_bye_label),
            FadeOut(dog),
            FadeOut(dog_label)
        )
        
        # Away to Me (Counter-Clockwise)
        away_me_arc = Arc(radius=flank_radius, start_angle=-90*DEGREES, angle=-360*DEGREES, color="#7C3AED", stroke_width=3)
        away_me_arrow = Arrow(
            start=away_me_arc.point_from_proportion(0.2),
            end=away_me_arc.point_from_proportion(0.25),
            color="#7C3AED",
            stroke_width=3,
            max_tip_length_to_length_ratio=0.3
        )
        away_me_label = Text("AWAY TO ME (przeciwnie do wskazówek zegara)", font_size=16, color="#7C3AED", font="Georgia", weight=BOLD).move_to(2.6 * UP)
        
        # Show Away to Me
        self.play(Write(away_me_label))
        self.play(Create(away_me_arc), run_time=2)
        self.play(GrowArrow(away_me_arrow))
        
        # Dog marker running counter-clockwise
        dog2 = Dot(color="#7C3AED", radius=0.2).move_to(away_me_arc.point_from_proportion(0.0))
        dog_label2 = Text("PIES", font_size=10, color="#7C3AED", font="Georgia", weight=BOLD).next_to(dog2, DOWN, buff=0.1)
        self.play(FadeIn(dog2), FadeIn(dog_label2))
        
        self.play(
            MoveAlongPath(dog2, away_me_arc),
            UpdateFromFunc(dog_label2, lambda m: m.next_to(dog2, UP if dog2.get_y() < 0 else DOWN, buff=0.1)),
            run_time=3,
            rate_func=linear
        )
        self.wait(1.5)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)
