#Abel Goshu
#1675552

lemon_juice=float(input('Enter amount of lemon juice (in cups):\n'))
water=float(input('Enter amount of water (in cups):\n'))
agave_nectar=float(input('Enter amount of agave nectar (in cups):\n'))
serving=float(input('How many servings does this make?\n'))
print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(serving))+' servings')
print(str('{:.2f}'.format(lemon_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(water))+' cup(s) water')
print(str('{:.2f}'.format(agave_nectar))+' cup(s) agave nectar')
print("")
new_serving=float(input('How many servings would you like to make?\n'))
x=new_serving/serving
new_lemon_juice=lemon_juice*x
new_water=water*x
new_agave_nectar=agave_nectar*x
print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water))+' cup(s) water')
print(str('{:.2f}'.format(new_agave_nectar))+' cup(s) agave nectar')
print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice/16))+' gallon(s) lemon juice')
print(str('{:.2f}'.format(new_water/16))+' gallon(s) water')
print(str('{:.2f}'.format(new_agave_nectar/16))+' gallon(s) agave nectar')