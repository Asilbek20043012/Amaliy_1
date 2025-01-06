L1 = input("(share/steal): ").split()
L2 = input("(share/steal): ").split()

tanga1, tanga2 = 3, 3  
foyda1, foyda2 = 0, 0  

for i in range(len(L1)):
    action1 = L1[i]
    action2 = L2[i]
    if action1 == "share" and action2 == "share":
        foyda1 += 2
        foyda2 += 2
    elif action1 == "share" and action2 == "steal":
        foyda1 += -1
        foyda2 += 3
    elif action1 == "steal" and action2 == "share":
        foyda1 += 3
        foyda2 += -1
    elif action1 == "steal" and action2 == "steal":
        foyda1 += 0
        foyda2 += 0

natija1 = tanga1 + foyda1
natija2 = tanga2 + foyda2

print(f"Natija: [{natija1}, {natija2}]")