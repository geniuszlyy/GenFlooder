# GenFlooder
A versatile attack simulation tool for testing network security measures. GenFlooder can simulate various types of attacks including UDP DoS, TCP SYN flood, and HTTP flood.

# EN
## Features
- **UDP DoS**: Simulate UDP flood attacks.
- **TCP SYN Flood**: Simulate TCP SYN flood attacks.
- **HTTP Flood**: Simulate HTTP flood attacks.

## Requirements
- Python 3.x
- `colorama` for colored terminal output
- `requests` for HTTP requests
- `aiohttp` for asynchronous HTTP flood attack

## Installation
```bash
pip install colorama requests aiohttp
```

## Usage
```bash
python GenFlooder.py [target] [port] [duration] [attack_type]
```
- **target**: The IP address of the target.
- **port**: The target port.
- **duration**: Duration of the attack in seconds.
- **attack_type**: Type of attack (`UDP`, `TCP`, `HTTP`).

![image](https://github.com/user-attachments/assets/07da4c7f-f320-4ba7-b09c-0b3f7e462ee7)


## Example
```bash
python GenFlooder.py 192.168.1.1 80 60 UDP
```

![image](https://github.com/user-attachments/assets/4b19e190-c656-42b1-b2bb-3a2d108b473f)


## Important
This tool is intended solely for educational purposes. Unauthorized use of this tool against networks or systems without permission is illegal and unethical. Use it responsibly. The author is not responsible for using his program for selfish purposes.

# RU
## Возможности
- **UDP DoS**: Моделирование UDP-флуд атак.
- **TCP SYN Flood**: Моделирование TCP SYN-флуд атак.
- **HTTP Flood**: Моделирование HTTP-флуд атак.

## Требования
- Python 3.x
- `colorama` для цветного вывода в терминале
- `requests` для HTTP-запросов
- `aiohttp` для асинхронных HTTP-флуд атак

## Установка
```bash
pip install colorama requests aiohttp
```

## Использование
```bash
python GenFlooder.py [цель] [порт] [длительность] [тип_атаки]
```
- **цель**: IP-адрес цели.
- **порт**: Целевой порт.
- **длительность**: Длительность атаки в секундах.
- **тип_атаки**: Тип атаки (`UDP`, `TCP`, `HTTP`).

![image](https://github.com/user-attachments/assets/54f0e827-97fd-47d9-b016-75727e90ec20)

## Пример
```bash
python GenFlooder.py 192.168.1.1 80 60 UDP
```

![image](https://github.com/user-attachments/assets/fbbc2636-c3db-4288-b1c6-f7d3cd50b09a)


## Важно
Этот инструмент предназначен исключительно для образовательных целей. Несанкционированное использование этого инструмента против сетей или систем без разрешения является незаконным и неэтичным. Используйте ответственно. Автор не несет ответственности за использование его программы в корыстных целях.
