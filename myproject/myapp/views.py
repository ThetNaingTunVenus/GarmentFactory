import datetime

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum,Count,F
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from .forms import *
from .models import *

class Test(View):
    def get(self,request):
        message_data='TheNaing'
        context = {'message_data':message_data}
        return render(request, 'home.html', context)

    def post(self,request):
        t=request.POST.get('test')
        return HttpResponse(t)

#Buyer Section
class BuyerView(View):
    def get(self,request):
        buyer = Buyer.objects.all()
        context ={
            'buyer':buyer
        }
        return render(request, 'buyer_list.html', context)
    def post(self,request):
        buyer_name = request.POST.get('buyer_name')
        vendor_name = request.POST.get('vendor_name')
        address = request.POST.get('address')
        message = None
        if not buyer_name:
            message = 'please enter buyer name'
        elif not address:
            message = 'Please Fill Address'
        if not message:
            b = Buyer(BuyerName=buyer_name,Address=address, Vendor=vendor_name)
            b.save()
            success = 'Buyer Name Created'
            buyer = Buyer.objects.all()
            context = {
                'success':success,
                'message':message,
                'buyer':buyer,
            }
            return render(request, 'buyer_list.html', context)
        else:
            buyer = Buyer.objects.all()
            context = {
                # 'success': success,
                'message': message,
                'buyer': buyer,
            }
            return render(request, 'buyer_list.html', context)

#Style Section
class StyleView(View):
    def get(self,request):
        buyer = Buyer.objects.all()
        style = Style.objects.all()
        context = {
            'style': style,
            'buyer':buyer,
        }
        return render(request, 'style_list.html', context)
    def post(self,request):
        buyer_name = request.POST.get('buyer_name')
        style_code = request.POST.get('style_code')
        item = request.POST.get('item')
        message = None
        if not buyer_name:
            message = 'please enter buyer name'
        elif not style_code:
            message = 'please enter style code'
        elif not item:
            message = 'please fill item'
        if not message:
            v=Buyer.objects.filter(BuyerName=buyer_name)
            vender = v[0].Vendor
            s = Style(Vendor=vender,BuyerName=buyer_name,StyleCode=style_code,ItemName=item)
            s.save()
            success = 'Style Created Successful'
            buyer = Buyer.objects.all()
            style = Style.objects.all()
            context = {
                'message': message,
                'success': success,
                'style': style,
                'buyer': buyer,

            }
            return render(request, 'style_list.html', context)
        else:
            buyer = Buyer.objects.all()
            style = Style.objects.all()
            context = {
                'style': style,
                'buyer': buyer,
                'message':message
            }
            return render(request, 'style_list.html', context)

class ProductionLineView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        context={'line':line}
        return render(request, 'ProductionLineView.html', context)
    def post(self,request):
        line = request.POST.get('line')
        message = None
        if not line:
            message = 'please enter line name'
        if not message:
            l = ProductionLine(ProductionLine=line)
            l.save()
            success = 'Production Line Created'
            line = ProductionLine.objects.all()
            context = {'success':success,'line':line}
            return render(request, 'ProductionLineView.html', context)
        else:
            line = ProductionLine.objects.all()
            context = {'line': line, 'message':message}
            return render(request, 'ProductionLineView.html', context)

class OrderQtyView(TemplateView):
    template_name = 'orderqty_create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #     # supplier id get from request url
        style_id = self.kwargs['id']
        # get style info
        style_data = Style.objects.get(id=style_id)
        context['style_data']=style_data

        return context


class SaveOrderQty(View):
    def get(self,request):
        pass
    def post(self,request):
        buyer = request.POST.get('buyer')
        style_code = request.POST.get('style_code')
        item = request.POST.get('item')
        order_date = request.POST.get('order_date')
        order_qty = request.POST.get('order_qty')
        cmp = request.POST.get('cmp_amount')
        making_charge = request.POST.get('making_charge')
        import_export_charge = request.POST.get('import_export_charge')
        box_charge = request.POST.get('box_charge')
        poly_bag = request.POST.get('poly_bag')
        sewing_thread = request.POST.get('sewing_thread')
        delivery = request.POST.get('deli_date')
        fabricETA = request.POST.get('fabric_eta')
        accETA = request.POST.get('acc_eta')
        vendor = request.POST.get('vendor')
        message = None
        print(box_charge)

        if not order_date:
            message = 'select date'
        elif not order_qty:
            message = 'enter order qty'
        elif not cmp:
            message = 'set cmp'
        # elif not making_charge:
        #     making_charge = 0
        # elif not import_export_charge:
        #     import_export_charge = 0
        # elif not box_charge:
        #     box_charge = 0
        # elif not poly_bag:
        #     poly_bag=0
        # elif not sewing_thread:
        #     sewing_thread=0

        if not message:

            cmp_amount = float(cmp)*float(order_qty)
            cmp_condition = int(making_charge) + int(import_export_charge) + int(poly_bag) + int(sewing_thread)+int(box_charge)
            serial_number = buyer + style_code + order_date


            saorder = OrderQty(
                buyer=buyer,
                vendor=vendor,
                style=style_code,
                item=item,
                order_qty=order_qty,
                cmp=cmp,
                cmp_amount=cmp_amount,
                making_charge=making_charge,
                import_export_charge=import_export_charge,
                box_charge=box_charge,
                poly_bag=poly_bag,
                sewing_thread=sewing_thread,
                cmp_condition=cmp_condition,
                delivery =delivery,
                fabricETA = fabricETA,
                accETA=accETA,
                date = order_date,
                serial_number=serial_number
            )
            saorder.save()
            orderqty = OrderQty.objects.all()
            success ='Order Qty Save Successfully'
            context = {
                'success':success,
                'orderqty':orderqty,
            }
            return render(request, 'OrederCMPreportView.html', context)
        else:
            message = 'Please Enter Correct Data'
            context = {'message':message}
            return render(request, 'style_list.html',context)

class OrederCMPreportView(View):
    def get(self,request):
        orderqty = OrderQty.objects.all()
        form = OrderDeliveryForm()
        context={
            'orderqty':orderqty,
            'form':form
        }
        return render(request, 'OrederCMPreportView.html', context)

class ETAView(View):
    def get(self,request):
        orderqty = OrderQty.objects.all()
        # form = OrderETAForm()
        context = {
            'orderqty': orderqty,
            # 'form': form
        }
        return render(request, 'ETAView.html', context)

class OrderQtyDetailView(TemplateView):
    template_name = 'OrderQtyDetailView.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #     # supplier id get from request url
        order_id = self.kwargs['id']
        # get style info
        order_data = OrderQty.objects.get(id=order_id)
        context['order_data']=order_data

        return context

class EditOrderQtyView(View):
    def get(self, request, pk):
        pi = OrderQty.objects.get(id=pk)
        fm = EditOrderQtyForm(instance=pi)
        return render(request, 'EditOrderQtyView.html', {'form': fm})

    def post(self, request, pk):
        pi = OrderQty.objects.get(id=pk)
        fm = EditOrderQtyForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            making_charge = request.POST.get('making_charge')
            import_export_charge = request.POST.get('import_export_charge')
            box_charge = request.POST.get('box_charge')
            poly_bag = request.POST.get('poly_bag')
            sewing_thread = request.POST.get('sewing_thread')
            cmp_condition = int(making_charge)+int(import_export_charge)+int(box_charge)+int(poly_bag)+int(sewing_thread)
            c = OrderQty.objects.filter(id=pi.id).update(cmp_condition=cmp_condition)

        return redirect('myapp:OrederCMPreportView')


class ProductionInputView(View):
    def get(self,request):
        line = ProductionLine.objects.all()
        style = Style.objects.all()
        context={'line':line,'style':style}
        return render(request, 'ProductionInput.html', context)

    def post(self,request):
        line = request.POST.get('pline')
        style = request.POST.get('style_code')
        input_qty = request.POST.get('qty')
        message = None
        if not line:
            message = 'line error'
        elif not style:
            message = 'style error'
        elif not input_qty:
            message = 'please enter input qty'
        if not message:
            inputqty = ProductionInput(line=line,style=style,input_qty=input_qty)
            inputqty.save()
            line = ProductionLine.objects.all()
            style = Style.objects.all()
            pi = ProductionInput.objects.all()
            context = {'line': line, 'style': style,'success':'Success','pi':pi}
            return render(request, 'ProductionInput.html', context)
        else:
            line = ProductionLine.objects.all()
            style = Style.objects.all()
            context = {'line': line, 'style': style,'message':message}
            return render(request, 'ProductionInput.html', context)




