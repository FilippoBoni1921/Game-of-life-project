import numpy as np

def block():
    block = [ [0, 0, 0, 0],
              [0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 0],
            ]
    return np.array(block)

def tube():
    tube =  [ [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0],
            ]
    return np.array(tube)

def boat():
    boat =  [ 
              [0, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0],
            ]
    return np.array(boat)

def ship():
    ship =  [ [0, 0, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 1, 0, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0],
            ]
    return np.array(ship)

def bee_hive():
    bee_hive = [ [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0],
               ]
    return np.array(bee_hive)

def loaf():
    loaf = [ [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 1, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
           ]
    return np.array(loaf)

def pond():
    pond = [ [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 1, 0, 0, 1, 0],
             [0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
           ]
    return np.array(pond)

def snake():
    snake = [ [0, 0, 0, 0, 0, 0],
              [0, 1, 0, 1, 1, 0],
              [0, 1, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0],
            ]
    return np.array(snake)

def eater1():
    eater1 = [ [0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0],
               [0, 1, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 0],
               ]
    return np.array(eater1)

def eater2():
    eater2 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 1, 1, 0],
               [0, 0, 1, 1, 1, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 1, 1, 0],
               [0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
             ]
    return np.array(eater2)

def blinker():
    blinker = [  [0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0],
               ]
    return np.array(blinker)

def toad(): #oscillator
    toad = [ [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0],
             [0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
           ]
    return np.array(toad)

def clock(): #oscillator but still life
    clock = [ [0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0],
           ]
    return np.array(clock)

def beacon():
    beacon = [ [0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 0],
           ]
    return np.array(beacon)

def pulsar(): #oscillator
    pulsar = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           ]
    return np.array(pulsar)

def penta_decathlon():
    penta = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           ]
    return np.array(penta)

def bi_penta_decathlon():
    bi_penta = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               ]
    return np.array(bi_penta)

def box_plot():
    box_plot = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             ]
    return np.array(box_plot)

def blocker():
    blocker = [ [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              ]
    
def octagon(): 
    oct = [  [0, 0, 0, 1, 1, 0, 0 ,0], 
             [0, 0, 1, 0, 0, 1, 0 ,0], 
             [0, 1, 0, 0, 0, 0, 1 ,0], 
             [1, 0, 0, 0, 0, 0, 0 ,1], 
             [1, 0, 0, 0, 0, 0, 0 ,1], 
             [0, 1, 0, 0, 0, 0, 1 ,0], 
             [0, 0, 1, 0, 0, 1, 0 ,0], 
             [0, 0, 0, 1, 1, 0, 0 ,0], 
          ] 
    return np.array(oct) 
 
def mazing(): 
    maz = [  [0, 0, 0, 0, 0, 0, 0 ,0, 0], 
             [0, 0, 0, 0, 1, 1, 0 ,0, 0], 
             [0, 0, 1, 0, 1, 0, 0 ,0, 0], 
             [0, 1, 0, 0, 0, 0, 0 ,1, 0], 
             [0, 0, 1, 0, 0, 0, 1 ,1, 0], 
             [0, 0, 0, 0, 0, 0, 0 ,0, 0], 
             [0, 0, 0, 0, 1, 0, 1 ,0, 0], 
             [0, 0, 0, 0, 0, 1, 0 ,0, 0], 
             [0, 0, 0, 0, 0, 0, 0 ,0, 0], 
              
          ] 
    return np.array(maz)

def glider():
    glider = [ [0, 1, 0],
               [0, 0, 1],
               [1, 1, 1],
             ]
    return np.array(glider)

def lw_spaceship():
    lw_spaceship = [ [1, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 1],
                     [0, 1, 1, 1, 1],
                   ]
    return np.array(lw_spaceship)

def mw_spaceship():
    mw_spaceship = [ [0, 0, 1, 0, 0, 0],
                     [1, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 1],
                     [0, 1, 1, 1, 1, 1],
                   ]
    return np.array(mw_spaceship)

def hw_spaceship():
    hw_spaceship = [ [0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 1],
                     [0, 1, 1, 1, 1, 1, 1],
                   ]
    return np.array(hw_spaceship)

def copperhead():
    copperhead =   [ [0, 1, 1, 0, 0, 1, 1, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 1],
                     [0, 1, 1, 0, 0, 1, 1, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                   ]
    return np.array(copperhead)

def weekender():
    weekender =    [ [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   ]
    return np.array(weekender)

def spider():
    spider    = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
                   [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                   [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                ] 
    return np.array(spider)

def queen_bee_shuttle():
    qbs = [    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
           ]
    return np.array(qbs)

def worker_bee():
    wb = [  [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
          [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
          [0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0],
          [0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0],
          [0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0],
          [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
          [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
         ]
    return np.array(wb)

def glider_gun():
    gun    = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             ] 
    return np.array(gun)

def acorn(): #explode
    acorn = [ [0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0],
              [1, 1, 0, 0, 1, 1, 1],
            ]
    return np.array(acorn)

def blinker_puffer1():
    blinker_puffer1 = [  [0, 0, 0, 1, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 1, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 1, 0, 0, 0],
                         [1, 1, 1, 1, 1, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 0, 0, 0, 0, 0, 0],
                         [1, 1, 0, 1, 1, 1, 0, 0, 0],
                         [0, 1, 1, 1, 1, 0, 0, 0, 1],
                         [0, 0, 1, 1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 1, 1, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0, 0, 1],
                         [0, 0, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 1, 0, 0, 0, 0, 0, 1],
                         [0, 0, 1, 1, 1, 1, 1, 1, 0],
                      ]
    return np.array(blinker_puffer1)

def pufferfish():
    pufferfish = [ [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                   [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                   [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
                   [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 ]
    return np.array(pufferfish)

def B_heptomino():
    B = [   [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
    ]
    return np.array(B)

def Pi_heptomino():
    Pi = [  [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
    ]
    return np.array(Pi)

def random_config(b, h):
    random_config = np.random.randint(2, size = (h, b))
    return random_config