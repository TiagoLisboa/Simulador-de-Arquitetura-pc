def add (comp):
    return comp["pilha"].append( comp["pilha"].pop() + comp["pilha"].pop() )

def sub (comp):
    return

def mul (comp):
    return

def div (comp):
    return

def push (comp, data):
	data = getFromMem (comp, data[1:]) if (data.startswith("$")) else data
	comp["pilha"].append(int(data))
	return data


def pop (comp,  memslot):
	comp["mbr"] = comp["pilha"].pop()
	comp["mar"] = memslot[1:]
	comp["datamem"][int(comp["mar"])] = comp["mbr"]
	return comp["mbr"]

decoder = {
    "ADD": add,
    "SUB": sub,
    "MUL": mul,
    "DIV": div,
    "PUSH": push,
    "POP": pop
    }

def getFromMem (comp, idx):
	comp["mar"] = idx
	comp["mbr"] = comp["datamem"][int(comp["mar"])]
	comp["mbr"] = comp["mbr"] if comp["mbr"] else 0
	return comp["mbr"]

def decode (comp):
	args = comp["ir"].split()	
	return decoder[args[0]](comp, *args[1:])
