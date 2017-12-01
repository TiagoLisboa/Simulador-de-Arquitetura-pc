from decoder import decode

MEMSIZE = 125000

comp = {
        "instmem": ["PUSH 1", "PUSH 2", "ADD", "POP"],
        "datamem": [],
        "pilha": [],
        "ir": 0,
        "pc": 0,
        "mbr": 0,
        "mar": 0
        }

for i in range (0, 124999):
    if i >= len(comp["instmem"]):
        comp["instmem"].append(None)
    if i >= len(comp["datamem"]):
        comp["datamem"].append(None)

for comp["pc"] in range(0, 124999):
    comp["ir"] = comp["instmem"][comp["pc"]]
    if comp["ir"]:
        print (decode (comp))
