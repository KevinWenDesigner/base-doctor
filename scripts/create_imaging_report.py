from PIL import Image, ImageDraw, ImageFont
import os
import sys

def create_imaging_report():
    # 确保目标目录存在
    target_dir = "assets/images"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 创建空白图片
    width, height = 800, 1100
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    try:
        # 加载字体 (尝试不同的路径)
        font_paths = [
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts', 'simsun.ttc'),
            "C:\\Windows\\Fonts\\simsun.ttc",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
        ]
        
        font_loaded = False
        for font_path in font_paths:
            if os.path.exists(font_path):
                title_font = ImageFont.truetype(font_path, 24)
                header_font = ImageFont.truetype(font_path, 18)
                normal_font = ImageFont.truetype(font_path, 14)
                font_loaded = True
                print(f"使用字体: {font_path}")
                break
                
        if not font_loaded:
            print("找不到合适的字体文件，使用默认字体")
            title_font = ImageFont.load_default()
            header_font = ImageFont.load_default()
            normal_font = ImageFont.load_default()
    except Exception as e:
        print(f"加载字体时出错: {e}")
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        normal_font = ImageFont.load_default()
    
    # 绘制报告标题
    draw.text((width//2 - 100, 50), "影像学检查报告", fill=(0, 0, 0), font=title_font)
    
    # 绘制横线
    draw.line([(50, 90), (width-50, 90)], fill=(0, 0, 0), width=2)
    
    # 绘制患者信息
    draw.text((60, 110), "患者信息", fill=(0, 0, 0), font=header_font)
    draw.text((60, 140), "姓名: 张三", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 140), "性别: 男", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 140), "年龄: 45岁", fill=(0, 0, 0), font=normal_font)
    draw.text((60, 170), "病历号: 2024032602", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 170), "科室: 放射科", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 170), "医生: 李医生", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 200), (width-50, 200)], fill=(0, 0, 0), width=1)
    
    # 绘制检查信息
    draw.text((60, 220), "检查信息", fill=(0, 0, 0), font=header_font)
    draw.text((60, 250), "检查类型: 胸部CT", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 250), "检查日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    draw.text((60, 280), "检查设备: 飞利浦Brilliance 64排螺旋CT", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 310), (width-50, 310)], fill=(0, 0, 0), width=1)
    
    # 绘制影像所见
    draw.text((60, 330), "影像所见", fill=(0, 0, 0), font=header_font)
    findings = [
        "1. 双肺纹理清晰，未见异常密度阴影。",
        "2. 两肺门结构清楚，未见肿大或异常密度灶。",
        "3. 纵隔内未见明显肿大淋巴结。",
        "4. 气管、支气管通畅，无狭窄或扩张。",
        "5. 心脏大小及形态正常，心包未见积液。",
        "6. 胸腔内未见积液或积气。",
        "7. 胸廓完整，未见骨质异常。"
    ]
    
    for i, finding in enumerate(findings):
        draw.text((60, 360 + i * 30), finding, fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 600), (width-50, 600)], fill=(0, 0, 0), width=1)
    
    # 绘制影像诊断
    draw.text((60, 620), "影像诊断", fill=(0, 0, 0), font=header_font)
    draw.text((60, 650), "胸部CT未见明显异常。", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 680), (width-50, 680)], fill=(0, 0, 0), width=1)
    
    # 绘制医生建议
    draw.text((60, 700), "医生建议", fill=(0, 0, 0), font=header_font)
    draw.text((60, 730), "影像学检查未见异常，建议定期复查，注意健康生活方式。", fill=(0, 0, 0), font=normal_font)
    
    # 绘制底部信息
    draw.text((60, height - 100), "检查医师: 王医师", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 100), "审核医师: 赵医师", fill=(0, 0, 0), font=normal_font)
    draw.text((60, height - 70), "检查日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 70), "报告日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    
    # 绘制医院名称
    draw.text((width//2 - 150, height - 40), "仁爱医院放射科", fill=(0, 0, 0), font=header_font)
    
    # 保存图片
    file_path = os.path.join(target_dir, "imaging-report-sample.jpg")
    image.save(file_path, quality=95)
    print(f"影像报告图片已生成: {file_path}")
    
    return file_path

if __name__ == "__main__":
    create_imaging_report() 