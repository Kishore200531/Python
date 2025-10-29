#Simple Interest = (P*T*R)/100
#P = Principal amount, R = Rate of interest, T = Time duration

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))
si = (principal*rate*time)/100
print("Simple Interest:", si)


#Compound Interest = A - P
#Amount(A) = P(1 + R/100)^T

amount = principal*(1 + rate/100)**time #amount = principal*pow((1 + rate/100),time)
print("Amount of interest:", round(amount,2))
ci = amount - principal
print("Compound Interest:", round(ci,2))
