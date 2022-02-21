hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
ot = float (h) - 40
print(ot)
if h > 40:
    pay = 40 * (float(rate) + (float(ot)*(float(rate)*1.5))
else:
    pay = float(h) * float(rate)
print(pay)
#h = float(hrs)
