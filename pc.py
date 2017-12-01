from decoder import decode

comp = {
        "instmem": ["PUSH 1", "PUSH 2", "ADD", "POP"],
        "datamem": [],
        "pilha": [],
        "ir": 0,
        "pc": 0,
        "mbr": 0,
        "mar": 0
        }

for i, j in enumerate(comp["instmem"]):
    print (decode (comp, j))
