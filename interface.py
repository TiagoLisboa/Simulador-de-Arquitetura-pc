from curses import wrapper
import curses, curses.panel
from pc import comp
from pc import exec_next_inst 

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
            "panel": 0,
            "selected": 0,
            "start_show": 0,
            "height": 0,
            "width": 0
            },
        "monitor": {
            "window": 0,
            "panel": 0
            }
        }

# INSTRUÇÔES

def update_insts ():
    lh = sc["insts"]["height"]
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    result = [a for i, a in enumerate(comp["instmem"]) if i >= sc["insts"]["start_show"]]
    for line, instruct in enumerate(result):
        #if (instruct == None):
        #    break
        #else:
            if (line+2 < lh):
                sc["insts"]["window"].addstr (
                        line+1, 1,
                        "{} - {} {}".format(line+sc["insts"]["start_show"], instruct if instruct != None else "","< NEXT" if line == comp["pc"] - sc["insts"]["start_show"] else ""),
                        curses.color_pair (1) if line == sc["insts"]["selected"] - sc["insts"]["start_show"] else curses.color_pair (2)
                        )

# MEMORIA

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

# PILHA

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
    lh,lw = sc["insts"]["window"].getmaxyx() 
    sc["insts"]["height"]   = lh
    sc["insts"]["width"]    = lw

def make_panel (h,l, y,x, s):
    win = curses.newwin (h,l, y,x)
    win.erase ()
    win.box ()
    win.addstr (0, 1, s)

    panel = curses.panel.new_panel (win)
    return win, panel

def update (stdscr):
    h,w = stdscr.getmaxyx()
    stdscr.clear ()
    
    setup (w, h) 

    update_insts ()
    populate_mem ()
    populate_pilha ()
    
    curses.panel.update_panels()

    stdscr.refresh ()


def main (stdscr): 
    update (stdscr)

    c = stdscr.getch ()

    if c == 27:
        return 0
    elif c == curses.KEY_DOWN:
        sc["insts"]["selected"] += 1
        if sc["insts"]["selected"] >= sc["insts"]["height"]-2:
            sc["insts"]["start_show"] += 1
    elif c == curses.KEY_UP:
        sc["insts"]["selected"] -= 1
        if sc["insts"]["selected"] < 0:
            sc["insts"]["selected"] = 0
        if sc["insts"]["selected"] - sc["insts"]["start_show"] < 0:
            sc["insts"]["start_show"] -= 1
            if sc["insts"]["start_show"] < 0:
                sc["insts"]["start_show"] = 0
    elif c == curses.KEY_HOME:
        sc["insts"]["selected"] = 0
        sc["insts"]["start_show"] = 0
    elif c == curses.KEY_ENTER or c == 10:
        exec_next_inst ()
    elif c == 263:
        try:
            comp["instmem"][sc["insts"]["selected"]] = comp["instmem"][sc["insts"]["selected"]][:-1]
        except TypeError:
            comp["instmem"][sc["insts"]["selected"]] = ""

    else:
        try:
            comp["instmem"][sc["insts"]["selected"]] += chr (c)
        except TypeError:
            comp["instmem"][sc["insts"]["selected"]] = chr (c)



    main (stdscr)

    
wrapper (main)
