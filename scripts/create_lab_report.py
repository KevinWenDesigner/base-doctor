from PIL import Image, ImageDraw, ImageFont
import os
import sys

def create_lab_report():
    # 确保目标目录存在
    target_dir = "."
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 创建空白图片
    width, height = 800, 1100
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    try:
        # 加载字体
        font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'fonts', 'simsun.ttc')
        if os.path.exists(font_path):
            title_font = ImageFont.truetype(font_path, 24)
            header_font = ImageFont.truetype(font_path, 18)
            normal_font = ImageFont.truetype(font_path, 14)
        else:
            print(f"找不到字体文件: {font_path}")
            title_font = ImageFont.load_default()
            header_font = ImageFont.load_default()
            normal_font = ImageFont.load_default()
    except Exception as e:
        print(f"加载字体时出错: {e}")
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        normal_font = ImageFont.load_default()
    
    # 绘制报告标题
    draw.text((width//2 - 100, 50), "检验报告单", fill=(0, 0, 0), font=title_font)
    
    # 绘制横线
    draw.line([(50, 90), (width-50, 90)], fill=(0, 0, 0), width=2)
    
    # 绘制患者信息
    draw.text((60, 110), "患者信息", fill=(0, 0, 0), font=header_font)
    draw.text((60, 140), "姓名: 张三", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 140), "性别: 男", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 140), "年龄: 45岁", fill=(0, 0, 0), font=normal_font)
    draw.text((60, 170), "病历号: 2024032601", fill=(0, 0, 0), font=normal_font)
    draw.text((300, 170), "科室: 内科", fill=(0, 0, 0), font=normal_font)
    draw.text((500, 170), "医生: 王医生", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, 200), (width-50, 200)], fill=(0, 0, 0), width=1)
    
    # 绘制检验项目标题
    draw.text((60, 220), "检验项目", fill=(0, 0, 0), font=header_font)
    
    # 绘制表头
    table_y = 260
    draw.text((60, table_y), "项目名称", fill=(0, 0, 0), font=normal_font)
    draw.text((200, table_y), "结果", fill=(0, 0, 0), font=normal_font)
    draw.text((300, table_y), "参考值", fill=(0, 0, 0), font=normal_font)
    draw.text((450, table_y), "单位", fill=(0, 0, 0), font=normal_font)
    draw.text((550, table_y), "状态", fill=(0, 0, 0), font=normal_font)
    
    # 绘制横线
    draw.line([(50, table_y + 30), (width-50, table_y + 30)], fill=(0, 0, 0), width=1)
    
    # 绘制表格数据
    data = [
        ["白细胞计数", "6.5", "4.0-10.0", "10^9/L", "正常"],
        ["红细胞计数", "4.6", "3.5-5.5", "10^12/L", "正常"],
        ["血红蛋白", "140", "120-160", "g/L", "正常"],
        ["血小板计数", "210", "100-300", "10^9/L", "正常"],
        ["中性粒细胞百分比", "65.0", "50.0-70.0", "%", "正常"],
        ["淋巴细胞百分比", "25.0", "20.0-40.0", "%", "正常"],
        ["单核细胞百分比", "4.0", "3.0-8.0", "%", "正常"],
        ["嗜酸性粒细胞百分比", "1.5", "0.5-5.0", "%", "正常"],
        ["嗜碱性粒细胞百分比", "0.5", "0.0-1.0", "%", "正常"],
    ]
    
    for i, row in enumerate(data):
        row_y = table_y + 40 + i * 30
        draw.text((60, row_y), row[0], fill=(0, 0, 0), font=normal_font)
        draw.text((200, row_y), row[1], fill=(0, 0, 0), font=normal_font)
        draw.text((300, row_y), row[2], fill=(0, 0, 0), font=normal_font)
        draw.text((450, row_y), row[3], fill=(0, 0, 0), font=normal_font)
        
        # 状态可能是正常或异常，使用不同颜色
        if row[4] == "正常":
            draw.text((550, row_y), row[4], fill=(0, 128, 0), font=normal_font)  # 绿色表示正常
        else:
            draw.text((550, row_y), row[4], fill=(255, 0, 0), font=normal_font)  # 红色表示异常
    
    # 绘制横线
    row_y = table_y + 40 + len(data) * 30
    draw.line([(50, row_y + 20), (width-50, row_y + 20)], fill=(0, 0, 0), width=1)
    
    # 绘制医生建议
    draw.text((60, row_y + 50), "医生建议", fill=(0, 0, 0), font=header_font)
    draw.text((60, row_y + 80), "各项指标正常，建议保持良好的生活习惯，定期复查。无特殊注意事项。", fill=(0, 0, 0), font=normal_font)
    
    # 绘制底部信息
    draw.text((60, height - 100), "检验医师: 李医师", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 100), "审核医师: 张医师", fill=(0, 0, 0), font=normal_font)
    draw.text((60, height - 70), "检验日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    draw.text((300, height - 70), "报告日期: 2024-03-26", fill=(0, 0, 0), font=normal_font)
    
    # 绘制医院名称
    draw.text((width//2 - 150, height - 40), "仁爱医院检验科", fill=(0, 0, 0), font=header_font)
    
    # 保存图片
    file_path = os.path.join(target_dir, "lab-report-sample.jpg")
    image.save(file_path, quality=95)
    print(f"检验报告图片已生成: {file_path}")
    
    return file_path

if __name__ == "__main__":
    create_lab_report() 