summa=int(input("минимальная сумма инвестиций -"))
maikl=int(input("сколько долларов у майкла -"))
ivan=int(input("сколько долларов у ивана -"))
if (maikl>=summa) and (ivan>=summa):
    print(2)
if (maikl>=summa) and (ivan<=summa):
    print("Mike")
if (maikl<=summa) and (ivan>=summa):
    print("Ivan")
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)>=summa):
    print(1)
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)<=summa):
    print(0)