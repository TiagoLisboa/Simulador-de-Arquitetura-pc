def add (comp):
    a = comp["pilha"].pop()
    b = comp["pilha"].pop()
    res = a + b
    comp["log"].append ( "({}) pilha[TOS] ↢ ({}) pilha[TOS] + ({}) pilha[TOS-1]".format(res, a, b) )
    return comp["pilha"].append(res)

def sub (comp):
    a = comp["pilha"].pop()
    b = comp["pilha"].pop()
    res = a - b
    comp["log"].append ( "({}) pilha[TOS] ↢ ({}) pilha[TOS] - ({}) pilha[TOS-1]".format(res, a, b) )
    return comp["pilha"].append(res)

def mul (comp):
    a = comp["pilha"].pop()
    b = comp["pilha"].pop()
    res = a * b
    comp["log"].append ( "({}) pilha[TOS] ↢ ({}) pilha[TOS] * ({}) pilha[TOS-1]".format(res, a, b) )
    return comp["pilha"].append(res)

def div (comp):
    a = comp["pilha"].pop()
    b = comp["pilha"].pop()
    res = a // b
    comp["log"].append ( "({}) pilha[TOS] ↢ ({}) pilha[TOS] / ({}) pilha[TOS-1]".format(res, a, b) )
    return comp["pilha"].append(res)

def jae (comp, pc):
    a = comp["pilha"][-2:][1]
    b = comp["pilha"][-2:][0]
    res = a >= b
    comp["log"].append ( "(({}) pilha[TOS] >= ({}) pilha[TOS-1]) == {}".format(a, b, res) )
    if res:
        comp["pc"] = int(pc)-1
    return comp["pc"]

def jbe (comp, pc):
    a = comp["pilha"][-2:][1]
    b = comp["pilha"][-2:][0]
    res = a <= b
    comp["log"].append ( "(({}) pilha[TOS] <= ({}) pilha[TOS-1]) == {}".format(a, b, res) )
    if res:
        comp["pc"] = int(pc)-1
    return comp["pc"]

def ja (comp, pc):
    a = comp["pilha"][-2:][1]
    b = comp["pilha"][-2:][0]
    res = a > b
    comp["log"].append ( "(({}) pilha[TOS] > ({}) pilha[TOS-1]) == {}".format(a, b, res) )
    if res:
        comp["pc"] = int(pc)-1
    return comp["pc"]

def jb (comp, pc):
    a = comp["pilha"][-2:][1]
    b = comp["pilha"][-2:][0]
    res = a < b
    comp["log"].append ( "(({}) pilha[TOS] < ({}) pilha[TOS-1]) == {}".format(a, b, res) )
    if res:
        comp["pc"] = int(pc)-1
    return comp["pc"]

def push (comp, memslot):
    if memslot.startswith ("$"):
        comp["mar"] = int(memslot[1:])-1
        comp["log"].append ( "mar            ↢ ${}".format ( int(comp["mar"]) + 1 ) )

        comp["mbr"] = getFromMem (comp, comp["mar"])
        comp["log"].append ( "({}) mbr        ↢ mem[mar] (${})".format ( comp["mbr"], int(comp["mar"]) + 1 ) )
    else:
        comp["mbr"] = memslot
        comp["log"].append ( "mbr            ↢ {}".format (comp["mbr"]) )

    comp["pilha"].append(int(comp["mbr"]))
    comp["log"].append ( "pilha[TOS]     ↢ mbr ({})".format (comp["mbr"]) )
    return comp["mbr"]


def pop (comp,  memslot):
    comp["mbr"] = comp["pilha"].pop()
    comp["log"].append ( "mbr            ↢ pilha[TOS] ({})".format ( comp["mbr"]) )
    comp["mar"] = int(memslot[1:])-1
    comp["log"].append ( "mar            ↢ ${}".format ( int(comp["mar"]) + 1 ) )
    comp["datamem"][int(comp["mar"])] = comp["mbr"]
    comp["log"].append ( "(${}) mem[mar]  ↢ mbr ({})".format (int(comp["mar"]), comp["mbr"]) )
    return comp["mbr"]

decoder = {
    "ADD": add,
    "SUB": sub,
    "MUL": mul,
    "DIV": div,
    "PUSH": push,
    "POP": pop,
    "JAE": jae,
    "JBE": jbe,
    "JA": ja,
    "JB": jb
    }

def getFromMem (comp, idx):
	comp["mar"] = idx
	comp["mbr"] = comp["datamem"][int(comp["mar"])]
	comp["mbr"] = comp["mbr"] if comp["mbr"] else 0
	return comp["mbr"]

def decode (comp):
	args = comp["ir"].split()	
	return decoder[args[0]](comp, *args[1:])
