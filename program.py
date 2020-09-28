import pandas as pd

dt = pd.to_datetime('20200511')
print(dt, type(dt))
print(dt.day, dt.day_name(), dt.dayofweek, dt.isoweekday(),
      dt.dayofyear, dt.quarter,
      dt.daysinmonth,  # 所在月总天数
      dt.is_leap_year, # 所在年是否为闰年
      dt.month_name(), sep=',')
print(dt.to_pydatetime(), type(dt.to_pydatetime()))
print(pd.to_datetime('202005111409'))
print(pd.to_datetime('20200511140935'))
print(pd.to_datetime('2020051114', format='%Y%m%d%H'))
print(pd.to_datetime('2020年5月11日14时', format='%Y年%m月%d日%H时'))
print(pd.to_datetime('2020年5月11日14时29分', format='%Y年%m月%d日%H时%M分'))
print(pd.to_datetime('2020年5月11日14时29分8秒', format='%Y年%m月%d日%H时%M分%S秒'))
import pandas as pd

print(pd.to_datetime('2020/5/11'))     # 自动解释为年/月/日
print(pd.to_datetime('5/11/2020'))     # 自动解释为月/日/年
print(pd.to_datetime('20/5/11'))       # 无法把20解释为月，自动解释为日/月/年
print(pd.to_datetime('11/5/20'))       # 可以把11解释为月，自动解释为月/日/年
print(pd.to_datetime('11/5/20', dayfirst=True))   # 把第一个数字理解为日
print(pd.to_datetime('110520', dayfirst=True))    # 把第一组数字理解为日
print(pd.to_datetime('20/5/11', yearfirst=True))  # 把第一组数字理解为年
print(pd.to_datetime('2020/5/11'))                # 自动解释为年/月/日
print(pd.to_datetime('2020/5/11 22:22:22'))       # 年/月/日 时:分:秒
import pandas as pd

print(pd.to_datetime(['20200511', '202005111654', '20200511165405']))  # 自动解释数据格式
print(pd.to_datetime(['2020年5月11日', '2020年05月12日', '2020年05月13日'],
                     format='%Y年%m月%d日'                             # 指定数据格式
                    ))
from copy import deepcopy
import pandas as pd

# 设置输出结果列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df = pd.DataFrame({'日期1':['20200511', '20200512', '20200513'],
                   '日期2':['2020年5月11日', '2020年5月12日', '2020年5月13日'],
                   '日期3':['2020年5月11日', '2020年5月12日', '2020年5月13日']
                  })
print(df)
df['日期1'] = pd.to_datetime(df['日期1'])
df.日期2 = pd.to_datetime(df.日期2, format='%Y年%m月%d日')
df.日期3 = pd.to_datetime(df.日期3,
                          format='%Y年%m月%d日').map(str).str.slice(0,7) # 调用字符串接口
df['所在季度'] = df.日期2.dt.quarter      # 调用日期对象接口
df['周几'] = df.日期2.dt.day_name()       # 调用日期对象接口
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

pattern = r'您的iP地址是：[.+?] 来自：.+?\n'
print(','.join(findall(pattern, content)))
