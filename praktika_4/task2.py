import robot
# создаем робота
r = robot.rmap()
#загружаем карту соотвествующей задачи
r.lm('task2')

def flower():
    r. pt()
    r. rt(1)
    r. up(1)
    r. pt()
    r. dn(2)
    r. pt()    
    r. up(1)
    r. rt(1)
    r. pt()
    r. rt(1)

def test():    
    r. up(1)
    for i in range(5):
        flower()
        
r.start(test)
