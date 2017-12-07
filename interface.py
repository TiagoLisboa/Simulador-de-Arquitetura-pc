from curses import wrapper
import curses, curses.panel
from pc import comp

sc = {
        "dmem": {
            "window": 0,
            "panel": 0
            },
        "pilha": {
            "window": 0,
            "panel": 0
            },
        "insts": {
            "window": 0,
            "panel": 0
            },
        "monitor": {
            "window": 0,
            "panel": 0
            }
        }

# INSTRUÇÔES

def populate_insts ():
    lh,lw = sc["insts"]["window"].getmaxyx()
    for line, instruct in enumerate(comp["instmem"]):
        if (instruct == None):
            break
        else:
            print (line)
            if (line+2 < lh):
                sc["insts"]["window"].addstr (line+1, 1, "{} - {} {}".format(line, instruct,
                    "<" if line == comp["pc"] else ""
                    ))

def populate_mem ():
    lh,lw = sc["dmem"]["window"].getmaxyx()
    l = 1
    sc["dmem"]["window"].move (l,1)
    try:
        for i in range (0, 1000):
            if comp["datamem"][i] != None:
                sc["dmem"]["window"].addstr ('■ ')
            else:
                sc["dmem"]["window"].addstr ('□ ')
    
            if (i+1) % (( lw-int(lw/2)-1 )) == 0:
                l+=1
                sc["dmem"]["window"].move (l,1)
    except Exception as e:
        print (e)

def populate_pilha ():
    lh,lw = sc["pilha"]["window"].getmaxyx()
    l = 1
    sc["pilha"]["window"].move (l,1)
    try:
        for i in range (0, 100):
            if i <  len(comp["pilha"]):
                sc["pilha"]["window"].addstr ('■ ')
            else:
                sc["pilha"]["window"].addstr ('□ ')

            if (i+1) % (( lw-int(lw/2)-1 )) == 0:
                l+=1
                sc["pilha"]["window"].move (l,1)
    except Exception as e:
        print (e)


def setup (w, h):
    dmw, dmp = make_panel (int(h*.8),int(w*.6), 0,0, "Memoria de dados")
    rw, rp = make_panel (h-int(h*.8),int(w*.6), int(h*.8),0, "Pilha")
    iw, ip = make_panel (h - int(h*.4),int(w*.4), int(h*.4), int(w*.6), "Instruções")
    mw, mp = make_panel (int(h*.4),int(w*.4), 0,int(w*.6), "Monitor")
    sc["dmem"]["window"]    = dmw
    sc["dmem"]["panel"]     = dmp
    sc["pilha"]["window"]   = rw
    sc["pilha"]["panel"]    = rp
    sc["monitor"]["window"] = mw
    sc["monitor"]["panel"]  = mp
    sc["insts"]["window"]   = iw
    sc["insts"]["panel"]    = ip

def make_panel (h,l, y,x, s):
    win = curses.newwin (h,l, y,x)
    win.erase ()
    win.box ()
    win.addstr (0, 1, s)

    panel = curses.panel.new_panel (win)
    return win, panel


def main (stdscr):
    h,w = stdscr.getmaxyx()
    stdscr.clear ()

    pad = curses.newpad (100, 100)
    
    setup (w, h) 

    populate_insts ()
    populate_mem ()
    populate_pilha ()
    
    curses.panel.update_panels()

    stdscr.refresh ()
    stdscr.getkey()

wrapper (main)
