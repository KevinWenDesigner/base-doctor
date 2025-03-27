from PIL import Image, ImageDraw, ImageFont
import os
import sys

def create_physical_report():
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
    draw.text((width//2 - 100, 50), "健康体检报告", fill=(0, 0, 0), font=title_font)
    
    # 绘制横线
    draw.line([(50, 90), (width-50, 90)], fill=(0, 0, 0), width=2)
    
    # 绘制患者信息
    draw.text((60, 110), "个人信息", fill=(0, 0, 0), font=header_font)
    draw.text((60, 140), "姓名: 张三", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 140), "性别: 男", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 140), "年龄: 45岁", fill=(0, 0, 0), font=normal_font)
    draw.text((60, 170), "体检编号: 2024032603", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 170), "体检机构: 仁爱医院", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 170), "体检日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 200), (width-50, 200)], fill=(0, 0, 0), width=1)
    
    # 绘制体格检查
    draw.text((60, 220), "体格检查", fill=(0, 0, 0), font=header_font)
    physical_items = [
        ["身高", "175 cm", "正常"],
        ["体重", "68 kg", "正常"],
        ["BMI", "22.2 kg/m²", "正常"],
        ["血压", "125/75 mmHg", "正常"],
        ["脉搏", "72 次/分", "正常"]
    ]
    
    table_y = 250
    # 绘制表头
    draw.text((60, table_y), "检查项目", fill=(0, 0, 0), font=normal_font)
    draw.text((300, table_y), "结果", fill=(0, 0, 0), font=normal_font)
    draw.text((500, table_y), "状态", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, table_y + 30), (width-50, table_y + 30)], fill=(0, 0, 0), width=1)
    
    for i, item in enumerate(physical_items):
        row_y = table_y + 40 + i * 30
        draw.text((60, row_y), item[0], fill=(0, 0, 0), font=normal_font)
        draw.text((300, row_y), item[1], fill=(0, 0, 0), font=normal_font)
        
        # 根据状态选择颜色
        if item[2] == "正常":
            draw.text((500, row_y), item[2], fill=(0, 128, 0), font=normal_font)  # 绿色
        else:
            draw.text((500, row_y), item[2], fill=(255, 0, 0), font=normal_font)  # 红色
    
    # 绘制横线
    row_y = table_y + 40 + len(physical_items) * 30
    draw.line([(50, row_y + 10), (width-50, row_y + 10)], fill=(0, 0, 0), width=1)
    
    # 绘制实验室检查
    draw.text((60, row_y + 30), "实验室检查", fill=(0, 0, 0), font=header_font)
    lab_items = [
        ["血红蛋白", "140 g/L", "120-160 g/L", "正常"],
        ["白细胞计数", "6.5×10^9/L", "4.0-10.0×10^9/L", "正常"],
        ["血小板计数", "210×10^9/L", "100-300×10^9/L", "正常"],
        ["血糖", "5.1 mmol/L", "3.9-6.1 mmol/L", "正常"],
        ["总胆固醇", "4.6 mmol/L", "≤5.2 mmol/L", "正常"],
        ["甘油三酯", "1.5 mmol/L", "≤1.7 mmol/L", "正常"],
        ["高密度脂蛋白", "1.2 mmol/L", "≥1.0 mmol/L", "正常"],
        ["低密度脂蛋白", "2.6 mmol/L", "≤3.4 mmol/L", "正常"]
    ]
    
    lab_y = row_y + 60
    # 绘制表头
    draw.text((60, lab_y), "检查项目", fill=(0, 0, 0), font=normal_font)
    draw.text((220, lab_y), "结果", fill=(0, 0, 0), font=normal_font)
    draw.text((350, lab_y), "参考范围", fill=(0, 0, 0), font=normal_font)
    draw.text((500, lab_y), "状态", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, lab_y + 30), (width-50, lab_y + 30)], fill=(0, 0, 0), width=1)
    
    for i, item in enumerate(lab_items):
        row_y = lab_y + 40 + i * 30
        draw.text((60, row_y), item[0], fill=(0, 0, 0), font=normal_font)
        draw.text((220, row_y), item[1], fill=(0, 0, 0), font=normal_font)
        draw.text((350, row_y), item[2], fill=(0, 0, 0), font=normal_font)
        
        # 根据状态选择颜色
        if item[3] == "正常":
            draw.text((500, row_y), item[3], fill=(0, 128, 0), font=normal_font)  # 绿色
        else:
            draw.text((500, row_y), item[3], fill=(255, 0, 0), font=normal_font)  # 红色
    
    # 绘制横线
    row_y = lab_y + 40 + len(lab_items) * 30
    draw.line([(50, row_y + 10), (width-50, row_y + 10)], fill=(0, 0, 0), width=1)
    
    # 绘制总结与建议
    draw.text((60, row_y + 30), "体检总结及健康建议", fill=(0, 0, 0), font=header_font)
    summary = [
        "1. 整体健康状况良好，各项指标在正常范围内。",
        "2. 建议保持良好的生活习惯，规律作息，合理饮食。",
        "3. 每天保持适量运动，控制体重。",
        "4. 建议一年后进行下一次体检。"
    ]
    
    for i, line in enumerate(summary):
        draw.text((60, row_y + 60 + i * 25), line, fill=(0, 0, 0), font=normal_font)
    
    # 绘制底部信息
    draw.text((60, height - 80), "体检医师: 王医师", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 80), "审核医师: 李医师", fill=(0, 0, 0), font=normal_font)
    draw.text((60, height - 50), "体检日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 50), "报告日期: 2024-03-27", fill=(0, 0, 0), font=normal_font)
    
    # 绘制医院名称
    draw.text((width//2 - 100, height - 20), "仁爱医院体检中心", fill=(0, 0, 0), font=header_font)
    
    # 保存图片
    file_path = os.path.join(target_dir, "physical-report-sample.jpg")
    image.save(file_path, quality=95)
    print(f"体检报告图片已生成: {file_path}")
    
    return file_path

if __name__ == "__main__":
    create_physical_report() 