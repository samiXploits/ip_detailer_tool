import requests
import os
from datetime import datetime
from prettytable import PrettyTable
import threading
import colorama
from colorama import Fore, Style
import socket

# Initialize colorama
colorama.init()

IPINFO_ACCESS_TOKEN = ""  # Add your IPinfo access token here

# IPinfo API URL with your token
url = f"https://ipinfo.io/{{}}/json?token={IPINFO_ACCESS_TOKEN}"

# Hacker-style Banner with colorama
HACKER_BANNER = f"""
{Fore.GREEN}
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ▄▄▄       ███▄    █   ██████ 
▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▒██    ▒ 
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒░ ▓██▄   
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒  ▒   ██▒
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░▒██████▒▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░░ ░▒  ░ ░
░  ░  ░  ░░         ░   ▒   ░      ░     ░   ▒      ░   ░ ░ ░  ░  ░  
      ░                 ░  ░       ░         ░  ░         ░       ░  
{Fore.CYAN}                                                                      
                IP Information Lookup Tool - Created by Mr. Sami
{Style.RESET_ALL}
"""

def check_internet_connection():
    try:
        # Try to connect to a reliable host
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

def fetch_ip_info(ip_address):
    response = requests.get(url.format(ip_address))
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None  # Return None for failure

def save_report(ip_address, data):
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)

    report_file_path = os.path.join(reports_dir, f'ip_info_report_{ip_address}.html')

    html_content = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IP Address Information</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" rel="stylesheet"/>
        <style>
            body {{ background-color: #000; color: #0f0; font-family: 'Courier New', Courier, monospace; }}
            .container {{ margin-top: 50px; padding: 20px; background-color: #111; box-shadow: 0px 4px 8px rgba(0, 255, 0, 0.1); border-radius: 10px; }}
            h1 {{ text-align: center; color: #0f0; font-size: 40px; margin-bottom: 20px; }}
            table {{ width: 100%; margin-top: 20px; }}
            th {{ background-color: #0f0; color: #000; font-weight: bold; text-align: center; }}
            tr:nth-child(even) {{ background-color: #222; }}
            td {{ padding: 12px; text-align: center; color: #0f0; }}
            .banner {{ color: #0f0; font-size: 30px; text-align: center; font-weight: bold; margin-bottom: 30px; }}
            footer {{ text-align: center; margin-top: 30px; font-size: 14px; color: #0f0; }}
        </style>
    </head>
    <body>
        <div class="container animate__animated animate__fadeInUp">
            <div class="banner animate__animated animate__zoomIn">IP Information Lookup</div>
            <h1>Details for IP: {ip_address}</h1>
            <table class="table table-bordered">
                <tr><th>Field</th><th>Details</th></tr>
                <tr><td>IP Address</td><td>{data.get('ip', 'N/A')}</td></tr>
                <tr><td>Hostname</td><td>{data.get('hostname', 'N/A')}</td></tr>
                <tr><td>City</td><td>{data.get('city', 'N/A')}</td></tr>
                <tr><td>Region</td><td>{data.get('region', 'N/A')}</td></tr>
                <tr><td>Country</td><td>{data.get('country', 'N/A')}</td></tr>
                <tr><td>Location</td><td>{data.get('loc', 'N/A')}</td></tr>
                <tr><td>Postal Code</td><td>{data.get('postal', 'N/A')}</td></tr>
                <tr><td>Timezone</td><td>{data.get('timezone', 'N/A')}</td></tr>
            </table>
            <footer><p>&copy; {datetime.now().year} - Created by Mr. Sami</p></footer>
        </div>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    with open(report_file_path, 'w') as file:
        file.write(html_content)
    print(f"{Fore.GREEN}Report for IP {ip_address} saved to {report_file_path}{Style.RESET_ALL}")

def display_results_table(results):
    table = PrettyTable()
    table.field_names = [f"{Fore.CYAN}IP Address{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Hostname{Style.RESET_ALL}", 
                         f"{Fore.CYAN}City{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Region{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Country{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Location{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Postal Code{Style.RESET_ALL}", 
                         f"{Fore.CYAN}Timezone{Style.RESET_ALL}"]
    
    for ip_data in results:
        if ip_data:
            table.add_row([
                f"{Fore.GREEN}{ip_data.get('ip', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.YELLOW}{ip_data.get('hostname', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.MAGENTA}{ip_data.get('city', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.BLUE}{ip_data.get('region', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.RED}{ip_data.get('country', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.CYAN}{ip_data.get('loc', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.WHITE}{ip_data.get('postal', 'N/A')}{Style.RESET_ALL}",
                f"{Fore.GREEN}{ip_data.get('timezone', 'N/A')}{Style.RESET_ALL}"
            ])
    
    print(table)

def main():
    if not check_internet_connection():
        print(f"{Fore.RED}No internet connection. Please check your network settings.{Style.RESET_ALL}")
        return

    print(HACKER_BANNER)
    ip_addresses = input(f"{Fore.YELLOW}Enter IP Addresses separated by commas: {Style.RESET_ALL}").strip().split(',')
    
    results = []
    threads = []
    for ip in ip_addresses:
        ip = ip.strip()
        thread = threading.Thread(target=lambda ip=ip: results.append(fetch_ip_info(ip)), args=())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    display_results_table(results)

    # Save HTML reports for each IP
    for ip_data in results:
        if ip_data:
            save_report(ip_data.get('ip'), ip_data)

if __name__ == "__main__":
    main()