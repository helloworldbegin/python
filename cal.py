def cmul(*st):
    st=str(st)
    st=st.replace(",","*")
    st=st.strip("()")
    return eval(str(st).replace(",","*"))

print(eval("cmul({})".format(input())))