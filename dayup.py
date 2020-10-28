# up = 1
# upfact = 0.01
# aup = 1.01**365

# for i in range(365):
#     if i%7 in [0,6]:
#         up*=0.99
#     else:
#         up*=(1+upfact)

# while up < aup:
#     print("upfact={},up={},aup={}.".format(upfact,up,aup))
#     up=1
#     upfact += 0.0001
#     for i in range(365):
#         if i%7 in [0,6]:
#             up*=0.99
#         else:
#             up*=(1+upfact)

# print("工作日的努力参数是: {:.3f},up={}".format(upfact,up))
def dayup(dayfact):
    dayUp=1
    for i in range(365):
        if i % 7 in [0,6]:
            dayUp *= 0.99
        else:
            dayUp *= 1 + dayfact
    return dayUp
dayFact = 0.01
while dayup(dayFact) < 1.01**365:
    dayFact += 0.001
print("工作日的努力参数是: {:.3f}".format(dayFact))
# def dayUP(df):
#     dayup = 1
#     for i in range(365):
#         if i % 7 in [6,0]:
#             dayup = dayup*(1 - 0.01)
#         else:
#             dayup = dayup*(1 + df)
#     return dayup
# dayfactor = 0.01
# while dayUP(dayfactor) < 37.78:
#     dayfactor += 0.001
# print("工作日的努力参数是: {:.3f}".format(dayfactor))