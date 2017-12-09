from decoder import decode

MEMSIZE = 1000
QTDREGS = 100

comp = {
        "instmem": ["PUSH $0", "PUSH $1", "ADD", "POP $2"],
        "datamem": [1, 2],
        "pilha": [],
        "ir": 0,
        "pc": 0,
        "mbr": 0,
        "mar": 0
        }

for i in range (0, 999):
    if i >= len(comp["instmem"]):
        comp["instmem"].append(None)
    if i >= len(comp["datamem"]):
        comp["datamem"].append(None)


def exec_next_inst ():
    comp["ir"] = comp["instmem"][comp["pc"]]
    
    if comp["pc"] < 999:
        comp["pc"] += 1
    else:
        comp["pc"]=0

    if comp["ir"]:
        decode (comp)


