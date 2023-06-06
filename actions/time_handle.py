from datetime import datetime
from dateutil.relativedelta import relativedelta, MO


def search_custom(text, lst_key_search):
    text = text.lower()
    for key in lst_key_search:
        try:
            text.index(key)
            return True
        except:
            None
    return False


def year_format(year: str, Date: object):
    # get number in string
    num = [int(num) for num in year.split() if num.isdigit()]
    if len(num) == 1:
        # exception
        if num[0] < datetime.now().year:
            return False
        # return obj datetime
        if search_custom(year, ["đầu"]):
            # Đầu năm 2022
            if num[0] == Date.year:
                new_date = datetime(
                    year=num[0], month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(days=1)
            # Đầu năm 2023 (2023 > Date.year)
            else:
                new_date = datetime(
                    year=num[0], month=1, day=1, hour=Date.hour, minute=Date.minute)

        elif search_custom(year, ["cuối"]):
            # Cuối năm 2022
            new_date = datetime(
                year=num[0], month=12, day=31, hour=Date.hour, minute=Date.minute)

        elif search_custom(year, ["nữa"]):
            # 1 năm nữa
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(years=num[0])

        # return value of year
        else:
            new_date = datetime(
                year=num[0], month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)

    elif len(num) == 0:
        # return obj datetime
        if search_custom(year, ["đầu"]):

            if search_custom(year, ["sau nữa", "tới nữa"]):
                # Đầu năm sau nữa - Đầu năm tới nữa
                new_date = datetime(year=Date.year, month=1,
                                    day=1, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(years=2)

            elif search_custom(year, ["sau", "tới"]):
                # Đầu năm sau - Đầu năm tới
                new_date = datetime(year=Date.year, month=1,
                                    day=1, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(years=1)

            elif search_custom(year, ["nay", "này"]):
                # Đầu năm nay/này
                new_date = datetime(year=Date.year, month=Date.month,
                                    day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(days=1)

            else:
                new_date = Date

        elif search_custom(year, ["cuối"]):
            if search_custom(year, ["sau nữa", "tới nữa"]):
                # Cuối năm sau nữa - Cuối năm tới nữa
                new_date = datetime(year=Date.year, month=12,
                                    day=31, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(years=2)

            elif search_custom(year, ["sau", "tới"]):
                # Cuối năm sau - Cuối năm tới
                new_date = datetime(year=Date.year, month=12,
                                    day=31, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(years=1)

            elif search_custom(year, ["nay", "này"]):
                # Cuối năm nay/này
                new_date = datetime(year=Date.year, month=12,
                                    day=31, hour=Date.hour, minute=Date.minute)

        elif search_custom(year, ["nữa"]):
            # năm nữa
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(years=1)

        # return value of year
        else:
            new_date = Date
    return new_date


def month_format(month: str, Date: object):
    # get number in string
    num = [int(num) for num in month.split() if num.isdigit()]
    if len(num) == 1:
        # exception
        if Date.year == datetime.now().year and num[0] < datetime.now().month:
            return False
        # return obj datetime
        if search_custom(month, ["đầu"]):
            # Đầu tháng 2
            if num[0] == Date.month:
                new_date = datetime(
                    year=Date.year, month=num[0], day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(days=1)
            # Đầu tháng 3 (3 > Date.month)
            else:
                new_date = datetime(
                    year=Date.year, month=num[0], day=1, hour=Date.hour, minute=Date.minute)

        elif search_custom(month, ["cuối"]):
            # Cuối tháng num[0]
            new_date = datetime(
                year=Date.year, month=num[0], day=Date.day, hour=Date.hour, minute=Date.minute)
            # last day of month
            new_date += relativedelta(day=31)

        elif search_custom(month, ["nữa"]):
            # num[0] tháng nữa
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(months=num[0])

        # return value of year
        else:
            new_date = datetime(
                year=Date.year, month=num[0], day=Date.day, hour=Date.hour, minute=Date.minute)
    else:
        # return obj datetime
        if search_custom(month, ["đầu"]):

            if search_custom(month, ["sau nữa", "tới nữa"]):
                # Đầu tháng sau nữa - Đầu tháng tới nữa
                new_date = datetime(
                    year=Date.year, month=Date.month, day=1, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(months=2)

            elif search_custom(month, ["sau", "tới"]):
                # Đầu tháng sau - Đầu tháng tới
                new_date = datetime(
                    year=Date.year, month=Date.month, day=1, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(months=1)

            else:
                new_date = Date

        elif search_custom(month, ["cuối"]):

            if search_custom(month, ["sau nữa", "tới nữa"]):
                # Cuối tháng sau nữa - Cuối tháng tới nữa
                new_date = datetime(year=Date.year, month=Date.month,
                                    day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(months=2, day=31)

            elif search_custom(month, ["sau", "tới"]):
                # Cuối tháng sau - Cuối tháng tới
                new_date = datetime(year=Date.year, month=Date.month,
                                    day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(months=1, day=31)

        elif search_custom(month, ["nữa"]):
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(months=1)

        # return value of year
        else:
            new_date = Date
    return new_date


def week_format(week: str, Date: object):
    # get number in string
    num = [int(num) for num in week.split() if num.isdigit()]
    if len(num) == 1:
        # return obj datetime
        if search_custom(week, ["sau", "nữa", "tới"]):
            # T2 của: 1 tuần sau - 1 tuần nữa - 1 tuần tới
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(days=1, weekday=MO(num[0]))
        # return value of year
        else:
            new_date = Date

    else:
        if search_custom(week, ["cuối"]):
            if search_custom(week, ["sau", "tới"]):
                if search_custom(week, ["nữa"]):
                    # Cuối tuần sau nữa - Cuối tuần tới nữa
                    new_date = datetime(
                        year=Date.year, month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)
                    # T2 của 2 tuần sau
                    new_date += relativedelta(days=1, weekday=MO(2))
                    # CN của 2 tuần sau
                    new_date += relativedelta(days=6)

                else:
                    # Cuối tuần sau - Cuối tuần tới
                    new_date = datetime(
                        year=Date.year, month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)
                    # T2 của 1 tuần sau
                    new_date += relativedelta(days=1, weekday=MO(1))
                    # CN của 1 tuần sau
                    new_date += relativedelta(days=6)
        else:
            # return obj datetime
            if search_custom(week, ["sau", "tới"]):
                if search_custom(week, ["nữa"]):
                    # Đầu tuần sau nữa - Đầu tuần tới nữa - Tuần tới nữa
                    new_date = datetime(
                        year=Date.year, month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)
                    # T2 của 2 tuần sau
                    new_date += relativedelta(days=1, weekday=MO(2))

                else:
                    # Đầu tuần sau - Đầu tuần tới - Tuần tới - Tuần sau
                    new_date = datetime(
                        year=Date.year, month=Date.month, day=Date.day, hour=Date.hour, minute=Date.minute)
                    # T2 của 1 tuần sau
                    new_date += relativedelta(days=1, weekday=MO(1))

            elif search_custom(week, ["nữa"]):
                # Tuần nữa
                new_date = datetime(year=Date.year, month=Date.month,
                                    day=Date.day, hour=Date.hour, minute=Date.minute)
                # T2 của 1 tuần sau
                new_date += relativedelta(days=1, weekday=MO(1))

            else:
                new_date = Date
    return new_date


def weekday_format(weekday: str, Date: object):
    # get number in string
    num = [int(num) for num in weekday.split() if num.isdigit()]
    lst_week_day = [2, 3, 4, 5, 6, 7, "chủ nhật"]
    new_date = Date
    if len(num) == 1:
        try:
            week_day = lst_week_day.index(num[0])
            # T2 - T3 - T4 - T5 - T6 - T7
            new_date += relativedelta(weekday=week_day)
        except:
            None
    elif search_custom(weekday, ["chủ nhật"]):
        # Chủ nhật
        new_date += relativedelta(weekday=6)

    return new_date


def day_format(day: str, Date: object):
    # get number in string
    num = [int(num) for num in day.split() if num.isdigit()]

    if len(num) == 1:
        # return obj datetime
        # 5 ngày nữa
        new_date = datetime(year=Date.year, month=Date.month,
                            day=Date.day, hour=Date.hour, minute=Date.minute)
        new_date += relativedelta(days=num[0])

    else:
        # Ngày mai - Ngày hôm sau - mai
        if search_custom(day, ["mai", "sau"]):
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(days=1)

        elif search_custom(day, ["mốt", "kia"]):
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(days=2)

        else:
            new_date = Date
    return new_date


def time_format(time: str, Date: object):
    num = [int(num) for num in time.split()
           if num.isdigit()]  # get number in string
    # 1h chiều -> 13h
    # 10h tối  -> 22h
    if num != []:
        if search_custom(time, ["chiều", "tối"]):
            if num[0] < 12:
                num[0] += 12

    if len(num) == 1:
        if search_custom(time, ["rưỡi"]):
            if search_custom(time, ["nữa"]):
                # 1 tiếng rưỡi nữa
                new_date = datetime(year=Date.year, month=Date.month,
                                    day=Date.day, hour=Date.hour, minute=Date.minute)
                new_date += relativedelta(hours=num[0], minutes=30)
            else:
                # 10 rưỡi -> 10:30
                new_date = datetime(
                    year=Date.year, month=Date.month, day=Date.day, hour=num[0], minute=30)

        elif search_custom(time, ["nữa"]):
            # 1 tiếng nữa
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=Date.hour, minute=Date.minute)
            new_date += relativedelta(hours=num[0])

        else:
            # 10h
            new_date = datetime(
                year=Date.year, month=Date.month, day=Date.day, hour=num[0])

    elif len(num) == 2:
        if search_custom(time, ["kém", "thiếu"]):
            # 10h kém 15 -> 9:45
            new_date = datetime(
                year=Date.year, month=Date.month, day=Date.day, hour=num[0])
            # - num[1] minutes
            new_date -= relativedelta(minutes=num[1])

        else:
            # 10h30
            new_date = datetime(year=Date.year, month=Date.month,
                                day=Date.day, hour=num[0], minute=num[1])
    else:
        if search_custom(time, ["trưa"]):
            # Trưa nay - Sau giờ trưa - Đầu giờ trưa
            new_date = datetime(
                year=Date.year, month=Date.month, day=Date.day, hour=13)

        elif search_custom(time, ["chiều", "tối", "tan", "làm", "ca"]):
            # Chiều nay - Tối nay - Tan làm - Tan ca - Sau giờ làm - Sau ca làm việc
            new_date = datetime(
                year=Date.year, month=Date.month, day=Date.day, hour=18)

        elif search_custom(time, ["chút", "chốc", "tí", "xíu", "hồi", "lát", "nữa"]):
            new_date = datetime(
                year=Date.year, month=Date.month, day=Date.day, hour=Date.hour)
            # + 1 hours
            new_date += relativedelta(hours=1)

        else:
            new_date = Date
    return new_date

# Date = datetime.now()
# print(time_format("9 giờ sáng", Date))