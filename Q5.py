#Abel Goshu
#1675552

services = {'-': 0, 'Oil change' : 35, 'Tire rotation' : 19, 'Car wash' : 7, 'Car wax' : 12}
first_service = ""
second_service = ""
invoice_total = 0
print ('Davy\'s auto shop services')
print ('Oil change -- $35')
print ('Tire rotation -- $19')
print ('Car wash -- $7')
print ('Car wax -- $12\n')
oil_change = 35
tire_rotation = 19
car_wash = 7
car_wax =  12
first_service = input('Select first service:')
print ('')
second_service = input('Select second service:')
print('')
print('')
print ('Davy\'s auto shop invoice\n')
if(first_service == '-'):
  print('Service 1: No service')
else:
  print('Service 1: %s, $%d' % (first_service, services.get(first_service)))
if(second_service == '-'):
  print('Service 2: No service')
else:
  print('Service 2: %s, $%d' % (second_service, services.get(second_service)))
invoice_total = services.get(first_service) + services.get(second_service)
print()
print('Total: $%d' % (invoice_total))
