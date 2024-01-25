class Discount:
    def __init__(self) -> None:
        self.Coupon = []

    def addCoupon(self, campain = "fixed amount" , category = "coupon", item_type = [], every = 0, discount = 0, reduce = 0):
        if category == "coupon":
        
            if (campain == "fixed amount" or campain == "percentage discount") and reduce > 0:
                self.Coupon.append({"rank": 1, "campain": campain, "category": category, "type": item_type, "every": every, "discount": discount, "reduce": reduce})
            else:
                return "error reduce < 0"
            
        elif category == "on top":

            if campain == "percentage discount by item category" and reduce > 0 and len(item_type) > 0:
                self.Coupon.append({"rank": 2, "campain": campain, "category": category, "type": item_type, "every": every, "discount": discount, "reduce": reduce})
            elif campain == "discount by point":
                self.Coupon.append({"rank": 2, "campain": campain, "category": category, "type": item_type, "every": every, "discount": discount, "reduce": reduce})
            else:
                return "error no item_type or reduce < 0"

        elif category == "seasonnal":
            if campain == "special campaigns" and every > 0 and discount > 0:
                self.Coupon.append({"rank": 3, "campain": campain, "category": category, "type": item_type, "every": every, "discount": discount, "reduce": reduce})
            else:
                return "error every or discount < 0"

        #sort coupon by buble sort
        for a in range(len(self.Coupon)):
            for b in range(len(self.Coupon)):
                if self.Coupon[a]["rank"] < self.Coupon[b]["rank"]:
                    self.Coupon[a] , self.Coupon[b] = self.Coupon[b] , self.Coupon[a]
        


    def calcalate(self, item = [], point = 0):
        price = 0
        total = 0
        coupon_discount = 0
        ontop_discount = 0
        seasonnal_discount = 0

        for item_coupon in self.Coupon:
            if item_coupon["category"] == "coupon":
                if item_coupon["campain"] == "fixed amount":
                    coupon_discount = item_coupon["reduce"]
                elif item_coupon["campain"] == "percentage discount":
                    for i in item:
                        price += i["price"]
                    sub = (price/100)*item_coupon["reduce"]
                    coupon_discount = sub
            elif item_coupon["category"] == "on top":
                if item_coupon["campain"] == "percentage discount by item category":
                    for i in item:
                        if i["type"] in item_coupon["type"]:
                            price += i["price"]
                    sub = (price/100)*item_coupon["reduce"]
                    ontop_discount = sub
                elif item_coupon["campain"] == "discount by point":
                    for i in item:
                        price += i["price"]
                    sub = (price/100)*20
                    if point < sub:
                        ontop_discount = point
                    else:
                        ontop_discount = sub
            elif item_coupon["category"] == "seasonnal":
                if item_coupon["campain"] == "special campaigns":
                    for i in item:
                        price += i["price"]
                    a = price // item_coupon["every"]
                    seasonnal_discount = (a * item_coupon["discount"])
            price = 0

        for i in item:
            price += i["price"]  
        total = price - (coupon_discount + ontop_discount + seasonnal_discount)

        return total

'''
iteme  = [{"name":"T-Shirt", "price": 350, "type": "clothing"},{"name":"Hat", "price": 250, "type": "accessories"},{"name":"Belt", "price": 230, "type": "accessories"}]

dis = Discount()

dis.addCoupon(campain = "fixed amount", category = "coupon", reduce = 50)
dis.addCoupon(campain = "percentage discount", category = "coupon", reduce = 50)
dis.addCoupon(campain = "percentage discount by item category",  category = "on top", item_type = ["clothing","accessories","electronics"], reduce = 15)
dis.addCoupon(campain = "discount by point", category = "on top")
dis.addCoupon(campain = "special campaigns", category = "seasonnal", every = 300, discount = 40)

print(dis.calcalate(iteme,68))
'''