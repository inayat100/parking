import time
class Parking ():
    def __init__(self):
        self.lt= []

    def slot_add(self):
        global slot
        global total
        t = time.localtime()
        tm = f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'
        while True:
            try:
                if slot > 0:
                    print('''
                                   1 for car parking  Rs.50     2 for bike parking  Rs.20
                                   3 for bicycle parking Rs.10   4 for trucks parking Rs.100
                                   ''')
                    ty = int(input("enter parking type..."))
                    if ty == 1:
                        am = 50
                    elif ty == 2:
                        am = 20
                    elif ty == 3:
                        am = 10
                    elif ty == 4:
                        am = 100
                    else:
                        print("please enter right type...")
                        continue
                    self.id = input("enter vehicle id...")
                    if self.uniq():
                        print("this id is exist  take unique id....")
                        continue
                    self.name = input("enter vehicle name or number...")
                    self.obj = {'id':int(self.id),'name':self.name,'amount':am,'time':tm}
                    self.ad = self.lt.append(self.obj)
                    print(f"for this parking amount : {am}")
                    total = total + am
                    slot = slot - 1
                    print(f"we have only slot {slot}")
                    print("")
                    y = input("for more add press Y/y and for exit presss any key")
                    print("")
                    if y == 'y' or y == 'Y':
                        continue
                    else:
                        print("exit...")
                        print("")
                        break
                else:
                    print("sloat is full")
                    print("")
                    break

            except Exception:
                print("maybe your  input is not right....")

    def slot_remove(self):
        global slot
        global total
        try:
            self.id = input("enter vehicle id")
            for l in self.lt:
                if l['id'] == int(self.id):
                    self.r = self.lt.index(l)
                    self.lt.remove(self.lt[self.r])
                    total = total - l['amount']
                    slot = slot + 1
                    print("removed....")
                    break
            else:
                print("id not matched..... enter right id")
        except Exception:
            print("maybe  your input is not right....")

    def view(self):
        print('''
            Id   Number   Amount   Time ''')
        for l in self.lt:
            print( f'''
            {l['id']}   {l['name']}    {l['amount']}    {l['time']} ''')

    def uniq(self):
         for l in self.lt:
             if l['id'] == int(self.id):
                 return True


if __name__ == '__main__':
    slot= 4
    total = 0
    p = Parking()
    while True:
        print(f"we have total parking  slot {slot}    Total amount {total}")
        print('''
        1 Add parking vehicle
        2 Remove parking vehicle 
        3 View all vehicle detail
        ''')
        try:
            op = input("what do you want perform Choice a number")
            print("")
            if int(op) == 1:
                p.slot_add()
            elif int(op)  == 2:
                p.view()
                print("enter right id for remove parking vehicle")
                p.slot_remove()
            elif int(op)  == 3:
                p.view()
            else:
                break
        except Exception:
            print("maybe your your input is wrong....")
            input()
            # print("\033[31m maybe your your input is wrong....")
        # raise Exception("enter int")





