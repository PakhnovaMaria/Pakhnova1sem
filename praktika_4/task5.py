import robot
# создаем робота
r = robot.rmap()
#загружаем карту соотвествующей задачи
r.lm('task5')

def check():
    r. pt()
    r. rt (1)
    r. dn (1)
    r. pt()
    r. up (1)
    r. rt (1) 
    r. pt ()
    
def mab():
    r. pt()
    r. lt (1)
    r. dn (1)
    r. pt()
    r. up (1)
    r. lt (1) 
    r. pt ()

    

def task():
    r.sleep=0.1
    for k in range (0, 3):
        check()
        r. rt (2)
    check()
    r. dn(3)
    for p in range (0, 3):
        mab()
        r. lt (2)
    mab()
    r. dn(3)
    for m in range (0, 3):
        check()
        r. rt (2)
    check()
        
r.start(task)
