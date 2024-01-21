leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

m_luoti = 13.3
m_naula = 32*m_luoti
m_leiviska = 20*m_naula
grammat0 = m_luoti*luodit + m_naula*naulat + m_leiviska*leiviskat

if grammat0 >= 1000:
    kilot = int(grammat0/1000)
    grammat1 = float(grammat0 - 1000*kilot)
else:
    kilot = 0
    grammat1 = grammat0

print(f"Massa nykymittojen mukaan:\n{kilot} kilogrammaa ja {grammat1:.2f} grammaa.")