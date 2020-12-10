from collections import Counter

with open('/var/log/nginx/access.log', 'r') as f:
    ip_list = []
    for line in f.readlines():
        ip = ''
        for char in line:
            if char != ' ':
                ip += char
            else:
                ip_list.append(ip)
                break
        ip_counter = Counter(ip_list)
    f.close()

with open('report.txt', 'w') as f:
    for ip in ip_counter:
        f.write(f'{ip} --> {ip_counter[ip]}\n')
    f.close()
