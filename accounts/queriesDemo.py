''' 
returns all customers from customer table
    customers = Customer.objects.all()
    print(customer)   //you will get a queryset
returns first customer from the table
    firstCustomer = Customer.objects.first()
returns last customer from the table
    firstCustomer = Customer.objects.last()
returns single customer by name
    customer1 = Customer.objects.get(name="Ajith M") 
    print(customer1.email)
    print(customer1.id)
    //if there are more than one same name it will be error so
    customer1 = Customer.objects.get(id=2) 
return all orders related to customer
    orders = customer1.order_set.all()   //even though Order is capital O here you use small o
    print()
return customer related to order
    order = Order.objects.first()
#filter method 
Return products from product table with value
    products = Product.objects.filter(category = "Outdoor")
    print(products)
multiple filter
    products = Product.objects.filter(category = "Outdoor", name = "")
sort 
    products = Product.objects.all().order_by('id')
    products = Product.objects.all().order_by('-id') //reverse order


#many to many relationship query
Returns all products with tag of 'Sports'
    products = Product.objects.filter(tags__name="Sports" ) //tags is the attribute name in Product and name is the field name in Tag

Return the number of times a ball was ordered
    ballOrders = firstCustomer.order_set.filter(product_name="Ball").count()
Returns total count for each product ordered
    allOrders={} //empty dictionary
    for order in firstCustomer.order_set.all(): //loop through all customer orders
        if order.product.name in allOrders:
            allOrders[order.product.name] += 1
        else:
            allOrders[order.product.name] = 1  //creating
        
    //output : allOrders :{'Ball': 2 , 'BBQ Grill': 1}
            


''' 