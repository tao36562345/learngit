# -*- coding: utf-8 -*-
# ��wsgirefģ�鵼��
from wsgiref.simple_server import make_server
# ���������Լ���д��application����
from hello import application

# ����һ����������IP��ַΪ�գ��˿���8000������������application:
httpd = make_server('127.0.0.1', 8000, application)
print "Serving HTTP on port 8000..."
# ��ʼ����HTTP����
httpd.serve_forever()