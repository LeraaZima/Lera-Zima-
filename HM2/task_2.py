# Выдвигаем гипотезу: лучшие рекомендации получатся, если просто отсортировать имена по алфавиту и
# познакомить людей с одинаковыми индексами после сортировки. 
# Но вы не будете никого знакомить, если кто-то может остаться без пары.

boys = ["Александр","Иннокентий","Добрыня","Алиджон"]
girls = ["Прокофья","Зинаида","Петруша","Лера","Любовь"] 
g = sorted(girls)
b = sorted(boys)
if len(boys) != len(girls):
    print("Извините,вы идете домой одни")
else:
    for idx in range(len(b)):
        print(b[idx],g[idx])
