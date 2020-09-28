import pandas as pd

dt = pd.to_datetime('20200511')
print(dt, type(dt))
print(dt.day, dt.day_name(), dt.dayofweek, dt.isoweekday(),
      dt.dayofyear, dt.quarter,
      dt.daysinmonth,  # ������������
      dt.is_leap_year, # �������Ƿ�Ϊ����
      dt.month_name(), sep=',')
print(dt.to_pydatetime(), type(dt.to_pydatetime()))
print(pd.to_datetime('202005111409'))
print(pd.to_datetime('20200511140935'))
print(pd.to_datetime('2020051114', format='%Y%m%d%H'))
print(pd.to_datetime('2020��5��11��14ʱ', format='%Y��%m��%d��%Hʱ'))
print(pd.to_datetime('2020��5��11��14ʱ29��', format='%Y��%m��%d��%Hʱ%M��'))
print(pd.to_datetime('2020��5��11��14ʱ29��8��', format='%Y��%m��%d��%Hʱ%M��%S��'))
import pandas as pd

print(pd.to_datetime('2020/5/11'))     # �Զ�����Ϊ��/��/��
print(pd.to_datetime('5/11/2020'))     # �Զ�����Ϊ��/��/��
print(pd.to_datetime('20/5/11'))       # �޷���20����Ϊ�£��Զ�����Ϊ��/��/��
print(pd.to_datetime('11/5/20'))       # ���԰�11����Ϊ�£��Զ�����Ϊ��/��/��
print(pd.to_datetime('11/5/20', dayfirst=True))   # �ѵ�һ���������Ϊ��
print(pd.to_datetime('110520', dayfirst=True))    # �ѵ�һ���������Ϊ��
print(pd.to_datetime('20/5/11', yearfirst=True))  # �ѵ�һ���������Ϊ��
print(pd.to_datetime('2020/5/11'))                # �Զ�����Ϊ��/��/��
print(pd.to_datetime('2020/5/11 22:22:22'))       # ��/��/�� ʱ:��:��
import pandas as pd

print(pd.to_datetime(['20200511', '202005111654', '20200511165405']))  # �Զ��������ݸ�ʽ
print(pd.to_datetime(['2020��5��11��', '2020��05��12��', '2020��05��13��'],
                     format='%Y��%m��%d��'                             # ָ�����ݸ�ʽ
                    ))
from copy import deepcopy
import pandas as pd

# �����������ж���
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.DataFrame({'����1':['20200511', '20200512', '20200513'],
                   '����2':['2020��5��11��', '2020��5��12��', '2020��5��13��'],
                   '����3':['2020��5��11��', '2020��5��12��', '2020��5��13��']
                  })
print(df)
df['����1'] = pd.to_datetime(df['����1'])
df.����2 = pd.to_datetime(df.����2, format='%Y��%m��%d��')
df.����3 = pd.to_datetime(df.����3,
                          format='%Y��%m��%d��').map(str).str.slice(0,7) # �����ַ����ӿ�
df['���ڼ���'] = df.����2.dt.quarter      # �������ڶ���ӿ�
df['�ܼ�'] = df.����2.dt.day_name()       # �������ڶ���ӿ�
print(df)
from urllib.request import urlopen

with urlopen(r'http://ip.42.pl/raw') as fp:
    print(fp.read().decode())
from re import findall
from urllib.request import urlopen, Request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
headers = {'user-agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
          'referer':r'https://www.ip138.com/'}
req = Request(url=r'https://2020.ip138.com/', headers=headers)
with urlopen(req) as fp:
    content = fp.read().decode('gbk')

pattern = r'����iP��ַ�ǣ�[.+?] ���ԣ�.+?\n'
print(','.join(findall(pattern, content)))
