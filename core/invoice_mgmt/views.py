from .serializers import BillItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Bill, BillItems
from . utils import generate_bill_code
from rest_framework import generics



class BillAPI(APIView):
    def get(self, request):
        bill_details = Bill.objects.prefetch_related('bills')
        # print(bills)         #.all()
        if not bill_details:            
            return Response("Sorry...! You have'nt generated any bills")
        else:
            serializer = BillItemSerializer(bill_details, many=True)
            data = { "Bill-Details": [
                
                        {   "Bill_code": bill.bill_code,
                             "Total": bill.total,
                        } 
                             for bill in bill_details
                        ],

                     "Bill-Items":
                    [
                        {"Item-Name": item.item_name,
                         "Quantity": item.quantity,
                         "Rate": item.rate,
                         "Amount": item.amount,
                         }
                        for bill in bill_details 
                        for item in bill.bills.all()
                    ]
                    }
            

            return Response(data=data, status=status.HTTP_200_OK)
            
class BillAPIView(APIView):
    def post(self, request):
        serializer = BillItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            bill = generate_bill_code()            
            total = 0
            for item in serializer.validated_data:
                bill_items = BillItems()
                bill_items.bill_code = bill
                bill_items.item_name = item['item_name']
                bill_items.quantity = item['quantity']
                bill_items.rate = item['rate']                                
                amount = bill_items.quantity * bill_items.rate
                bill_items.amount = amount
                total += amount 
                bill_items.save()
                # print('Total-Amount=', total)
            bill.total = total
            bill.save()
            # print(bill.total)
            data = Bill.objects.prefetch_related('bills').get(bill_code=bill.bill_code)
            bill_data = {
                            "bill_code": data.bill_code,
                            "total": data.total,
                            "bill_items": [
                                    
                                {
                                    "item_name": item.item_name,
                                    "rate": item.rate,
                                    "quantity": item.quantity,
                                    "amount": item.amount, 

                                }
                                for item in data.bills.all()
                            ]
                        }         
            return Response({"Bill-Details":bill_data},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
