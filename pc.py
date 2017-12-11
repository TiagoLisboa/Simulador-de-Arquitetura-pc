from decoder import decode

MEMSIZE = 1000
QTDREGS = 100

comp = {
        "instmem": ["PUSH 5", "PUSH 1", "PUSH 1", "ADD", "JB 3", "POP $3"],
        "datamem": [3, 5],
        "pilha": [],
        "ir": 0,
        "pc": 0,
        "mbr": 0,
        "mar": 0,
        "log": []
        }

for i in range (0, 999):
    if i >= len(comp["instmem"]):
        comp["instmem"].append(None)
    if i >= len(comp["datamem"]):
        comp["datamem"].append(None)


def exec_next_inst ():
    comp["ir"] = comp["instmem"][comp["pc"]]
    
    comp["log"].append ( "ir             ↢ instmem[pc (${})] ({})".format ( int(comp["pc"]) + 1 , comp["ir"] ) )

    if comp["pc"] < 999:
        comp["pc"] += 1 
    else:
        comp["pc"]=0

    comp["log"].append ( "pc             ↢ ${}".format ( int(comp["pc"]) + 1 ) )

    if comp["ir"]:
        decode (comp)


