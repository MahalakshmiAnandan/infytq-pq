input Number
Sum=0
Temp=Number
while(Number!=0) do
Remainder=Number%10
Sum=Sum+Remainder*Remainder*Remainder
Number=Number/10
end-while
if(Temp==Sum) then
display "This is an Armstrong Number"
else
display "This is not an Armstrong Number"
end-if



