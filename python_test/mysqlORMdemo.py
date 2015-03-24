# -*-coding: utf-8 -*-
# ����
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ��������Ļ��ࣺ
Base = declarative_base()

# ����User����
class User(Base):
    # �������
    __tablename__ = 'user'

    # ��Ľṹ��
    id = Column(String(20), primary_key = True)
    name = Column(String(20))

# ��ʼ�����ݿ����ӣ�
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# ����DBSession���ͣ�
DBSession = sessionmaker(bind=engine)

# ����session����
session = DBSession()
# ������User����
new_user = User(id='5', name='Bob')
# ��ӵ�session:
session.add(new_user)
# �ύ�����浽���ݿ⣺
session.commit()
# �ر�session:
session��close()