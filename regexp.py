q='"'
q1="'"
n='\n'
s='\\'
variable_1 = "def f(a,s1,s2,s3,s4):"
variable_2 = " print a+'1='+q+s1+q+n+a+'2='+q+s2+q"
variable_3 = " print a+'3='+q+s3+q+n+a+'4='+q+s4+q"
variable_4 = " print s1+n+s2+n+s3+n+s4"
def f(a,s1,s2,s3,s4):
    print("a+'1='+q+s1+q+n+a+'2='+q+s2+q")
    print("a+'3='+q+s3+q+n+a+'4='+q+s4+q")
    print("s1+n+s2+n+s3+n+s4")
p1="print 'q='+q1+q+q1+n+'q1='+q+q1+q"
p2="print 'n='+q1+s+'n'+q1+n+'s='+q1+s+s+q1"
p3="f('r',r1,r2,r3,r4)"
p4="f('p',p1,p2,p3,p4)"
print 'q='+q1+q+q1+n+'q1='+q+q1+q
print 'n='+q1+s+'n'+q1+n+'s='+q1+s+s+q1
f('r',r1,r2,r3,r4)
f('p',p1,p2,p3,p4)