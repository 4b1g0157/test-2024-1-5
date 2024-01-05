class Product:
    #建構子為建立類別中所含的屬性,Self,參數為設定函數以便後續程式
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def BUY(self, quantity):
        if quantity <= self.stock_quantity:
            total_price = self.price * quantity
            self.stock_quantity -= quantity
            print(f"\n已成功購買 {quantity} 數量的 {self.name}。總費用為：{total_price}")
        else:
            print(f"\n抱歉，{self.name} 庫存不足。剩餘庫存：{self.stock_quantity}")

    def introduce(self):
        return(f"商品名稱為:{self.name} 價格為{self.price}。\n目前有 {self.stock_quantity} 件庫存")

    def update(self, new_quantity):
        self.stock_quantity = new_quantity

        
product1 = Product("電腦", 50000, 10)
product2 = Product("手機", 8000, 15)
product3 = Product("耳機", 500, 30)

product1.BUY(2)
product1_intro = product1.introduce()
print(f"{product1_intro}")
product1.update(8)


product2.BUY(5)
product2_introduce = product2.introduce()
print(f"{product2_introduce}")
product2.update(10)

product3.BUY(31)
product3_introduce = product3.introduce()
print(f"{product3_introduce}")
product3.update(30)