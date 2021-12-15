input_dice_count = input("Ievadi metamo kaulinu skaitu (2-5): ")

try:
 dice_count = int(input_dice_count)
except ValueError:
 print("Ievadi skaitli')
 exit()

+ if 2 > dice_count or dice_count > 5:
 print(*Ievadi skaitli no 2 lidz 5")
 exit()


# Uzmestie kaulini ir pâra skaitli
print("Varbütiba, ka uzmestie kaulini ir para skaitli: " + str(1 ** dice_count) + "/" + str(2 ** dice_count))

# Uzmestie kaulini ir vienadi skaitli
print("Varbütiba, ka uzmestie kaulini ir vienadi skaitli: " + str(1 ** dice_count) + "/" + str(6 ** dice_count))


# Uzmestie kaulini ir nepara skaitli
print("Varbütiba, ka uzmestie kaulini ir nepara skaitli: " + str(1 > * dice_count) + "/" + str(2 ** dice_count))


# No uzmestajiem kauliniem neviens skaitlis neatkärtojas
print("Varbütiba, ka no uzmestajiem kauliniem neviens skaitlis neatkartojas:" + str(5 ** dice_count) + " / * + str(6 * dicecount))


# No uzmestajiem kauliniem divi ir vienadi skaitli

x - 1 * 2

if dice_count - 2 > 0:
 × += 6 ** (dice_count - 2)

+ print("Varbütiba, ka no uzmestajiem kauliniem divi ir vienadi skait]i: " + str(x) * ° / " + str(6 ** dice_ count))
