from PIL import Image, ImageDraw
import os

# 确保目录存在
os.makedirs('assets/images', exist_ok=True)

# 创建所有图片
images = [
    # Logo
    {
        'name': 'logo.png',
        'size': (32, 32),
        'bgcolor': (255, 255, 255, 0),
        'draw': lambda draw: [
            draw.ellipse((4, 4, 28, 28), fill=(59, 130, 246)),
            draw.rectangle((12, 10, 20, 22), fill=(255, 255, 255)),
            draw.line((12, 16, 20, 16), fill=(255, 255, 255), width=2)
        ]
    },
    # Video doctor
    {
        'name': 'video-doctor.png',
        'size': (80, 80),
        'bgcolor': (219, 234, 254),
        'draw': lambda draw: [
            draw.rectangle((20, 30, 60, 50), outline=(59, 130, 246), width=2),
            draw.polygon([(60, 40), (70, 35), (70, 45)], fill=(59, 130, 246))
        ]
    },
    # Patient info
    {
        'name': 'patient-info.png',
        'size': (24, 24),
        'bgcolor': (255, 255, 255, 0),
        'draw': lambda draw: [
            draw.rectangle((5, 4, 19, 20), outline=(255, 255, 255), width=2),
            draw.line((8, 8, 16, 8), fill=(255, 255, 255), width=1),
            draw.line((8, 12, 16, 12), fill=(255, 255, 255), width=1),
            draw.line((8, 16, 16, 16), fill=(255, 255, 255), width=1)
        ]
    },
    # Choose doctor
    {
        'name': 'choose-doctor.png',
        'size': (24, 24),
        'bgcolor': (255, 255, 255, 0),
        'draw': lambda draw: [
            draw.ellipse((8, 3, 16, 11), outline=(255, 255, 255), width=2),
            draw.polygon([(12, 11), (7, 21), (17, 21)], outline=(255, 255, 255), width=2)
        ]
    },
    # Video call
    {
        'name': 'video-call.png',
        'size': (24, 24),
        'bgcolor': (255, 255, 255, 0),
        'draw': lambda draw: [
            draw.rectangle((3, 8, 15, 16), outline=(255, 255, 255), width=2),
            draw.polygon([(15, 12), (21, 9), (21, 15)], outline=(255, 255, 255), width=2)
        ]
    },
    # Patient avatar 1
    {
        'name': 'patient1.jpg',
        'size': (100, 100),
        'bgcolor': (237, 100, 166),
        'draw': lambda draw: [
            draw.text((45, 45), "1", fill=(255, 255, 255)),
            draw.rectangle((30, 30, 70, 70), outline=(255, 255, 255), width=1)
        ]
    },
    # Patient avatar 2
    {
        'name': 'patient2.jpg',
        'size': (100, 100),
        'bgcolor': (59, 130, 246),
        'draw': lambda draw: [
            draw.text((45, 45), "2", fill=(255, 255, 255)),
            draw.rectangle((30, 30, 70, 70), outline=(255, 255, 255), width=1)
        ]
    },
    # Patient avatar 3
    {
        'name': 'patient3.jpg',
        'size': (100, 100),
        'bgcolor': (16, 185, 129),
        'draw': lambda draw: [
            draw.text((45, 45), "3", fill=(255, 255, 255)),
            draw.rectangle((30, 30, 70, 70), outline=(255, 255, 255), width=1)
        ]
    },
    # Doctor video
    {
        'name': 'doctor-video.jpg',
        'size': (400, 300),
        'bgcolor': (42, 75, 141),
        'draw': lambda draw: [
            draw.text((180, 140), "医生视频", fill=(255, 255, 255)),
            draw.rectangle((50, 50, 350, 250), outline=(255, 255, 255), width=2)
        ]
    },
    # Self video
    {
        'name': 'self-video.jpg',
        'size': (120, 90),
        'bgcolor': (68, 68, 68),
        'draw': lambda draw: [
            draw.text((45, 40), "我", fill=(255, 255, 255)),
            draw.rectangle((10, 10, 110, 80), outline=(255, 255, 255), width=1)
        ]
    }
]

# 生成所有图片
for img_data in images:
    if img_data['name'].endswith('.png'):
        img = Image.new('RGBA', img_data['size'], img_data['bgcolor'])
    else:
        img = Image.new('RGB', img_data['size'], img_data['bgcolor'])
    
    draw = ImageDraw.Draw(img)
    draw_commands = img_data['draw'](draw)
    
    img.save(f"assets/images/{img_data['name']}")
    print(f"生成{img_data['name']}")

print("所有图片生成完成！") 