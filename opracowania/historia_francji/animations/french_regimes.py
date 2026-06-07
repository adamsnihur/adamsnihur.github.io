from manim import *

class FrenchRegimesScene(Scene):
    def construct(self):
        # Background
        self.camera.background_color = "#FAF9F6"
        
        # Title
        title = Text("Ewolucja Ustrojowa Francji (1789 - 2026)", font_size=28, color="#1F3A60", font="Georgia", weight=BOLD)
        title.to_edge(UP, buff=0.6)
        self.play(Write(title))
        self.wait(0.5)
        
        # Timeline line
        timeline_y = -1.5
        line = Line(start=5*LEFT + timeline_y*UP, end=5*RIGHT + timeline_y*UP, color="#475569", stroke_width=4)
        self.play(Create(line))
        
        # Start and end labels
        label_1789 = Text("1789", font_size=14, color="#475569", font="Georgia").next_to(line.get_left(), DOWN, buff=0.2)
        label_2026 = Text("2026", font_size=14, color="#475569", font="Georgia").next_to(line.get_right(), DOWN, buff=0.2)
        self.play(FadeIn(label_1789), FadeIn(label_2026))
        
        # Data for regimes
        regimes_data = [
            {"name": "Ancien Régime", "start": 1789, "end": 1792, "color": "#1F3A60", "desc": "Monarchia absolutna"},
            {"name": "I Republika", "start": 1792, "end": 1804, "color": "#A6242A", "desc": "Rewolucja i Konwent"},
            {"name": "I Cesarstwo", "start": 1804, "end": 1814, "color": "#D2A14E", "desc": "Napoleon I Bonaparte"},
            {"name": "Restauracja", "start": 1814, "end": 1830, "color": "#1F3A60", "desc": "Burbonowie (Ludwik XVIII, Karol X)"},
            {"name": "Monarchia Lipcowa", "start": 1830, "end": 1848, "color": "#2B4C7E", "desc": "Ludwik Filip I"},
            {"name": "II Republika", "start": 1848, "end": 1852, "color": "#A6242A", "desc": "Wiosna Ludów, Ludwik Napoleon"},
            {"name": "II Cesarstwo", "start": 1852, "end": 1870, "color": "#D2A14E", "desc": "Napoleon III"},
            {"name": "III Republika", "start": 1870, "end": 1940, "color": "#A6242A", "desc": "Czas rozkwitu i wojny światowej"},
            {"name": "Państwo Francuskie", "start": 1940, "end": 1944, "color": "#64748B", "desc": "Rząd Vichy, okupacja"},
            {"name": "IV Republika", "start": 1946, "end": 1958, "color": "#A6242A", "desc": "Odbudowa powojenna"},
            {"name": "V Republika", "start": 1958, "end": 2026, "color": "#A6242A", "desc": "De Gaulle i współczesność"}
        ]
        
        # Helper to convert year to x coordinate
        def year_to_x(year):
            return -5 + 10 * (year - 1789) / (2026 - 1789)
            
        # Draw colored blocks along the timeline
        blocks = VGroup()
        for r in regimes_data:
            x_start = year_to_x(r["start"])
            x_end = year_to_x(r["end"])
            width = x_end - x_start
            if width < 0.1:
                width = 0.1
                
            block = Rectangle(
                width=width, 
                height=0.4, 
                stroke_color=r["color"], 
                fill_color=r["color"], 
                fill_opacity=0.65
            )
            block.move_to((x_start + width/2) * RIGHT + timeline_y * UP)
            blocks.add(block)
            
        self.play(Create(blocks, run_time=3))
        self.wait(0.5)
        
        # Sweeper line (vertical red indicator)
        sweeper = Line(
            start=timeline_y * UP - 0.4 * UP - 5 * RIGHT, 
            end=timeline_y * UP + 0.4 * UP - 5 * RIGHT, 
            color="#A6242A", 
            stroke_width=5
        )
        self.play(Create(sweeper))
        
        # Details Card (Rectangle for info)
        card_box = RoundedRectangle(
            corner_radius=0.15,
            width=6.5, 
            height=2.2, 
            stroke_color="#1F3A60", 
            fill_color="#FFFFFF", 
            fill_opacity=0.95
        )
        card_box.move_to(0.8 * UP)
        self.play(FadeIn(card_box))
        
        # Dynamic Text elements
        regime_title = Text("", font_size=20, color="#1F3A60", font="Georgia", weight=BOLD).move_to(1.3 * UP)
        regime_years = Text("", font_size=15, color="#A6242A", font="Georgia").move_to(0.8 * UP)
        regime_desc = Text("", font_size=13, color="#475569", font="Georgia", slant=ITALIC).move_to(0.3 * UP)
        
        self.add(regime_title, regime_years, regime_desc)
        
        # Animate the sweeper moving across the timeline, updating the card info
        for idx, r in enumerate(regimes_data):
            x_start = year_to_x(r["start"])
            x_end = year_to_x(r["end"])
            x_middle = (x_start + x_end) / 2
            
            new_title = Text(r["name"], font_size=20, color="#1F3A60", font="Georgia", weight=BOLD).move_to(1.3 * UP)
            new_years = Text(f"{r['start']} - {r['end']}", font_size=15, color=r["color"], font="Georgia", weight=BOLD).move_to(0.8 * UP)
            new_desc = Text(r["desc"], font_size=13, color="#475569", font="Georgia", slant=ITALIC).move_to(0.3 * UP)
            
            active_block = blocks[idx]
            
            self.play(
                sweeper.animate.move_to(x_middle * RIGHT + timeline_y * UP),
                Transform(regime_title, new_title),
                Transform(regime_years, new_years),
                Transform(regime_desc, new_desc),
                active_block.animate.set_fill(opacity=1.0),
                run_time=0.8
            )
            self.wait(1.2)
            
            self.play(active_block.animate.set_fill(opacity=0.65), run_time=0.2)
            
        self.play(FadeOut(sweeper), FadeOut(card_box), FadeOut(regime_title), FadeOut(regime_years), FadeOut(regime_desc))
        self.wait(0.5)
        
        # Final summary text
        summary = Text(
            "Francja ukształtowała nowoczesną kulturę polityczną Europy\npoprzez ciągłe poszukiwanie syntezy wolności i stabilności.", 
            font_size=15, 
            color="#1F3A60", 
            font="Georgia"
        ).move_to(0.8 * UP)
        self.play(Write(summary))
        self.wait(3.5)
        self.play(FadeOut(summary), FadeOut(blocks), FadeOut(line), FadeOut(title), FadeOut(label_1789), FadeOut(label_2026))
        self.wait(0.5)
