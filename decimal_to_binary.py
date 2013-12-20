num= int(raw_input("Please input a number in the range [0,127]:"))
                   
bit1=num%2
bit2=(num/2)%2
bit3=(num/4)%2
bit4=(num/8)%2
bit5=(num/16)%2
bit6=(num/32)%2
bit7=(num/64)%2
bit8=(num/128)%2
if num>127 or num<1:
    print str (num )+ " is out of the range!"

elif (bit1+bit2+bit3+bit4+bit5+bit6+bit7+bit8)%2==0:
    print str(num )+ ("(10)") + "=" + str(bit7) + str(bit6)+str(bit5)+str(bit4)+str(bit3)+str(bit2)+str(bit1)+ str( "(2)")+ " has even parity"


else:
    print str(num )+ ("(10)") + "=" + str(bit7) + str(bit6)+str(bit5)+str(bit4)+str(bit3)+str(bit2)+str(bit1)+ str( "(2)")+ " has odd parity"

