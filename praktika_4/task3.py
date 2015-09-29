import robot
# создаем робота
r = robot.rmap()
#загружаем карту соотвествующей задачи
r.lm('task3')

def check(): 
    r. rt (2)
    r. dn (1)
    r. up (1)
    
def task ():
    r.sleep=0.1
    while r. fr ():
        check ()
        
r. start(task)
    
    
    
