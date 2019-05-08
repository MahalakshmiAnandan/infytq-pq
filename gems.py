def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
   bill_amount=0
   for i in range(len(reqd_gems)):
        for j in range(len(gems_list)):
            if(reqd_gems[i]==gems_list[j]):
               bill_amount+=(price_list[j]*reqd_quantity[i])
               if(bill_amount>30000):
                    bill_amount=bill_amount-(5/100)*30000
                else:
                    bill_amount=-1
    
return bill_amount
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]
bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)

print(bill_amount)
