from collections import Counter
print('1')
with open('/var/log/nginx/access.log', 'r') as f:
    print('2')
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
print('3')
with open('./opt/report.txt', 'w') as f:
    print('4')
    for ip in ip_counter:
        f.write(f'{ip}\t{ip_counter[ip]}\n')
    f.close()
