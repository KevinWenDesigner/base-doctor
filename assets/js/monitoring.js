// WebSocket连接管理
let ws = null;
let isConnected = false;

// 图表实例管理
const charts = {
    bloodPressure: null,
    bloodSugar: null,
    heartRate: null,
    temperature: null,
    oxygen: null,
    respiration: null
};

// 数据缓存
const dataCache = {
    bloodPressure: [],
    bloodSugar: [],
    heartRate: [],
    temperature: [],
    oxygen: [],
    respiration: []
};

// 初始化WebSocket连接
function initWebSocket() {
    ws = new WebSocket('ws://localhost:8080');

    ws.onopen = () => {
        isConnected = true;
        updateConnectionStatus(true);
        console.log('设备连接成功');
    };

    ws.onclose = () => {
        isConnected = false;
        updateConnectionStatus(false);
        console.log('设备连接断开');
    };

    ws.onerror = (error) => {
        console.error('WebSocket错误:', error);
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        handleDeviceData(data);
    };
}

// 更新连接状态显示
function updateConnectionStatus(connected) {
    const statusElement = document.querySelector('.connection-status');
    const buttonElement = document.querySelector('.connection-button');
    
    if (connected) {
        statusElement.innerHTML = `
            <div class="h-3 w-3 rounded-full bg-green-500 mr-2"></div>
            <span class="text-sm text-gray-500">设备已连接</span>
        `;
        buttonElement.textContent = '断开连接';
        buttonElement.classList.remove('bg-blue-600', 'hover:bg-blue-700');
        buttonElement.classList.add('bg-red-600', 'hover:bg-red-700');
    } else {
        statusElement.innerHTML = `
            <div class="h-3 w-3 rounded-full bg-red-500 mr-2"></div>
            <span class="text-sm text-gray-500">设备未连接</span>
        `;
        buttonElement.textContent = '连接设备';
        buttonElement.classList.remove('bg-red-600', 'hover:bg-red-700');
        buttonElement.classList.add('bg-blue-600', 'hover:bg-blue-700');
    }
}

// 连接/断开设备
function toggleConnection() {
    if (isConnected) {
        ws.close();
    } else {
        initWebSocket();
    }
}

// 处理设备数据
function handleDeviceData(data) {
    const timestamp = new Date();
    
    // 更新实时值显示
    updateRealTimeValue('blood-pressure-value', `${data.bloodPressure.systolic}/${data.bloodPressure.diastolic}`);
    updateRealTimeValue('blood-sugar-value', data.bloodSugar);
    updateRealTimeValue('heart-rate-value', data.heartRate);
    updateRealTimeValue('temperature-value', data.temperature);
    updateRealTimeValue('oxygen-value', data.oxygen);
    updateRealTimeValue('respiration-value', data.respiration);

    // 更新数据缓存
    updateDataCache('bloodPressure', {
        systolic: data.bloodPressure.systolic,
        diastolic: data.bloodPressure.diastolic,
        timestamp: timestamp
    });
    updateDataCache('bloodSugar', { value: data.bloodSugar, timestamp: timestamp });
    updateDataCache('heartRate', { value: data.heartRate, timestamp: timestamp });
    updateDataCache('temperature', { value: data.temperature, timestamp: timestamp });
    updateDataCache('oxygen', { value: data.oxygen, timestamp: timestamp });
    updateDataCache('respiration', { value: data.respiration, timestamp: timestamp });

    // 更新图表
    updateCharts();
}

// 更新实时值显示
function updateRealTimeValue(elementId, value) {
    const element = document.querySelector(`.${elementId}`);
    if (element) {
        element.textContent = value;
    }
}

// 更新数据缓存
function updateDataCache(type, data) {
    dataCache[type].push(data);
    // 保持最近20个数据点
    if (dataCache[type].length > 20) {
        dataCache[type].shift();
    }
}

// 更新图表
function updateCharts() {
    // 血压图表
    if (charts.bloodPressure) {
        charts.bloodPressure.data.datasets[0].data = dataCache.bloodPressure.map(d => ({
            x: d.timestamp,
            y: d.systolic
        }));
        charts.bloodPressure.data.datasets[1].data = dataCache.bloodPressure.map(d => ({
            x: d.timestamp,
            y: d.diastolic
        }));
        charts.bloodPressure.update();
    }

    // 血糖图表
    if (charts.bloodSugar) {
        charts.bloodSugar.data.datasets[0].data = dataCache.bloodSugar.map(d => ({
            x: d.timestamp,
            y: d.value
        }));
        charts.bloodSugar.update();
    }

    // 心率图表
    if (charts.heartRate) {
        charts.heartRate.data.datasets[0].data = dataCache.heartRate.map(d => ({
            x: d.timestamp,
            y: d.value
        }));
        charts.heartRate.update();
    }

    // 体温图表
    if (charts.temperature) {
        charts.temperature.data.datasets[0].data = dataCache.temperature.map(d => ({
            x: d.timestamp,
            y: d.value
        }));
        charts.temperature.update();
    }

    // 血氧图表
    if (charts.oxygen) {
        charts.oxygen.data.datasets[0].data = dataCache.oxygen.map(d => ({
            x: d.timestamp,
            y: d.value
        }));
        charts.oxygen.update();
    }

    // 呼吸率图表
    if (charts.respiration) {
        charts.respiration.data.datasets[0].data = dataCache.respiration.map(d => ({
            x: d.timestamp,
            y: d.value
        }));
        charts.respiration.update();
    }
}

// 保存监测数据
function saveMonitoringData() {
    const patientSelect = document.querySelector('select');
    const selectedPatient = patientSelect.value;
    
    if (!selectedPatient) {
        alert('请选择患者');
        return;
    }

    const data = {
        patient: selectedPatient,
        timestamp: new Date(),
        bloodPressure: dataCache.bloodPressure[dataCache.bloodPressure.length - 1],
        bloodSugar: dataCache.bloodSugar[dataCache.bloodSugar.length - 1],
        heartRate: dataCache.heartRate[dataCache.heartRate.length - 1],
        temperature: dataCache.temperature[dataCache.temperature.length - 1],
        oxygen: dataCache.oxygen[dataCache.oxygen.length - 1],
        respiration: dataCache.respiration[dataCache.respiration.length - 1]
    };

    // 发送数据到服务器
    fetch('/api/monitoring/save', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            alert('数据保存成功');
            updateHistoryTable();
        } else {
            alert('数据保存失败：' + result.message);
        }
    })
    .catch(error => {
        console.error('保存数据失败:', error);
        alert('保存数据失败，请重试');
    });
}

// 更新历史记录表格
function updateHistoryTable() {
    fetch('/api/monitoring/history')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('table tbody');
            tbody.innerHTML = data.map(record => `
                <tr>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">${formatDateTime(record.timestamp)}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${record.patient}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor(record.bloodPressure)}">${record.bloodPressure.systolic}/${record.bloodPressure.diastolic}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor({ value: record.bloodSugar })}">${record.bloodSugar}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor({ value: record.heartRate })}">${record.heartRate}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor({ value: record.temperature })}">${record.temperature}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor({ value: record.oxygen })}">${record.oxygen}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm ${getStatusColor({ value: record.respiration })}">${record.respiration}</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                        <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${getStatusBadgeColor(record)}">
                            ${getStatusText(record)}
                        </span>
                    </td>
                </tr>
            `).join('');
        })
        .catch(error => {
            console.error('获取历史记录失败:', error);
        });
}

// 格式化日期时间
function formatDateTime(date) {
    return new Date(date).toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// 获取状态颜色
function getStatusColor(data) {
    if (data.systolic && data.diastolic) {
        // 血压状态
        if (data.systolic > 140 || data.diastolic > 90) {
            return 'text-red-600';
        }
    } else if (data.value !== undefined) {
        // 其他指标状态
        if (data.value > getThreshold(data).max || data.value < getThreshold(data).min) {
            return 'text-yellow-600';
        }
    }
    return 'text-gray-900';
}

// 获取阈值
function getThreshold(data) {
    const thresholds = {
        bloodSugar: { min: 3.9, max: 6.1 },
        heartRate: { min: 60, max: 100 },
        temperature: { min: 36.3, max: 37.2 },
        oxygen: { min: 95, max: 100 },
        respiration: { min: 12, max: 20 }
    };
    return thresholds[Object.keys(data)[0]] || { min: 0, max: 100 };
}

// 获取状态标签颜色
function getStatusBadgeColor(record) {
    if (hasAbnormalValues(record)) {
        return 'bg-red-100 text-red-800';
    }
    return 'bg-green-100 text-green-800';
}

// 获取状态文本
function getStatusText(record) {
    return hasAbnormalValues(record) ? '异常' : '正常';
}

// 检查是否有异常值
function hasAbnormalValues(record) {
    return (
        record.bloodPressure.systolic > 140 || record.bloodPressure.diastolic > 90 ||
        record.bloodSugar > 6.1 ||
        record.heartRate > 100 || record.heartRate < 60 ||
        record.temperature > 37.2 || record.temperature < 36.3 ||
        record.oxygen < 95 ||
        record.respiration > 20 || record.respiration < 12
    );
}

// 初始化图表
function initCharts() {
    // 血压图表
    charts.bloodPressure = new Chart(document.getElementById('blood-pressure-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '收缩压',
                data: [],
                borderColor: 'rgb(239, 68, 68)',
                tension: 0.1
            }, {
                label: '舒张压',
                data: [],
                borderColor: 'rgb(59, 130, 246)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // 血糖图表
    charts.bloodSugar = new Chart(document.getElementById('blood-sugar-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '血糖',
                data: [],
                borderColor: 'rgb(16, 185, 129)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // 心率图表
    charts.heartRate = new Chart(document.getElementById('heart-rate-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '心率',
                data: [],
                borderColor: 'rgb(239, 68, 68)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // 体温图表
    charts.temperature = new Chart(document.getElementById('temperature-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '体温',
                data: [],
                borderColor: 'rgb(234, 179, 8)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // 血氧图表
    charts.oxygen = new Chart(document.getElementById('oxygen-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '血氧',
                data: [],
                borderColor: 'rgb(99, 102, 241)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });

    // 呼吸率图表
    charts.respiration = new Chart(document.getElementById('respiration-chart'), {
        type: 'line',
        data: {
            datasets: [{
                label: '呼吸率',
                data: [],
                borderColor: 'rgb(168, 85, 247)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'minute'
                    }
                }
            }
        }
    });
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', () => {
    // 初始化图表
    initCharts();

    // 绑定连接按钮事件
    document.querySelector('.connection-button').addEventListener('click', toggleConnection);

    // 绑定保存按钮事件
    document.querySelector('button:contains("保存数据")').addEventListener('click', saveMonitoringData);

    // 加载历史记录
    updateHistoryTable();
}); 