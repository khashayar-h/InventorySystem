import random
from tabulate import tabulate


#پروژه درس شبیه سازی
#سیستم کنترل موجودی
#استاد مربوطه: دکتر شروان فکری ارشاد
#برنامه نویس:خشایار حقیقی
#شماره شناسایی: 39700816


def rand(v1, v2, v3):

    #موجودی اولیه
    firstInventory = 3
    #سربرگ جدول
    header = ["day", "firstInventory", "demandRandom", "demand", "endInventory", "needed", "bought", "dayRandom",
              "daysLeft"]
    #لیست نتایج
    arr = []

    totalNeed = 0

    totalEndInventory = 0

    for x in range(1, v1+1):

        day = x

        if day == 1:

            bought = check(firstInventory, v3)
            dayRandom = timer()
            daysLeft = checkTimer(dayRandom)

        else:

            dayRandom = None
            daysLeft -= 1

        dayInventory = firstInventory

        demandRandom = random.randint(0, 99)

        if 1 <= demandRandom < 11:
            demand = 0
        elif 10 < demandRandom < 36:
            demand = 1
        elif 35 < demandRandom < 71:
            demand = 2
        elif 70 < demandRandom < 92:
            demand = 3
        elif 91 < demandRandom < 100 or demandRandom == 0:
            demand = 4

        firstInventory = firstInventory - demand

        if firstInventory < 1:
            needed = 0 - firstInventory
        else:
            needed = 0


        if day % v2 == 0:

            bought = check(firstInventory, v3)
            dayRandom = timer()
            daysLeft = checkTimer(dayRandom)

        #برای نمایش null ستون خرید در روز هایی که در آنها خرید انجام نشده

        if day != 1 and day%v2 != 0:
            shownBought = None
        else :
            shownBought = bought

        random_table = [day, dayInventory, demandRandom, demand, firstInventory, needed, shownBought, dayRandom,
                        daysLeft]

        arr.append(random_table)

        totalEndInventory += firstInventory

        if needed > 0:

            totalNeed += 1

        if daysLeft == 1:
            firstInventory += bought

    print(tabulate(arr, header, tablefmt="github"))

    print("متوسط موجودی در انتهای روز : "+str(totalEndInventory/day))

    print("احتمال رخداد کمبود : "+str(totalNeed/day))


#برای چک کردن کمبود انیار


def check(inv, max):
    if inv < max:
        return max-inv


#برای تولید رقم تصادفی مهلت تحویل


def timer():

    return random.randint(0, 9)


#برای چک کردن روز های مانده تا سفارش


def checkTimer(rnd):

    if 0 < rnd < 7:
        return 1
    elif 6 < rnd < 10:
        return 2
    elif rnd == 0:
        return 3


#دریافت ورودی و فراخوانی تابع اصلی
val1 = int(input("تعداد روز های هر دوره را وارد کنید:"))

while val1 > 6 or val1 < 3:
    print("تعداد روز ها باید بین 3 و 6 باشد!")
    val1 = int(input("تعداد روز های هر دوره را مجددا وارد کنید:"))

val2 = int(input("تعداد دور ها را مشخص کنید:"))

while val2 > 7 or val2 < 3:

    print("تعداد دور ها باید بین 3 و 7 باشد!")
    val2 = int(input("تعداد دور ها را مجددا مشخص کنید:"))

val3 = int(input("سقف انبار را مشخص کنید : "))

while val3 < 4 or val3 > 12:

    print("سقف انبار باید بین 4 و 12 باشد!")
    val3 = int(input("سقف انبار را مجددا مشخص کنید : "))

daysCount = val1 * val2

rand(daysCount, val2, val3)