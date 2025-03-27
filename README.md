# 汉唐医生基层版

<p align="center">
  <img src="assets/images/logo.png" alt="汉唐医生基层版" width="120">
</p>

<p align="center">
  基层医疗机构专用智慧医疗平台，打造基层智慧医疗新模式
</p>

<p align="center">
  <a href="#功能特性">功能特性</a> •
  <a href="#技术路线">技术栈</a> •
  <a href="#快速开始">快速开始</a> •
  <a href="#项目结构">项目结构</a> •
  <a href="#演示截图">演示截图</a> •
  <a href="#贡献指南">贡献指南</a> •
  <a href="#许可证">许可证</a>
</p>

## 项目介绍

汉唐医生基层版是专为基层医疗机构设计的智慧医疗平台，集成患者管理、健康监测、远程会诊、随访管理和医生工作站五大核心功能模块，助力基层医疗机构提升诊疗水平、优化医患体验、强化慢病管理。

## 功能特性

本项目提供以下五大核心功能模块：

### 🧑‍⚕️ 患者管理系统

- 患者档案管理：创建和维护完整的患者电子档案
- 分类筛选查询：按时间范围、患者状态等多维度筛选患者
- 异常标记管理：实时标记血压异常、血糖异常等健康风险
- 患者详情查看：展示患者基本信息、就诊历史和监测数据

### 📊 健康监测平台

- 多项指标监测：支持血压、血糖、心率、体温、血氧和呼吸率等实时监测
- 异常数据预警：自动识别并标记异常生理指标数据
- 历史记录查询：以表格形式展示患者历史监测记录
- 设备连接管理：支持医疗监测设备的连接和数据采集

### 🎥 远程会诊系统

- 远程视频会诊：与上级医院专家进行实时视频沟通
- 专家协作诊断：共享患者信息和监测数据进行协作诊断
- 会诊记录管理：记录和查询历史会诊记录
- 会诊预约管理：安排和管理远程会诊预约

### 📅 智能随访管理

- 随访计划创建：根据不同类型创建个性化随访计划
- 患者分类管理：支持术后随访、慢病管理、复诊提醒、用药指导等分类
- 时间计划安排：按今日、三日内、七日内等时间范围规划随访任务
- 随访记录管理：记录随访结果和下一步随访计划

### 👩‍⚕️ 医生工作站

- 个人信息管理：编辑医生个人资料和专业背景
- 专业技能展示：管理医生的擅长领域和专业特长
- 系统功能设置：包括数据同步、通知设置和安全中心等功能
- 绩效管理工具：提供医务人员工作绩效分析和管理

## 技术栈

- 前端框架：HTML5, CSS3, JavaScript
- UI 框架：Tailwind CSS
- 图表库：Chart.js
- 图标库：Font Awesome
- 响应式设计：适配移动端和桌面端

## 快速开始

### 前提条件

- 现代浏览器（Chrome, Firefox, Safari, Edge等）
- 本地Web服务器（如 Live Server, XAMPP, WAMP等）

### 安装步骤

1. 克隆仓库到本地
```bash
git clone https://github.com/yourusername/doctor.git
cd doctor
```

2. 使用Web服务器打开项目
```bash
# 如果使用 VS Code + Live Server
code .
# 然后点击右下角的 "Go Live" 按钮
```

3. 在浏览器中访问
```
http://localhost:5500/pages/dashboard.html
```

## 项目结构

```
doctor/
├── assets/            # 静态资源文件
│   ├── images/        # 图片资源
│   ├── js/            # JavaScript文件
│   └── css/           # CSS样式文件
├── pages/             # 页面文件
│   ├── dashboard.html # 应用首页/仪表盘
│   ├── patients.html  # 患者管理
│   ├── monitoring.html# 健康监测
│   ├── consultation.html # 远程会诊
│   ├── schedule.html  # 随访管理
│   └── profile.html   # 医生工作站
└── README.md          # 项目说明文档
```

## 演示截图

<p align="center">
  <img src="path/to/screenshot1.png" alt="患者管理" width="200">
  <img src="path/to/screenshot2.png" alt="健康监测" width="200">
  <img src="path/to/screenshot3.png" alt="远程会诊" width="200">
</p>

## 贡献指南

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建一个 Pull Request

## 许可证

根据 MIT 许可证分发。更多信息请查看 `LICENSE` 文件。

## 联系我们

- 项目维护者: [您的名字](mailto:your.email@example.com)
- 项目主页: [https://github.com/yourusername/doctor](https://github.com/yourusername/doctor)

---

<p align="center">
  © 2024 汉唐医生基层版. 保留所有权利.
</p> 