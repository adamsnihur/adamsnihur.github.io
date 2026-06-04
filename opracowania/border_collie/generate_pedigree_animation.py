from manim import *

class PedigreeScene(Scene):
    def construct(self):
        # Background color
        self.camera.background_color = "#FAF9F6"
        
        # Title
        title = Text("Rodowód psa Old Hemp (1893)", font_size=32, color="#5B21B6", font="Georgia")
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)
        
        # Father Roy (Rectangle)
        roy_box = Rectangle(width=3.6, height=1.6, stroke_color="#475569", fill_color="#E2E8F0", fill_opacity=0.8)
        roy_title = Text("ROY (Ojciec)", font_size=18, color="#1E293B", weight=BOLD, font="Georgia")
        roy_desc1 = Text("Czarny-podpalany", font_size=14, color="#475569")
        roy_desc2 = Text("Praca głośna (szczekanie)", font_size=12, color="#475569")
        roy_desc3 = Text("Słaba kontrola wzrokiem", font_size=12, color="#475569")
        roy_text = VGroup(roy_title, roy_desc1, roy_desc2, roy_desc3).arrange(DOWN, buff=0.08)
        roy = VGroup(roy_box, roy_text)
        roy.move_to(2.0 * UP + 3.5 * LEFT)
        
        # Mother Meg (Rectangle)
        meg_box = Rectangle(width=3.6, height=1.6, stroke_color="#0D9488", fill_color="#CCFBF1", fill_opacity=0.8)
        meg_title = Text("MEG (Matka)", font_size=18, color="#1E293B", weight=BOLD, font="Georgia")
        meg_desc1 = Text("Czarna", font_size=14, color="#0D9488")
        meg_desc2 = Text("Praca cicha (brak głosu)", font_size=12, color="#0D9488")
        meg_desc3 = Text("Niezwykle silne \"oko\"", font_size=12, color="#0D9488")
        meg_text = VGroup(meg_title, meg_desc1, meg_desc2, meg_desc3).arrange(DOWN, buff=0.08)
        meg = VGroup(meg_box, meg_text)
        meg.move_to(2.0 * UP + 3.5 * RIGHT)
        
        self.play(FadeIn(roy, shift=RIGHT), FadeIn(meg, shift=LEFT))
        self.wait(1)
        
        # Connection lines
        dot_roy = Dot(roy.get_bottom(), color="#475569")
        dot_meg = Dot(meg.get_bottom(), color="#0D9488")
        
        target_center = 0.2 * UP
        line_roy = Line(roy.get_bottom(), target_center, color="#475569", stroke_width=2)
        line_meg = Line(meg.get_bottom(), target_center, color="#0D9488", stroke_width=2)
        
        self.play(Create(line_roy), Create(line_meg))
        self.wait(0.5)
        
        # Synthesis text
        synth_label = Text("Ideał pośredni (Telfer)", font_size=14, color="#1E293B", font="Georgia", weight=BOLD).move_to(target_center + 0.3 * UP)
        self.play(Write(synth_label))
        self.wait(0.5)
        
        # Arrow down from synthesis
        arrow_synth = Arrow(start=target_center, end=1.2 * DOWN, color="#5B21B6", stroke_width=3)
        self.play(GrowArrow(arrow_synth))
        
        # Old Hemp (Rectangle)
        hemp_box = Rectangle(width=5.0, height=2.2, stroke_color="#5B21B6", fill_color="#F3E8FF", fill_opacity=0.9)
        hemp_title = Text("OLD HEMP (ISDS 9)", font_size=20, color="#5B21B6", weight=BOLD, font="Georgia")
        hemp_desc1 = Text("Trójkolorowy (ur. 1893)", font_size=14, color="#1E293B")
        hemp_desc2 = Text("Praca w ciszy i pełnej płynności", font_size=12, color="#1E293B")
        hemp_desc3 = Text("Zbalansowane \"oko\", brak agresji", font_size=12, color="#1E293B")
        hemp_desc4 = Text("Protoplasta rasy Border Collie", font_size=12, color="#1E293B", weight=BOLD)
        hemp_text = VGroup(hemp_title, hemp_desc1, hemp_desc2, hemp_desc3, hemp_desc4).arrange(DOWN, buff=0.08)
        hemp = VGroup(hemp_box, hemp_text)
        hemp.move_to(2.3 * DOWN)
        
        self.play(FadeIn(hemp, shift=UP))
        self.wait(1.5)
        
        # Footnote text
        footnote = Text("Skojarzenie skrajności dało perfekcyjny wzorzec użytkowej pracy.", font_size=14, color="#475569", font="Georgia", slant=ITALIC)
        footnote.next_to(hemp, DOWN, buff=0.3)
        self.play(Write(footnote))
        self.wait(3.5)
        
        # Fade out everything nicely
        self.play(
            FadeOut(title),
            FadeOut(roy),
            FadeOut(meg),
            FadeOut(line_roy),
            FadeOut(line_meg),
            FadeOut(synth_label),
            FadeOut(arrow_synth),
            FadeOut(hemp),
            FadeOut(footnote)
        )
        self.wait(0.5)
