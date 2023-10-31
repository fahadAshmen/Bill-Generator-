from . models import Bill

def generate_bill_code(): 
    last_bill = Bill.objects.order_by('-id').first()
    if last_bill:
        bill_code = int(last_bill.bill_code.split('-')[1])
        # print('===>',bill_code)
        code = f'Bill-{str(bill_code + 1).zfill(4)}'
        # print('code==',code)
        bill = Bill.objects.create(bill_code=code)
    else:
            bill = Bill.objects.create(bill_code='Bill-0001')    
    return bill