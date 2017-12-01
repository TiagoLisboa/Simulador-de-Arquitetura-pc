def add (comp):
    return comp["pilha"].append( comp["pilha"].pop() + comp["pilha"].pop() )

def sub (comp):
    return

def mul (comp):
    return

def div (comp):
    return

def push (comp, data):
    return comp["pilha"].append(int(data))


def pop (comp,  memslot = -1):
    data = comp["pilha"].pop()
    if memslot >= 0:
        comp["datamem"][memslot] = data
    else:
        comp["datamem"].append(data)
    return data

decoder = {
    "ADD": add,
    "SUB": sub,
    "MUL": mul,
    "DIV": div,
    "PUSH": push,
    "POP": pop
    }

def decode (comp):
    # if type (comp["ir"]) is list:
    args = comp["ir"].split()
    return decoder[args[0]](comp, *args[1:])
