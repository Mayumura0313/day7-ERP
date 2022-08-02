###作者: SJW.mayumura



import tkinter as tk

class product(object):
    product_name = "棒球手套"                        # 產品名稱
    product_material = "牛皮"                        # 產品材質
    product_amount = 10                             # 產品數量
    product_company = "Mizuno"                      # 產品公司
    product_country = "Japan"                       # 產品製造地
    play_position = "Outfield"                      # 適合守位
    product_price = "5000"                          # 價錢
    def __init__(self,name,material,amount,company,country,position,price):
        self.product_name =name
        self.product_material = material
        self.product_amount =amount
        self.product_company = company
        self.product_country = country
        self.play_position = position
        self.product_price =price


    def output(self):                                       #method
        print("產品名稱: ",self.product_name)
        print("產品材質: ",self.product_material)
        print("產品數量: ",self.product_amount)
        print("產品公司: ",self.product_company)
        print("產品製造地: ",self.product_country)
        print("適合守位: ",self.play_position)
        print("價錢: ",self.product_price)

sell=product(name="棒球手套",material="牛皮",amount=7,company="Mizuno",country="Japan",position="infield",price="8000")



win = tk.Tk()                                   # 建立GUI 應用程式的主視窗
win.title("史致韋的視窗")                         # 設定主視窗標題
win.resizable(width=False, height=False)        # 設定主視窗不可以被調整大小
win.minsize(width=440, height=480)              # 最小尺寸
win.maxsize(width=640, height=480)              # 最大尺寸



label1 =tk.Label(win,text="產品名稱: "+sell.product_name)                      # 建立文字
label1.place(x=0, y=0)                    # 指定元件位置 x=0, y=0 的位置

label2 =tk.Label(win,text="產品材質: "+sell.product_material)                      # 建立文字
label2.place(x=0, y=20)                    # 指定元件位置 x=0, y=20 的位置

label3 =tk.Label(win,text="產品數量: "+str(sell.product_amount))                      # 建立文字
label3.place(x=0, y=40)                    # 指定元件位置 x=0, y=40 的位置

label4 =tk.Label(win,text="產品公司: "+sell.product_company)                      # 建立文字
label4.place(x=0, y=60)                    # 指定元件位置 x=0, y=60 的位置

label5 =tk.Label(win,text="產品製造地: "+sell.product_country)                      # 建立文字
label5.place(x=0, y=80)                    # 指定元件位置 x=0, y=80 的位置

label6 =tk.Label(win,text="適合守位: "+sell.play_position)                      # 建立文字
label6.place(x=0, y=100)                    # 指定元件位置 x=0, y=100 的位置

label7 =tk.Label(win,text="價錢: "+sell.product_price)                      # 建立文字
label7.place(x=0, y=120)                    # 指定元件位置 x=0, y=120 的位置

win.mainloop()

