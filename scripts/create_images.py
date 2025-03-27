import os
from PIL import Image, ImageDraw
import numpy as np
import random

# 确保目录存在
os.makedirs('assets/images', exist_ok=True)

def create_logo():
    """创建logo图片"""
    img = Image.new('RGBA', (32, 32), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # 绘制蓝色圆形
    draw.ellipse((4, 4, 28, 28), fill=(59, 130, 246))
    # 绘制简化的"医"字
    draw.rectangle((12, 10, 20, 22), fill=(255, 255, 255))
    draw.line((12, 16, 20, 16), fill=(255, 255, 255), width=2)
    img.save('assets/images/logo.png')
    print("生成logo.png")

def create_video_doctor():
    """创建视频问诊图标"""
    img = Image.new('RGBA', (80, 80), color=(219, 234, 254))
    draw = ImageDraw.Draw(img)
    # 绘制摄像头图标
    draw.rectangle((20, 30, 60, 50), outline=(59, 130, 246), width=2)
    draw.polygon([(60, 40), (70, 35), (70, 45)], fill=(59, 130, 246))
    img.save('assets/images/video-doctor.png')
    print("生成video-doctor.png")

def create_patient_info():
    """创建填写信息图标"""
    img = Image.new('RGBA', (24, 24), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # 绘制文档图标
    draw.rectangle((5, 4, 19, 20), outline=(255, 255, 255), width=2)
    # 绘制文档线条
    draw.line((8, 8, 16, 8), fill=(255, 255, 255), width=1)
    draw.line((8, 12, 16, 12), fill=(255, 255, 255), width=1)
    draw.line((8, 16, 16, 16), fill=(255, 255, 255), width=1)
    img.save('assets/images/patient-info.png')
    print("生成patient-info.png")

def create_choose_doctor():
    """创建选择医生图标"""
    img = Image.new('RGBA', (24, 24), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # 绘制人形图标
    draw.ellipse((8, 3, 16, 11), outline=(255, 255, 255), width=2)
    # 绘制身体
    draw.polygon([(12, 11), (7, 21), (17, 21)], outline=(255, 255, 255), width=2)
    img.save('assets/images/choose-doctor.png')
    print("生成choose-doctor.png")

def create_video_call():
    """创建视频诊疗图标"""
    img = Image.new('RGBA', (24, 24), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # 绘制摄像头图标
    draw.rectangle((3, 8, 15, 16), outline=(255, 255, 255), width=2)
    draw.polygon([(15, 12), (21, 9), (21, 15)], outline=(255, 255, 255), width=2)
    img.save('assets/images/video-call.png')
    print("生成video-call.png")

def create_patient_avatar(name, color):
    """创建患者头像"""
    img = Image.new('RGB', (100, 100), color=color)
    draw = ImageDraw.Draw(img)
    
    # 绘制随机形状
    for _ in range(5):
        x1 = random.randint(20, 80)
        y1 = random.randint(20, 80)
        x2 = x1 + random.randint(10, 30)
        y2 = y1 + random.randint(10, 30)
        
        shape_type = random.choice(['rect', 'ellipse'])
        if shape_type == 'rect':
            draw.rectangle((x1, y1, x2, y2), fill=(255, 255, 255, 100))
        else:
            draw.ellipse((x1, y1, x2, y2), fill=(255, 255, 255, 100))
    
    # 绘制头像中心的文字
    text = name[-1]  # 使用1、2、3作为标识
    draw.rectangle([40, 40, 60, 60], fill=color, outline=(255, 255, 255), width=2)
    draw.text((47, 45), text, fill=(255, 255, 255))
    
    # 保存图片
    img.save(f'assets/images/{name}.jpg')
    print(f"生成{name}.jpg")

# 主函数
def main():
    # 创建图标
    create_logo()
    create_video_doctor()
    create_patient_info()
    create_choose_doctor()
    create_video_call()
    
    # 创建患者头像
    colors = [(237, 100, 166), (59, 130, 246), (16, 185, 129)]
    names = ['patient1', 'patient2', 'patient3']
    
    for name, color in zip(names, colors):
        create_patient_avatar(name, color)
    
    print("所有图片生成完成！")

# 执行主函数
if __name__ == "__main__":
    main() 