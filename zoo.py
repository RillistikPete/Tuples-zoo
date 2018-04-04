
zoo = tuple()
zoo = ('Southern Monkey', 'Tiger', 'Crane', 'Leopard', 'Dragon')
print(zoo.index('Crane'))

for value in zoo:
    if value is 'Tiger':
        print(value)

# This assigns variables to each value in my tuple:
(NgMonkey, OoChwan, NgCrane, NgLeopard, NgDragon) = zoo
print(NgMonkey) #prints "Southern Monkey"


#Convert tuple into list:
zooList = list(zoo)
zooList.extend(['Praying Mantis', 'Bear', 'Snake'])

#Convert list back into tuple:
newZoo = tuple(zooList)
print(newZoo)

