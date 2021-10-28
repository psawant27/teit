import math
 
print(&quot;RSA ENCRYPTOR/DECRYPTOR&quot;)
print(&quot;*****************************************************&quot;)
 
#Input Prime Numbers
print(&quot;PLEASE ENTER THE &#39;p&#39; AND &#39;q&#39; VALUES BELOW:&quot;)
p = int(input(&quot;Enter a prime number for p: &quot;))
q = int(input(&quot;Enter a prime number for q: &quot;))
print(&quot;*****************************************************&quot;)
 
#Check if Input&#39;s are Prime
&#39;&#39;&#39;THIS FUNCTION AND THE CODE IMMEDIATELY BELOW THE FUNCTION CHECKS
WHETHER THE INPUTS ARE PRIME OR NOT.&#39;&#39;&#39;
def prime_check(a):
    if(a==2):
        return True
    elif((a&lt;2) or ((a%2)==0)):
        return False
    elif(a&gt;2):
        for i in range(2,a):
            if not(a%i):
                return false
    return True
 
check_p = prime_check(p)
check_q = prime_check(q)
while(((check_p==False)or(check_q==False))):
    p = int(input(&quot;Enter a prime number for p: &quot;))
    q = int(input(&quot;Enter a prime number for q: &quot;))
    check_p = prime_check(p)
    check_q = prime_check(q)
 
#RSA Modulus
&#39;&#39;&#39;CALCULATION OF RSA MODULUS &#39;n&#39;.&#39;&#39;&#39;
n = p * q
print(&quot;RSA Modulus(n) is:&quot;,n)
 
#Eulers Toitent
&#39;&#39;&#39;CALCULATION OF EULERS TOITENT &#39;r&#39;.&#39;&#39;&#39;
r= (p-1)*(q-1)
print(&quot;Eulers Toitent(r) is:&quot;,r)
print(&quot;*****************************************************&quot;)
 
#GCD

&#39;&#39;&#39;CALCULATION OF GCD FOR &#39;e&#39; CALCULATION.&#39;&#39;&#39;
def egcd(e,r):
    while(r!=0):
        e,r=r,e%r
    return e
 
#Euclid&#39;s Algorithm
def eugcd(e,r):
    for i in range(1,r):
        while(e!=0):
            a,b=r//e,r%e
            if(b!=0):
                print(&quot;%d = %d*(%d) + %d&quot;%(r,a,e,b))
            r=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print(&quot;%d = %d*(%d) + (%d)*(%d)&quot;%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s&lt;0):
            print(&quot;s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d.&quot;%(s,s,s%r))
        elif(s&gt;0):
            print(&quot;s=%d.&quot;%(s))
        return s%r
 
#e Value Calculation
&#39;&#39;&#39;FINDS THE HIGHEST POSSIBLE VALUE OF &#39;e&#39; BETWEEN 1 and 1000 THAT MAKES (e,r)
COPRIME.&#39;&#39;&#39;
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print(&quot;The value of e is:&quot;,e)
print(&quot;*****************************************************&quot;)

 
#d, Private and Public Keys
&#39;&#39;&#39;CALCULATION OF &#39;d&#39;, PRIVATE KEY, AND PUBLIC KEY.&#39;&#39;&#39;
print(&quot;EUCLID&#39;S ALGORITHM:&quot;)
eugcd(e,r)
print(&quot;END OF THE STEPS USED TO ACHIEVE EUCLID&#39;S ALGORITHM.&quot;)
print(&quot;*****************************************************&quot;)
print(&quot;EUCLID&#39;S EXTENDED ALGORITHM:&quot;)
d = mult_inv(e,r)
print(&quot;END OF THE STEPS USED TO ACHIEVE THE VALUE OF &#39;d&#39;.&quot;)
print(&quot;The value of d is:&quot;,d)
print(&quot;*****************************************************&quot;)
public = (e,n)
private = (d,n)
print(&quot;Private Key is:&quot;,private)
print(&quot;Public Key is:&quot;,public)
print(&quot;*****************************************************&quot;)
 
#Encryption
&#39;&#39;&#39;ENCRYPTION ALGORITHM.&#39;&#39;&#39;
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):              
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
 
#Decryption
&#39;&#39;&#39;DECRYPTION ALGORITHM&#39;&#39;&#39;
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(&#39;,&#39;)
    x=&#39;&#39;
    m=0

    for i in txt:
        if(i==&#39;400&#39;):
            x+=&#39; &#39;
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
message = input(&quot;What would you like encrypted or decrypted?(Separate numbers with &#39;,&#39; for decryption):&quot;)
print(&quot;Your message is:&quot;,message)
 
#Choose Encrypt or Decrypt and Print
choose = input(&quot;Type &#39;1&#39; for encryption and &#39;2&#39; for decrytion.&quot;)
if(choose==&#39;1&#39;):
    enc_msg=encrypt(public,message)
    print(&quot;Your encrypted message is:&quot;,enc_msg)
    print(&quot;Thank you for using the RSA Encryptor. Goodbye!&quot;)
elif(choose==&#39;2&#39;):
    print(&quot;Your decrypted message is:&quot;,decrypt(private,message))
    print(&quot;Thank you for using the RSA Encryptor. Goodbye!&quot;)
else:
    print(&quot;You entered the wrong option.&quot;)
    print(&quot;Thank you for using the RSA Encryptor. Goodbye!&quot;)
OutPut:
PLEASE ENTER THE &#39;p&#39; AND &#39;q&#39; VALUES BELOW:
Enter a prime number for p: 3
Enter a prime number for q: 5
*****************************************************
RSA Modulus(n) is: 15
Eulers Toitent(r) is: 8
*****************************************************
The value of e is: 999
*****************************************************
EUCLID&#39;S ALGORITHM:

8 = 0*(999) + 8
999 = 124*(8) + 7
8 = 1*(7) + 1
END OF THE STEPS USED TO ACHIEVE EUCLID&#39;S ALGORITHM.
*****************************************************
EUCLID&#39;S EXTENDED ALGORITHM:
1 = 8*(1) + (-1)*(7)
1 = 999*(-1) + (125)*(8)
s=-1. Since -1 is less than 0, s = s(modr), i.e., s=7.
END OF THE STEPS USED TO ACHIEVE THE VALUE OF &#39;d&#39;.
The value of d is: 7
*****************************************************
Private Key is: (7, 15)
Public Key is: (999, 15)
*****************************************************
What would you like encrypted or decrypted?(Separate numbers with &#39;,&#39; for decryption):HELLO
Your message is: HELLO
Type &#39;1&#39; for encryption and &#39;2&#39; for decrytion.1
Your encrypted message is: [13, 4, 11, 11, 14]
Thank you for using the RSA Encryptor. Goodbye!
&gt;&gt;&gt;
 RESTART: C:\Users\agott\Desktop\Penn State\PSU Summer 2018\CMPSC360\Project\Part 2\RSA
Algorithm 3.0.py
RSA ENCRYPTOR/DECRYPTOR
*****************************************************
PLEASE ENTER THE &#39;p&#39; AND &#39;q&#39; VALUES BELOW:
Enter a prime number for p: 3
Enter a prime number for q: 5

*****************************************************
RSA Modulus(n) is: 15
Eulers Toitent(r) is: 8
*****************************************************
The value of e is: 999
*****************************************************
EUCLID&#39;S ALGORITHM:
8 = 0*(999) + 8
999 = 124*(8) + 7
8 = 1*(7) + 1
END OF THE STEPS USED TO ACHIEVE EUCLID&#39;S ALGORITHM.
*****************************************************
EUCLID&#39;S EXTENDED ALGORITHM:
1 = 8*(1) + (-1)*(7)
1 = 999*(-1) + (125)*(8)
s=-1. Since -1 is less than 0, s = s(modr), i.e., s=7.
END OF THE STEPS USED TO ACHIEVE THE VALUE OF &#39;d&#39;.
The value of d is: 7
*****************************************************
Private Key is: (7, 15)
Public Key is: (999, 15)
*****************************************************
What would you like encrypted or decrypted?(Separate numbers with &#39;,&#39; for decryption):13,4,11,11,14
Your message is: 13,4,11,11,14
Type &#39;1&#39; for encryption and &#39;2&#39; for decrytion.2
Your decrypted message is: HELLO
Thank you for using the RSA Encryptor. Goodbye!
