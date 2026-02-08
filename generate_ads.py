# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

ADS_DIR = os.path.join(os.path.dirname(__file__), 'ads')
os.makedirs(ADS_DIR, exist_ok=True)

SIZE = 1080

COLORS = {
    'primary': (86, 228, 253),
    'primary_dark': (5, 93, 254),
    'bg_dark': (10, 10, 10),
    'white': (255, 255, 255),
    'danger': (255, 107, 107),
    'success': (34, 197, 94),
    'warning': (255, 217, 61),
    'text_secondary': (160, 160, 160),
    'orange': (255, 150, 50),
}

def get_font(size, bold=False):
    paths = [
        "C:/Windows/Fonts/malgunbd.ttf" if bold else "C:/Windows/Fonts/malgun.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

def gradient(size, c1, c2):
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)
    for i in range(size):
        r = int(c1[0] + (c2[0] - c1[0]) * i / size)
        g = int(c1[1] + (c2[1] - c1[1]) * i / size)
        b = int(c1[2] + (c2[2] - c1[2]) * i / size)
        draw.line([(0, i), (size, i)], fill=(r, g, b))
    return img

def center_text(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    x = (SIZE - (bbox[2] - bbox[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)

def rounded_rect(draw, coords, r, fill):
    x1, y1, x2, y2 = coords
    draw.rectangle([x1+r, y1, x2-r, y2], fill=fill)
    draw.rectangle([x1, y1+r, x2, y2-r], fill=fill)
    draw.ellipse([x1, y1, x1+r*2, y1+r*2], fill=fill)
    draw.ellipse([x2-r*2, y1, x2, y1+r*2], fill=fill)
    draw.ellipse([x1, y2-r*2, x1+r*2, y2], fill=fill)
    draw.ellipse([x2-r*2, y2-r*2, x2, y2], fill=fill)

def cta_btn(draw, text, y, w=500, h=90):
    x = (SIZE - w) // 2
    rounded_rect(draw, [x, y, x+w, y+h], 45, COLORS['primary'])
    font = get_font(34, True)
    bbox = draw.textbbox((0, 0), text, font=font)
    tx = x + (w - (bbox[2] - bbox[0])) // 2
    ty = y + (h - (bbox[3] - bbox[1])) // 2 - 5
    draw.text((tx, ty), text, font=font, fill=COLORS['bg_dark'])

def logo(draw):
    font = get_font(32, True)
    draw.text((SIZE - 200, SIZE - 55), "DevAuto", font=font, fill=COLORS['primary'])

# Ad 01: Pain Point - Excel Hell
def ad01():
    img = gradient(SIZE, (30, 15, 40), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    center_text(draw, "Excel", 200, get_font(120, True), COLORS['danger'])
    center_text(draw, "지옥에서", 350, get_font(80, True), COLORS['white'])
    center_text(draw, "탈출하세요", 450, get_font(80, True), COLORS['primary'])
    center_text(draw, "매일 반복되는 수작업, 이제 그만", 580, get_font(36), COLORS['text_secondary'])
    cta_btn(draw, "무료 자동화 진단받기", 720)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '01_pain.png'), quality=95)

# Ad 02: ROI Stats
def ad02():
    img = gradient(SIZE, (20, 35, 60), (10, 10, 15))
    draw = ImageDraw.Draw(img)
    center_text(draw, "업무시간", 150, get_font(48, True), COLORS['white'])
    center_text(draw, "70%", 250, get_font(200, True), COLORS['primary'])
    center_text(draw, "절감", 480, get_font(72, True), COLORS['white'])
    rounded_rect(draw, [200, 580, 880, 680], 20, (30, 40, 50))
    center_text(draw, "150+ 기업이 검증한 효과", 610, get_font(36, True), COLORS['success'])
    cta_btn(draw, "절감 효과 계산하기", 750)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '02_roi.png'), quality=95)

# Ad 03: Before/After
def ad03():
    img = Image.new('RGB', (SIZE, SIZE), COLORS['bg_dark'])
    draw = ImageDraw.Draw(img)
    # Left side - Before
    draw.rectangle([0, 0, SIZE//2-10, 700], fill=(50, 20, 20))
    draw.text((SIZE//4-80, 100), "BEFORE", font=get_font(40, True), fill=COLORS['danger'])
    draw.text((SIZE//4-70, 200), "4시간", font=get_font(100, True), fill=COLORS['danger'])
    draw.text((SIZE//4-60, 350), "야근 필수", font=get_font(36), fill=COLORS['text_secondary'])
    draw.text((SIZE//4-60, 410), "실수 발생", font=get_font(36), fill=COLORS['text_secondary'])
    draw.text((SIZE//4-60, 470), "스트레스", font=get_font(36), fill=COLORS['text_secondary'])
    # Right side - After
    draw.rectangle([SIZE//2+10, 0, SIZE, 700], fill=(20, 50, 35))
    draw.text((SIZE*3//4-60, 100), "AFTER", font=get_font(40, True), fill=COLORS['success'])
    draw.text((SIZE*3//4-60, 200), "3분", font=get_font(100, True), fill=COLORS['success'])
    draw.text((SIZE*3//4-60, 350), "자동 완료", font=get_font(36), fill=COLORS['white'])
    draw.text((SIZE*3//4-60, 410), "오류 제로", font=get_font(36), fill=COLORS['white'])
    draw.text((SIZE*3//4-60, 470), "퇴근 보장", font=get_font(36), fill=COLORS['white'])
    # Bottom CTA
    draw.rectangle([0, 720, SIZE, SIZE], fill=COLORS['bg_dark'])
    cta_btn(draw, "우리 회사도 가능할까?", 800, 550)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '03_before_after.png'), quality=95)

# Ad 04: FOMO/Urgency
def ad04():
    img = gradient(SIZE, (60, 15, 15), (15, 10, 10))
    draw = ImageDraw.Draw(img)
    draw.rectangle([15, 15, SIZE-15, SIZE-15], outline=COLORS['danger'], width=8)
    rounded_rect(draw, [280, 100, 800, 170], 35, COLORS['danger'])
    center_text(draw, "이번 달 마감 임박", 115, get_font(40, True), COLORS['white'])
    center_text(draw, "무료 진단", 250, get_font(80, True), COLORS['white'])
    center_text(draw, "3자리", 360, get_font(100, True), COLORS['primary'])
    center_text(draw, "남음", 490, get_font(60, True), COLORS['white'])
    center_text(draw, "놓치면 다음 달까지 대기", 600, get_font(32), COLORS['warning'])
    cta_btn(draw, "지금 바로 신청하기", 720, 480)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '04_fomo.png'), quality=95)

# Ad 05: Question Hook
def ad05():
    img = gradient(SIZE, COLORS['primary_dark'], (15, 15, 40))
    draw = ImageDraw.Draw(img)
    center_text(draw, "혹시 지금도", 180, get_font(56, True), COLORS['white'])
    center_text(draw, "Excel 복붙", 280, get_font(72, True), COLORS['warning'])
    center_text(draw, "하고 계신가요?", 380, get_font(56, True), COLORS['white'])
    rounded_rect(draw, [180, 500, 900, 620], 20, (30, 30, 50))
    center_text(draw, "하루 3시간 = 연간 1,560만원 낭비", 540, get_font(36, True), COLORS['danger'])
    cta_btn(draw, "낭비 비용 계산해보기", 720)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '05_question.png'), quality=95)

# Ad 06: Social Proof
def ad06():
    img = gradient(SIZE, (15, 25, 20), (10, 10, 15))
    draw = ImageDraw.Draw(img)
    center_text(draw, "150+ 기업이 선택한", 120, get_font(40, True), COLORS['text_secondary'])
    center_text(draw, "업무 자동화", 190, get_font(60, True), COLORS['white'])
    # Stats boxes
    stats = [('150+', '도입 기업'), ('98%', '재계약률'), ('4.9', '만족도')]
    bw, gap = 280, 40
    sx = (SIZE - (bw*3 + gap*2)) // 2
    for i, (n, l) in enumerate(stats):
        x = sx + i*(bw+gap)
        rounded_rect(draw, [x, 300, x+bw, 500], 20, (25, 40, 35))
        f1, f2 = get_font(80, True), get_font(32)
        b1 = draw.textbbox((0,0), n, font=f1)
        draw.text((x+(bw-(b1[2]-b1[0]))//2, 330), n, font=f1, fill=COLORS['primary'])
        b2 = draw.textbbox((0,0), l, font=f2)
        draw.text((x+(bw-(b2[2]-b2[0]))//2, 440), l, font=f2, fill=COLORS['white'])
    center_text(draw, "검증된 파트너와 함께하세요", 560, get_font(36, True), COLORS['text_secondary'])
    cta_btn(draw, "성공 사례 보기", 720, 400)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '06_social_proof.png'), quality=95)

# Ad 07: Cost Comparison
def ad07():
    img = Image.new('RGB', (SIZE, SIZE), COLORS['bg_dark'])
    draw = ImageDraw.Draw(img)
    center_text(draw, "직원 vs 자동화", 70, get_font(52, True), COLORS['white'])
    center_text(draw, "어떤 선택이 현명할까요?", 140, get_font(36), COLORS['text_secondary'])
    # Header
    hy = 220
    draw.rectangle([100, hy, 540, hy+70], fill=(50, 30, 30))
    draw.rectangle([560, hy, 980, hy+70], fill=(30, 50, 35))
    f = get_font(32, True)
    draw.text((250, hy+18), "직원 채용", font=f, fill=COLORS['danger'])
    draw.text((700, hy+18), "자동화", font=f, fill=COLORS['success'])
    # Comparison rows
    items = [
        ('월 비용', '350만원+', '50만원~'),
        ('실수율', '있음', '0%'),
        ('퇴사 위험', '높음', '없음'),
        ('24시간 가동', 'X', 'O'),
    ]
    fi, fv = get_font(28), get_font(30, True)
    for i, (lb, bad, good) in enumerate(items):
        y = 310 + i*85
        draw.rectangle([100, y, 980, y+75], fill=(22,22,28) if i%2==0 else (28,28,34))
        draw.text((120, y+22), lb, font=fi, fill=COLORS['text_secondary'])
        draw.text((320, y+22), bad, font=fv, fill=COLORS['danger'])
        draw.text((720, y+22), good, font=fv, fill=COLORS['success'])
    cta_btn(draw, "비용 비교 상담받기", 720, 480)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '07_comparison.png'), quality=95)

# Ad 08: Testimonial
def ad08():
    img = gradient(SIZE, (25, 25, 45), (10, 10, 15))
    draw = ImageDraw.Draw(img)
    # Quote mark
    draw.text((80, 60), '"', font=get_font(200, True), fill=(50, 50, 80))
    f1, f2 = get_font(44, True), get_font(56, True)
    draw.text((120, 220), "자동화 도입 후", font=f1, fill=COLORS['white'])
    draw.text((120, 290), "연 4,000만원", font=f2, fill=COLORS['primary'])
    draw.text((120, 380), "절감했습니다", font=f1, fill=COLORS['white'])
    # ROI badge
    rounded_rect(draw, [120, 480, 400, 560], 15, (35, 55, 45))
    draw.text((150, 502), "ROI 800%", font=get_font(40, True), fill=COLORS['success'])
    # Author
    draw.text((120, 620), "박지현 이사", font=get_font(32, True), fill=COLORS['white'])
    draw.text((120, 670), "물류회사 A사 | 직원 120명", font=get_font(26), fill=COLORS['text_secondary'])
    cta_btn(draw, "우리 회사 ROI 계산하기", 800, 500)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '08_testimonial.png'), quality=95)

# Ad 09: Loss Aversion
def ad09():
    img = gradient(SIZE, (60, 20, 20), (15, 10, 10))
    draw = ImageDraw.Draw(img)
    center_text(draw, "지금 이 순간에도", 150, get_font(48, True), COLORS['white'])
    center_text(draw, "1,200만원", 280, get_font(120, True), COLORS['danger'])
    center_text(draw, "이 낭비되고 있습니다", 440, get_font(48, True), COLORS['white'])
    rounded_rect(draw, [180, 530, 900, 620], 15, (50, 30, 30))
    center_text(draw, "직원 1명 x 하루 3시간 x 1년 기준", 560, get_font(30), COLORS['text_secondary'])
    cta_btn(draw, "우리 회사 낭비 비용 확인", 720, 520)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '09_problem.png'), quality=95)

# Ad 10: Solution Benefits
def ad10():
    img = gradient(SIZE, (15, 35, 30), (10, 15, 20))
    draw = ImageDraw.Draw(img)
    center_text(draw, "맞춤형 자동화로", 130, get_font(52, True), COLORS['white'])
    center_text(draw, "업무 혁신", 210, get_font(72, True), COLORS['primary'])
    benefits = [
        '데이터 자동 수집',
        '보고서 자동 생성',
        '알림 자동 발송',
        '100% 맞춤 개발',
        '1개월 무료 지원',
    ]
    f = get_font(34)
    y = 340
    for b in benefits:
        center_text(draw, '+ ' + b, y, f, COLORS['success'])
        y += 60
    cta_btn(draw, "무료 분석 신청하기", 750, 450)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '10_solution.png'), quality=95)

# Ad 11: Urgency Warning
def ad11():
    img = Image.new('RGB', (SIZE, SIZE), COLORS['bg_dark'])
    draw = ImageDraw.Draw(img)
    draw.rectangle([12, 12, SIZE-12, SIZE-12], outline=COLORS['warning'], width=8)
    rounded_rect(draw, [280, 100, 800, 170], 35, COLORS['warning'])
    center_text(draw, "지금 확인하세요", 118, get_font(38, True), COLORS['bg_dark'])
    center_text(draw, "반복 업무로 낭비되는", 240, get_font(44, True), COLORS['white'])
    center_text(draw, "인건비", 310, get_font(44, True), COLORS['white'])
    center_text(draw, "1,200만원", 420, get_font(110, True), COLORS['danger'])
    center_text(draw, "/년 (직원 1명, 하루 3시간 기준)", 560, get_font(28), COLORS['text_secondary'])
    cta_btn(draw, "우리 회사 계산해보기", 720, 480)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '11_loss.png'), quality=95)

# Ad 12: Simple Process
def ad12():
    img = gradient(SIZE, (15, 25, 45), (10, 10, 15))
    draw = ImageDraw.Draw(img)
    center_text(draw, "간단한 4단계", 100, get_font(56, True), COLORS['white'])
    center_text(draw, "프로세스", 180, get_font(56, True), COLORS['primary'])
    steps = [('1', '무료 진단'), ('2', '솔루션 제안'), ('3', '맞춤 개발'), ('4', '도입 완료')]
    cs, gap = 110, 140
    sx = (SIZE - (cs*4 + gap*3)) // 2 + 20
    y = 340
    fn, fs = get_font(52, True), get_font(28, True)
    for i, (n, nm) in enumerate(steps):
        x = sx + i*(cs+gap)
        draw.ellipse([x, y, x+cs, y+cs], fill=COLORS['primary'])
        b = draw.textbbox((0,0), n, font=fn)
        draw.text((x+(cs-(b[2]-b[0]))//2, y+(cs-(b[3]-b[1]))//2-5), n, font=fn, fill=COLORS['bg_dark'])
        b2 = draw.textbbox((0,0), nm, font=fs)
        draw.text((x+(cs-(b2[2]-b2[0]))//2, y+130), nm, font=fs, fill=COLORS['white'])
        if i < 3:
            draw.text((x+cs+40, y+30), '>', font=get_font(48, True), fill=COLORS['text_secondary'])
    cta_btn(draw, "지금 시작하기", 700, 400)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '12_process.png'), quality=95)

# Ad 13: Free Offer
def ad13():
    img = gradient(SIZE, COLORS['primary_dark'], COLORS['primary'])
    draw = ImageDraw.Draw(img)
    center_text(draw, "자동화", 150, get_font(60, True), COLORS['white'])
    center_text(draw, "무료 진단", 230, get_font(60, True), COLORS['white'])
    rounded_rect(draw, [250, 340, 830, 480], 70, COLORS['white'])
    center_text(draw, "100% 무료", 375, get_font(90, True), COLORS['primary_dark'])
    center_text(draw, "30분이면 절감 효과를 알 수 있습니다", 540, get_font(32), COLORS['white'])
    rounded_rect(draw, [280, 680, 800, 770], 45, COLORS['white'])
    center_text(draw, "무료로 시작하기", 705, get_font(36, True), COLORS['primary_dark'])
    center_text(draw, "부담 없이 상담받으세요", 840, get_font(28), COLORS['white'])
    logo(draw)
    img.save(os.path.join(ADS_DIR, '13_free.png'), quality=95)

# Ad 14: Competition Fear
def ad14():
    img = gradient(SIZE, (35, 25, 15), (10, 10, 15))
    draw = ImageDraw.Draw(img)
    center_text(draw, "경쟁사는 이미", 130, get_font(52, True), COLORS['white'])
    center_text(draw, "6시 퇴근", 220, get_font(72, True), COLORS['success'])
    # Two boxes
    bw = 380
    x1, x2 = 80, SIZE-80-bw
    # Left - Automated
    rounded_rect(draw, [x1, 350, x1+bw, 600], 20, (30, 50, 40))
    draw.rectangle([x1, 350, x1+bw, 420], fill=COLORS['success'])
    center_text(draw, "자동화 도입", 368, get_font(30, True), COLORS['white'])
    draw.text((x1+150, 470), ":)", font=get_font(100), fill=COLORS['white'])
    # Right - Manual
    rounded_rect(draw, [x2, 350, x2+bw, 600], 20, (50, 35, 35))
    draw.rectangle([x2, 350, x2+bw, 420], fill=COLORS['danger'])
    center_text(draw, "수작업", 368, get_font(30, True), COLORS['white'])
    draw.text((x2+150, 470), ":(", font=get_font(100), fill=COLORS['white'])
    center_text(draw, "VS", 460, get_font(52, True), COLORS['primary'])
    center_text(draw, "당신의 회사는?", 660, get_font(44, True), COLORS['white'])
    cta_btn(draw, "지금 바꾸기", 770, 400)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '14_competition.png'), quality=95)

# Ad 15: Guarantee
def ad15():
    img = gradient(SIZE, (15, 30, 25), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    # Shield icon simulation
    center_text(draw, "[GUARANTEE]", 100, get_font(48, True), COLORS['primary'])
    center_text(draw, "효과 없으면", 220, get_font(56, True), COLORS['white'])
    center_text(draw, "100% 환불", 310, get_font(80, True), COLORS['primary'])
    rounded_rect(draw, [180, 450, 900, 600], 20, (30, 50, 40))
    draw.rectangle([180, 450, 900, 510], fill=COLORS['success'])
    center_text(draw, "계약서 명시 | 리스크 제로", 465, get_font(32, True), COLORS['white'])
    center_text(draw, "결과가 나오지 않으면 전액 환불해드립니다", 540, get_font(28), COLORS['white'])
    cta_btn(draw, "부담 없이 상담받기", 720, 450)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '15_guarantee.png'), quality=95)

# Ad 16: Time Savings
def ad16():
    img = gradient(SIZE, (30, 20, 50), (15, 15, 35))
    draw = ImageDraw.Draw(img)
    center_text(draw, "[TIME]", 120, get_font(60, True), COLORS['primary'])
    center_text(draw, "매달", 230, get_font(56, True), COLORS['white'])
    center_text(draw, "80시간", 330, get_font(100, True), COLORS['primary'])
    center_text(draw, "되찾으세요", 470, get_font(56, True), COLORS['white'])
    rounded_rect(draw, [280, 560, 800, 650], 20, (40, 35, 60))
    center_text(draw, "= 근무일 10일분", 590, get_font(40, True), COLORS['warning'])
    cta_btn(draw, "시간 되찾기", 750, 400)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '16_time_save.png'), quality=95)

# Ad 17: CEO Target
def ad17():
    img = gradient(SIZE, (15, 15, 35), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    rounded_rect(draw, [280, 100, 800, 170], 35, (40, 50, 70))
    draw.rectangle([280, 100, 800, 140], fill=COLORS['primary'])
    center_text(draw, "중소기업 대표님께", 108, get_font(30, True), COLORS['bg_dark'])
    center_text(draw, "직원에게 반복 업무", 230, get_font(48, True), COLORS['white'])
    center_text(draw, "시키고 계신가요?", 300, get_font(48, True), COLORS['danger'])
    rounded_rect(draw, [120, 420, 960, 540], 15, (30, 30, 45))
    center_text(draw, "직원 월급 350만원 = 자동화 7개 도입", 465, get_font(32, True), COLORS['primary'])
    center_text(draw, "같은 비용으로 7배 더 많은 일을", 600, get_font(32), COLORS['text_secondary'])
    cta_btn(draw, "비용 비교해보기", 730, 420)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '17_ceo_target.png'), quality=95)

# Ad 18: Story/Testimonial Long
def ad18():
    img = gradient(SIZE, (20, 20, 30), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    f = get_font(40, True)
    lines = [
        ('"처음엔 반신반의했어요"', COLORS['text_secondary']),
        ('', None),
        ('근데 도입 첫 주부터', COLORS['white']),
        ('야근이 사라졌습니다.', COLORS['primary']),
        ('', None),
        ('월 80시간을', COLORS['white']),
        ('되찾았어요.', COLORS['primary']),
    ]
    y = 140
    for t, c in lines:
        if t:
            draw.text((100, y), t, font=f, fill=c)
        y += 60
    rounded_rect(draw, [100, 640, 550, 740], 15, (35, 35, 50))
    draw.text((120, 660), "김대표 | 마켓플러스", font=get_font(28, True), fill=COLORS['white'])
    draw.text((120, 700), "유통업 | 직원 45명", font=get_font(24), fill=COLORS['text_secondary'])
    cta_btn(draw, "더 많은 후기 보기", 820, 420)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '18_storytelling.png'), quality=95)

# Ad 19: Countdown Urgency
def ad19():
    img = gradient(SIZE, (60, 15, 15), (15, 10, 10))
    draw = ImageDraw.Draw(img)
    draw.rectangle([12, 12, SIZE-12, SIZE-12], outline=COLORS['danger'], width=8)
    center_text(draw, "무료 진단 마감까지", 130, get_font(48, True), COLORS['white'])
    # Countdown boxes
    boxes = [('0', '일'), ('23', '시간'), ('59', '분')]
    bw, gap = 200, 50
    sx = (SIZE - (bw*3 + gap*2)) // 2
    fn, fl = get_font(80, True), get_font(28)
    for i, (n, l) in enumerate(boxes):
        x = sx + i*(bw+gap)
        rounded_rect(draw, [x, 260, x+bw, 430], 20, (70, 30, 30))
        b = draw.textbbox((0,0), n, font=fn)
        draw.text((x+(bw-(b[2]-b[0]))//2, 285), n, font=fn, fill=COLORS['danger'])
        b2 = draw.textbbox((0,0), l, font=fl)
        draw.text((x+(bw-(b2[2]-b2[0]))//2, 385), l, font=fl, fill=COLORS['white'])
    center_text(draw, "이번 달 3자리만 가능", 500, get_font(36, True), COLORS['danger'])
    rounded_rect(draw, [220, 580, 860, 670], 15, (60, 35, 35))
    center_text(draw, "놓치면 다음 달까지 대기!", 608, get_font(34, True), COLORS['warning'])
    cta_btn(draw, "지금 바로 신청", 730, 450)
    logo(draw)
    img.save(os.path.join(ADS_DIR, '19_countdown.png'), quality=95)

# Ad 20: Final CTA
def ad20():
    img = gradient(SIZE, COLORS['primary_dark'], (15, 40, 80))
    draw = ImageDraw.Draw(img)
    center_text(draw, "오늘 바로", 150, get_font(64, True), COLORS['white'])
    center_text(draw, "자동화 시작하세요", 240, get_font(64, True), COLORS['white'])
    benefits = ['무료 진단', '맞춤 개발', '100% 환불 보장', '1개월 무료 지원']
    f = get_font(30, True)
    positions = [(160, 380), (560, 380), (160, 460), (560, 460)]
    for (x, y), t in zip(positions, benefits):
        rounded_rect(draw, [x, y, x+360, y+60], 30, (60, 80, 120))
        draw.text((x+25, y+14), '+ '+t, font=f, fill=COLORS['white'])
    center_text(draw, "150+ 기업 | 98% 재계약", 580, get_font(36, True), COLORS['warning'])
    rounded_rect(draw, [220, 680, 860, 780], 50, COLORS['white'])
    center_text(draw, "30초 만에 신청하기", 710, get_font(40, True), COLORS['primary_dark'])
    center_text(draw, "부담 없이 | 24시간 내 답변 | 100% 무료", 850, get_font(26), COLORS['white'])
    logo(draw)
    img.save(os.path.join(ADS_DIR, '20_final_cta.png'), quality=95)

if __name__ == '__main__':
    print("="*50)
    print("Generating 20 Meta Ad Images (Korean)...")
    print("="*50)

    funcs = [ad01, ad02, ad03, ad04, ad05, ad06, ad07, ad08, ad09, ad10,
             ad11, ad12, ad13, ad14, ad15, ad16, ad17, ad18, ad19, ad20]

    for i, fn in enumerate(funcs, 1):
        fn()
        print(f"[OK] Ad {i:02d} created")

    print("="*50)
    print(f"DONE! 20 images saved to: {ADS_DIR}")
    print("="*50)
