#coding: utf-8
# ����socket�⣺
import socket
# ����һ��socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# �������ӣ�
s.connect(('www.sina.com.cn', 80))

# �������ݣ�
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# ��������
buffer = []
while True:
    # ÿ��������1k�ֽ�
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# �ر�����
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# �ѽ��յ�����д���ļ���
with open('sina.html', 'wb') as f:
    f.write(html)