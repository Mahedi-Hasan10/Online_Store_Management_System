class Person:
    id_counter = 100

    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.user_id = Person.generate_id()

    @classmethod
    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id

    def __repr__(self) -> str:
        return f"User id {self.user_id} email : {self.email}"


class Store:
    def __init__(self) -> None:
        self.total_products = {}

    def add_product(self, seller_id, product):
        productDict = vars(product)
        # print(product)
        if seller_id not in self.total_products:
            self.total_products[seller_id] = []
            seller_info = {}
            seller_info["total_sell_product"] = 0
            seller_info["total_sell_amount"] = 0
            seller_info["total_profit_amount"] = 0
            self.total_products[seller_id].append(seller_info)

        self.total_products[seller_id].append(productDict)


class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product Name : {self.name} || Product Price : {self.price} || Product Quantity : {self.quantity}"


class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)

    def add_product(self, store, product_name, prduct_price, product_qantity):
        product = Product(product_name, prduct_price, product_qantity)
        store.add_product(self.user_id, product)

    def sell_info(self, store):
        print(store.total_products[self.user_id][0])


class Owner(Person):
    def __init__(self, email, password) -> None:
        self.total_sell_product = 0
        self.total_sell_price = 0
        self.total_profit = 0
        super().__init__(email, password)

    def sell_info(self, store):
        all_seller_id = store.total_products.keys()
        for seller_id in all_seller_id:
            sell_info = store.total_products[seller_id][0]
            self.total_sell_product += sell_info["total_sell_product"]
            self.total_sell_price += sell_info["total_sell_amount"]
            self.total_profit += sell_info["total_profit_amount"]
        sell_info = {
            "total_sell_product": self.total_sell_product,
            "total_sell_price": self.total_sell_price,
            "total_profit": self.total_profit
        }
        return sell_info


class Customer(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)
        self.total_buy_amount = 0
        self.total_buy_product = 0

    def show_product(self, store):
        print("--------------------Our Product List-------------------")
        all_seller_keys = store.total_products.keys()
        for seller_id in all_seller_keys:
            print()
            print("Seller Id : ", seller_id)
            print("=========================")
            for index in range(1, len(store.total_products[seller_id])):
                product = store.total_products[seller_id][index]
                print("Name : ", product["name"], " Price : ",
                      product["price"], " Quantity : ", product["quantity"])

    def buy_product(self, store, seller_id, product_name, quantity):
        flag = 1
        all_seller_id = store.total_products.keys()
        if seller_id in all_seller_id:
            for index in range(1, len(store.total_products[seller_id])):
                product = store.total_products[seller_id][index]
                if product["name"] == product_name:
                    if quantity <= product["quantity"]:
                        product["quantity"] -= quantity
                        self.total_buy_product += quantity
                        self.total_buy_amount += product["price"]*quantity
                        seller = store.total_products[seller_id][0]
                        seller["total_sell_product"] += quantity
                        seller["total_sell_amount"] += product["price"]*quantity
                        seller["total_profit_amount"] += 10 * \
                            product["price"]*quantity/100
                        flag = 0
                    else:
                        print("Not enough product!!")
        else:
            print("Seller id not found!!")
        if flag == 1:
            print("Product not found")


store = Store()

seller1 = Seller('s1@gmail.com', 1234)
seller2 = Seller('s2@gmail.com', 12345)
seller3 = Seller('s3@gmail.com', 123456)
# print(seller1)
# print(seller2)
# print(seller3)

seller1.add_product(store, "Ipun10", 150, 10)
seller1.add_product(store, "Ipun11", 200, 12)
seller2.add_product(store, "Ipun12", 250, 15)
seller2.add_product(store, "Ipun13", 350, 9)
# print(store.total_products)
# print(store.total_products)
customer = Customer('mah@gamil.com', 123)
customer1 = Customer('mah1@gamil.com', 1231)
# customer.show_product(store)
# print("After buy something==================")
customer.buy_product(store, 100, "Ipun11", 5)
customer1.buy_product(store, 101, "Ipun12", 5)
# customer.show_product(store)

# print(store.total_products)

# seller1.sell_info(store)
# seller2.sell_info(store)

owner = Owner("admin@gmail.com", 789)
print(owner.sell_info(store))
