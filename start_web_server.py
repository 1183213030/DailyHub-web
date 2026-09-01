#!/usr/bin/env python3
# start_web_server.py
# Local LAN preview server for DailyHub WebClip (for testing on ordinary iPhones)

import os
import sys
import socket
import http.server
import socketserver
from pathlib import Path

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def run_server(port=8080):
    web_dir = Path(__file__).parent.resolve()
    os.chdir(web_dir)
    
    lan_ip = get_lan_ip()
    print("==================================================")
    print("  DailyHub WebClip / PWA 局域网预览与安装服务     ")
    print("==================================================")
    print(f"[*] 本机访问地址: http://localhost:{port}/index.html")
    print(f"[*] 任意 iPhone (连接同一 Wi-Fi) 访问地址:")
    print(f"    👉 http://{lan_ip}:{port}/index.html")
    print("--------------------------------------------------")
    print("[*] iPhone Safari 安装步骤:")
    print("    1. 在 Safari 中打开上方网址；")
    print("    2. 点击底部「分享」图标（方框带向上箭头）；")
    print("    3. 选择「添加到主屏幕」（Add to Home Screen）；")
    print("    4. 即可在手机桌面上生成永久高清独立 App！")
    print("==================================================")

    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] 服务已停止。")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
