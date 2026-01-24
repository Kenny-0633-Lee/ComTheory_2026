from manim import *

# --- 설정: Starlink 컬러 팔레트 ---
BG_COLOR = "#0B0E14"       # Deep Navy/Black
EARTH_COLOR = "#1C2541"    # Earth Surface
SAT_BODY = "#FFFFFF"       # Satellite Body
SAT_PANEL = "#2E4053"      # Solar Panel
CYAN_NEON = "#00F0FF"      # Laser / Gateway
GREEN_NEON = "#00FF9D"     # Direct to Cell
ORANGE_NEON = "#FF9E00"    # Ku-band Dish

config.background_color = BG_COLOR

class StarlinkNetwork(Scene):
    def construct(self):
        # 1. 지구 (Earth Horizon)
        # 화면 아래쪽에 거대한 원을 배치하여 둥근 지평선 표현
        earth = Circle(radius=12, color=EARTH_COLOR, fill_opacity=1)
        earth.shift(DOWN * 13)
        
        # 대기권 느낌의 은은한 테두리
        atmosphere = Circle(radius=12.1, color=BLUE_E, stroke_width=20, stroke_opacity=0.3)
        atmosphere.shift(DOWN * 13)
        
        earth_label = Text("EARTH SURFACE", font_size=24, color=GRAY)
        earth_label.move_to(DOWN * 3.5)

        self.add(earth, atmosphere, earth_label)

        # 2. 위성 생성 함수 (Satellites)
        def create_satellite(pos_x, pos_y):
            # 본체
            body = Rectangle(width=0.6, height=0.1, color=SAT_BODY, fill_opacity=1)
            # 태양광 패널 (위쪽으로 뻗은 형태)
            panel = Rectangle(width=0.2, height=0.8, color=SAT_PANEL, fill_opacity=0.8, stroke_color=WHITE, stroke_width=1)
            panel.next_to(body, UP, buff=0)
            
            sat_group = VGroup(panel, body).move_to([pos_x, pos_y, 0])
            label = Text("Starlink V2", font_size=16, color=WHITE).next_to(sat_group, UP * 0.5)
            return sat_group, label

        # 위성 배치
        sat1, label1 = create_satellite(-3.5, 2.5)
        sat2, label2 = create_satellite(3.5, 2.5)
        
        self.add(sat1, label1, sat2, label2)

        # 3. 지상 장비 생성 (Ground Hardware)
        
        # (A) 스마트폰 (Direct to Cell)
        phone = RoundedRectangle(corner_radius=0.05, width=0.3, height=0.6, color=WHITE, stroke_width=2)
        phone.move_to([-4.5, -2.5, 0])
        phone_label = Tex(r"\textbf{Smartphone}", font_size=24, color=WHITE).next_to(phone, DOWN)
        phone_sub = Text("(LTE Direct)", font_size=16, color=GRAY).next_to(phone_label, DOWN, buff=0.1)
        
        # (B) 사용자 단말 (Dishy)
        dish_base = Line([-0.2, 0, 0], [0.2, 0, 0], color=GRAY)
        dish_stand = Line([0, 0, 0], [0, 0.3, 0], color=GRAY)
        dish_plate = Arc(radius=0.4, angle=PI/2, color=WHITE).rotate(PI/4).move_to([0, 0.4, 0])
        dish_group = VGroup(dish_base, dish_stand, dish_plate).move_to([-0.5, -2.5, 0])
        dish_label = Tex(r"\textbf{User Dish}", font_size=24, color=WHITE).next_to(dish_group, DOWN)
        dish_sub = Text("(Ku-band)", font_size=16, color=GRAY).next_to(dish_label, DOWN, buff=0.1)

        # (C) 게이트웨이 (Tower)
        tower_base = Line([-0.3, 0, 0], [0.3, 0, 0], color=GRAY)
        tower_body = Polygon([-0.2, 0, 0], [0.2, 0, 0], [0.1, 0.8, 0], [-0.1, 0.8, 0], color=GRAY, stroke_width=2)
        tower_dome = Circle(radius=0.2, color=WHITE).move_to([0, 0.9, 0])
        gateway_group = VGroup(tower_base, tower_body, tower_dome).move_to([4.5, -2.5, 0])
        gw_label = Tex(r"\textbf{Gateway}", font_size=24, color=WHITE).next_to(gateway_group, DOWN)
        gw_sub = Text("(Ka/E-band)", font_size=16, color=GRAY).next_to(gw_label, DOWN, buff=0.1)

        self.add(phone, phone_label, phone_sub)
        self.add(dish_group, dish_label, dish_sub)
        self.add(gateway_group, gw_label, gw_sub)

        # 4. 통신 빔 효과 (Beams & Laser) - Manim의 강점!

        # (1) Laser Link (Glow Effect)
        laser_line = Line(sat1.get_center(), sat2.get_center(), color=CYAN_NEON)
        laser_glow = laser_line.copy().set_stroke(width=15, opacity=0.3) # 빛나는 효과
        laser_label = Text("Optical Laser Link", font_size=16, color=CYAN_NEON).next_to(laser_line, UP, buff=0.1)
        
        self.add(laser_glow, laser_line, laser_label)

        # 빔 생성 함수 (원뿔형 그라데이션)
        def create_beam(sat_mobject, target_mobject, color, label_text):
            start = sat_mobject.get_bottom()
            end = target_mobject.get_top()
            
            # 빔의 좌우 폭 설정
            beam_poly = Polygon(
                start + LEFT*0.05, start + RIGHT*0.05,  # 위성은 좁게
                end + RIGHT*0.5, end + LEFT*0.5,        # 지상은 넓게
                stroke_width=0,
                fill_color=color,
                fill_opacity=0.4
            )
            
            # 빔 라벨 (각도에 맞춰 회전)
            angle = np.arctan2(end[1] - start[1], end[0] - start[0])
            label = Text(label_text, font_size=18, color=color, weight=BOLD)
            label.move_to((start + end) / 2)
            # 텍스트 배경을 어둡게 해서 빔 위에서도 잘 보이게
            label.add_background_rectangle(color=BG_COLOR, opacity=0.7, buff=0.05)
            
            return VGroup(beam_poly, label)

        # (2) Smartphone Beam
        beam_phone = create_beam(sat1, phone, GREEN_NEON, "1.9 GHz")
        
        # (3) Dish Beam
        beam_dish = create_beam(sat1, dish_group, ORANGE_NEON, "Ku-band")
        
        # (4) Gateway Beam
        beam_gw = create_beam(sat2, gateway_group, CYAN_NEON, "Ka/E-band")

        self.add(beam_phone, beam_dish, beam_gw)