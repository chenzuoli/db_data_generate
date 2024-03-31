# coding=utf-8

# pip install faker

from faker import Faker

fk = Faker(locale="zh-CN")


def name():
    name = fk.name()
    print(name)


def id_card():
    card = fk.ssn()
    print(card)


def phone():
    number = fk.phone_number()
    print(number)


def credit_card():
    card = fk.credit_card_number()
    print(card)


def personal_info():
    # 初始化
    fk = Faker(locale="zh-CN")
    # 1、带邮政编码的地址
    addr = fk.address()
    print(addr)  # 辽宁省张家港县怀柔赵街d座 192553

    # 2、 获取公司名称
    compancy = fk.company()
    print(compancy)  # 彩虹网络有限公司

    # 3、邮箱
    email = fk.email()
    print(email)  # naluo@io.cn

    # 4、获取职称
    job = fk.job()
    print(job)  # 艺术/设计

    # 5、获取城市
    city = fk.city()
    print(city)  # 淮安市
    # 6、获取国家
    country = fk.country()
    print(country)  # 苏里南

    # 7、获取省份
    province = fk.province()
    print(province)  # 内蒙古自治区

    # 8、获取简单的人物信息
    info = fk.simple_profile()
    print(info)

    per = fk.profile()
    print(per)


def desc():
    # 1、生成英文的字符串
    pystring = fk.pystr()
    print(pystring)  # TbXamiNaLAfSruNBRVqG

    # 2、生成词语
    word = fk.word()
    print(word)  # 设备

    # 3、生成一篇文章
    text = fk.text()
    print(text)

    # 4、生成一个随机数
    random_num = fk.random_int(min=1, max=999)
    print(random_num)  # 637


def dt():
    # 1、获取年份
    year = fk.year()
    print(year)  # 2004

    # 2、 获取月份
    month = fk.month()
    print(month)  # 12

    # 3、获取日期
    date = fk.date()
    print(date)  # 2018-06-11

    # 4、获取当前年份:年月日
    now = fk.date_this_year()
    print(now)  # 2022-01-01

    # 5、获取：年月日时分秒
    this_time = fk.date_time()
    print(this_time)  # 1972-11-08 22:30:30

    # 6、自定义年月日格式 年月日 时分秒
    res1 = fk.date_time_between(start_date="-3y", end_date="-1y")
    print(res1)  # 2019-06-17 16:43:42

    # 7、自定义时间范围，3年前到1年前之间的
    res2 = fk.date_between(start_date="-3y", end_date="-1y")
    print(res2)  # 2019-08-01

    # 8、获取未来时间 年月日
    future1 = fk.future_date()
    print(future1)  # 2022-02-01
    # 9、获取未来时间，年月日 时分秒
    future2 = fk.future_datetime()
    print(future2)  # 2022-02-04 13:14:24


def name_list():
    # 生成的数据不重复, 用于批量处理数据
    this_name = fk.name()
    name_list = [fk.unique.name() for i in range(10)]

    print(name_list)


if __name__ == '__main__':
    name()
    id_card()
    phone()
    credit_card()
