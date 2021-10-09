from datetime import datetime 
currect_time_min = datetime.now().strftime('%M')
currect_time_hour = datetime.now().strftime('%H')

your_time = input('Enter your time (view like hh:mm) ' )
right = your_time.split(':')

min_under_30 = {"01" : "Одна минута ", "02" : "Две минуты ", "03" : "Три минуты ", "04" : "Четыре минуты ", "05" : "Пять минут ", "06" : "Шесть минут ", \
    "07" : "Семь минут ", "08" : "Восемь минут ", "09" : "Девять минут ", "10" : "Десять минут ", \
    "11" : "Одинадцать минут ", "12" : "Двенадцать минут ", "13" : "Тринадцать минут ", "14" : "Четырнадцать минут ", \
    "15" : "Пятнадцать минут ", "16" : "Шестнадцать минут ", "17" : "Семнадцать минут", "18" : "Восемандцать минут ", \
    "19" : "Девятнадцать минут", "20" : "Двадцать минут ", "21" : "Двадцать одна минута", "22" : "Двадцать две минуты ", \
    "23" : "Двадцать три минуты ", "24" : "Двадцать четыре минуты ", "25" : "Двадцать пять минут 13", \
    "26" : "Двадцать шесть минут ", "27" : "Двадцать семь ", "28" : "Двадцать восеь минут", "29" : "Двадцать девять минут "}
min_equally_30 = {"30" : "Половина "}
min_more_30_less_45 = {"31" : "Тридцать одна минута ", "32" : "Тридцать две минуты ", "33" : "Тридцать три минуты ", "34" : "Тридцать четыре минуты", \
    "35" : "Тридцать пять минут ", "36" : "Тридцать шесть минут", "37" : " Тридцать семь минут ", "38" : "Тридцать восемь минут ", \
    "39" : "Тридцать девять минут", "40" : "Сорок минут ", "41" : "Сорок одна минута ", "42" : "Сорок две минуты", "43" : "Сорок три минуты", \
    "44" : "Сорок четыре минуты "}
min_more_45 = {"45" : "Без пятнадцати минут ", "46" : "Без четырнадцати минут ", "47" : "Без тринадцати минут ", \
    "48" : "Без двенадцати минут ", "49" : "Без одинадцати минут ", "50" : "Без десяти минут ", "51" : "Без девяти минут", "52" : "Без восьми минут", \
    "53" : "Без семи минут ", "54" : "Без шести минут ", "55" : "Без пяти минут ", "56" : "Без четырех минут", "57" : "Без трех минут ", \
    "58" : "Без двух минут ", "59" : "Без одной минуты "}
hour = { "00" : "первого", "01" : "второго", "02" : "третьего", "03" : "четвертого", "04" : "пятого", "05" : "шестого", \
    "06" : "седьмого", "07" : "восьмого", "08" : "девятого", "09" : "десятого", "10" : "одинадцатого", "11" : "двенадцатого", \
    "12" : "первого", "13" : "второго", "14" : "третьего", "15" : "четвертого", "16" : "пятого", "17" : "шестого", "18" : "седьмого", \
    "19" : "восьмого", "20" : "девятого", "21" : "десятого", "22" : "одинадцатого", "23" : "двенадцатого"}
hour_more_45 = {"00" : "час", "01" : "два", "02" : "три", "03" : "четыре", "04" : "пять", "05" : "шесть", \
    "06" : "семь", "07" : "восемь", "08" : "девять", "09" : "десять", "10" : "одинадцать", "11" : "двенадцать", \
    "12" : "час", "13" : "два", "14" : "три", "15" : "четыре", "16" : "пять", "17" : "шесть", "18" : "семь", \
    "19" : "восемь", "20" : "девять", "21" : "десять", "22" : "одинадцать", "23" : "двенадцать"}
min_eq_00 = {"01" : "Час ночи", "02" : "Два часа ночи", "03" : "Три часа ночи", "04" : "Четыре часа утра", "05" : "Пять часов утра", "06" : "Шесть часов утра", \
    "07" : "Семь часов утра", "08" : "Восемь часов утра", "09" : "Девять часов утра", "10" : "Десять часов утра", \
    "11" : "Одинадцать часов утра", "12" : "Полдень", "13" : "Час дня", "14" : "Два часа дня", "15" : "Три часа дня", \
    "16" : "Четыре часа дня", "17" : "Пять часов дня", "18" : "Шесть часов вечера", "19" : "Семь часов вечера", \
    "20" : "Восемь часов вечера", "21" : "Девять часов вечера", "22" : "Десять часов вечера", "23" : "Одинадцать часов вечера", \
    "00" : "Полночь"}

if int(currect_time_min) == 00 :
        print(min_eq_00.get(currect_time_hour))
if int(currect_time_min) < 30 :
    if int(currect_time_min) >= 1:
        print(min_under_30.get(currect_time_min) + hour.get(currect_time_hour))
elif int(currect_time_min) == 30 :
    print(min_equally_30.get(currect_time_min) + hour.get(currect_time_hour))
elif int(currect_time_min) > 30:
    if int(currect_time_min) < 45:
        print(min_more_30_less_45.get(currect_time_min) + hour.get(currect_time_hour))
    elif int(currect_time_min) > 45:
        print(min_more_45.get(currect_time_min) + hour_more_45.get(currect_time_hour))


if int(right[1]) > 59:
    print('Введено недопустимое количество минут, попробуйте еще раз')
if int(right[0]) > 23:
    print('Введено недопустимое количество часов, попробуй еще раз')

if int(right[1]) == 00 :
        print(min_eq_00.get(right[0]))
if int(right[1]) < 30 :
    if int(right[1]) >= 1:
        print(min_under_30.get(right[1]) + hour.get(right[0]))
elif int(right[1]) == 30 :
    print(min_equally_30.get(right[1]) + hour.get(right[0]))
elif int(right[1]) > 30:
    if int(right[1]) < 45:
        print(min_more_30_less_45.get(right[1]) + hour.get(right[0]))
    elif int(right[1]) > 45:
        print(min_more_45.get(right[1]) + hour_more_45.get(right[0]))