import os
import requests
from PIL import Image
from io import BytesIO
import urllib3
import time

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 创建目录
def create_directories():
    """创建必要的目录"""
    directories = [
        'assets/images',
        'assets/images/doctors',
        'assets/images/departments',
        'assets/images/icons',
        'assets/images/backgrounds'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

# 下载图片
def download_image(url, save_path, size=None, max_retries=3):
    """下载并处理图片"""
    for attempt in range(max_retries):
        try:
            # 设置请求头和超时
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            # 禁用代理
            proxies = {
                'http': None,
                'https': None
            }
            # 发送请求
            response = requests.get(
                url,
                headers=headers,
                verify=False,
                proxies=proxies,
                timeout=60  # 增加超时时间到60秒
            )
            response.raise_for_status()
            
            # 打开图片
            img = Image.open(BytesIO(response.content))
            
            # 如果是RGBA模式，转换为RGB
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # 调整大小
            if size:
                img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # 保存图片
            img.save(save_path, quality=95)
            print(f"Successfully processed: {save_path}")
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed for {save_path}: {str(e)}")
                time.sleep(2)  # 等待2秒后重试
            else:
                print(f"Error processing {save_path} after {max_retries} attempts: {str(e)}")
                return False

# 处理图片
def process_image(input_path, output_path, size=None):
    try:
        img = Image.open(input_path)
        if size:
            img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path, optimize=True, quality=85)
        print(f"Successfully processed: {output_path}")
        return True
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")
    return False

# 图片资源配置
image_resources = {
    # 系统图标
    'logo': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/logo.png',
        'size': (200, 200)
    },
    'favicon': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/favicon.ico',
        'size': (32, 32)
    },
    
    # 医生头像
    'doctor1': {
        'url': 'https://images.unsplash.com/photo-1622253692010-333f2da6031d',
        'path': 'assets/images/doctors/doctor-avatar-1.jpg',
        'size': (200, 200)
    },
    'doctor2': {
        'url': 'https://images.unsplash.com/photo-1622253692010-333f2da6031d',
        'path': 'assets/images/doctors/doctor-avatar-2.jpg',
        'size': (200, 200)
    },
    'doctor3': {
        'url': 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d',
        'path': 'assets/images/doctors/doctor-avatar-3.jpg',
        'size': (200, 200)
    },
    
    # 科室图标
    'department_internal': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/departments/department-internal.png',
        'size': (64, 64)
    },
    'department_surgery': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/departments/department-surgery.png',
        'size': (64, 64)
    },
    'department_pediatrics': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/departments/department-pediatrics.png',
        'size': (64, 64)
    },
    'department_ophthalmology': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/departments/department-ophthalmology.png',
        'size': (64, 64)
    },
    'department_dental': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/departments/department-dental.png',
        'size': (64, 64)
    },
    
    # 功能图标
    'icon_consultation': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/icons/icon-consultation.png',
        'size': (32, 32)
    },
    'icon_schedule': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/icons/icon-schedule.png',
        'size': (32, 32)
    },
    'icon_prescription': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/icons/icon-prescription.png',
        'size': (32, 32)
    },
    'icon_medical_record': {
        'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
        'path': 'assets/images/icons/icon-medical-record.png',
        'size': (32, 32)
    },
    
    # 背景图片
    'bg_login': {
        'url': 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3',
        'path': 'assets/images/backgrounds/bg-login.jpg',
        'size': (1920, 1080)
    },
    'bg_home': {
        'url': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118',
        'path': 'assets/images/backgrounds/bg-home.jpg',
        'size': (1920, 1080)
    },
    
    # 其他图片
    'placeholder_patient': {
        'url': 'https://images.unsplash.com/photo-1622253692010-333f2da6031d',
        'path': 'assets/images/placeholder-patient.jpg',
        'size': (200, 200)
    },
    'placeholder_report': {
        'url': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118',
        'path': 'assets/images/placeholder-report.jpg',
        'size': (800, 600)
    }
}

def main():
    # 只下载眼科图标
    image_resource = {
        'department_ophthalmology': {
            'url': 'https://cdn-icons-png.flaticon.com/512/3774/3774299.png',
            'path': 'assets/images/departments/department-ophthalmology.png',
            'size': (64, 64)
        }
    }
    
    # 下载并处理图片
    for name, config in image_resource.items():
        print(f"\nProcessing {name}...")
        download_image(config['url'], config['path'], config['size'])

if __name__ == '__main__':
    main() 