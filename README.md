# Server Monitor

一个使用 Python 编写的简单服务器监控 CLI 工具。

Server Monitor 可以在终端中实时查看服务器的 CPU、内存和磁盘使用率，并根据设定的阈值显示当前状态。

## Features

* 查看 CPU 使用率
* 查看内存使用率
* 查看磁盘使用率
* 显示主机名
* 显示当前时间
* CPU / Memory / Disk 高负载提示
* 支持持续监控
* 支持单次执行模式
* 支持自定义监控间隔
* 支持 Ctrl+C 优雅退出
* 包含 pytest 自动化测试

## Requirements

* Python 3.10+
* psutil
* pytest

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/snowball-bit/server-monitor.git
cd server-monitor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

激活虚拟环境：

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install psutil pytest
```

## Usage

### Continuous monitoring

默认每 5 秒刷新一次：

```bash
python monitor.py
```

### Custom interval

例如每 2 秒刷新一次：

```bash
python monitor.py --interval 2
```

### Run once

只获取一次系统状态：

```bash
python monitor.py --once
```

## Example Output

```text
Server Monitor
Host: MS-31469
2026-10-03 12:00:00

CPU Usage: 12.5% [OK]
Memory Usage: 35.2% [OK]
Disk Usage: 42.1% [OK]
```

## Testing

运行全部测试：

```bash
python -m pytest
```

测试内容包括：

* 系统状态返回值
* 返回值类型
* 必要字段
* CPU / Memory / Disk 数值范围
* 状态阈值判断
* CLI 参数解析
* 正整数参数验证

## Project Structure

```text
server-monitor/
├── monitor.py
├── server_monitor/
│   ├── __init__.py
│   └── system.py
├── tests/
│   └── test_system.py
├── .gitignore
└── README.md
```

## How It Works

```text
Operating System
       ↓
     psutil
       ↓
get_system_status()
       ↓
    Python dict
       ↓
  format_status()
       ↓
    Terminal
```

系统信息由 `psutil` 获取，然后由程序进行格式化并显示在终端中。

## License

MIT

