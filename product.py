products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
	    break
	price = input('請輸入商品價格')
	products.append([name, price]) #於於p = [] + p.append(name) + p.append(price)三行
print(products)

products[0][0]