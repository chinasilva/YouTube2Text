import json

def json_to_netscape(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Netscape format header
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# This file was generated by EditThisCookie\n")
        f.write("# Please edit at your own risk!\n\n")
        
        for cookie in cookies:
            domain = cookie['domain'].lstrip('.')
            flag = 'TRUE' if domain.startswith('.') else 'FALSE'
            path = cookie['path']
            secure = 'TRUE' if cookie['secure'] else 'FALSE'
            expiration = str(int(cookie['expirationDate'])) if 'expirationDate' in cookie else '0'
            name = cookie['name']
            value = cookie['value']
            
            f.write(f"{domain}\t{flag}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")

# 使用示例
json_to_netscape('cookies.json', 'cookies.txt')