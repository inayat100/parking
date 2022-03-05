import time
class park():
    def __init__(self):
        self.lt= []
        print(f"we have only slot {slot}")

    def slot_add(self):
        global slot
        t = time.localtime()
        tm = f'{t.tm_hour}:{t.tm_min}:{t.tm_sec}'
        while True:
            try:
                if slot > 0:
                    self.id = input("enter vehicle id...")
                    if self.uniq():
                        print("this id is exist take uniq id....")
                        continue
                    self.name = input("enter vehicle name...")
                    self.obj = {'id':int(self.id),'name':self.name,'time':tm}
                    self.ad = self.lt.append(self.obj)
                    slot = slot - 1
                    print(f"we have only slot {slot}")
                    print("")
                    y = input("for more add press Y and for exit presss any key")
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
                print(" maybe your your input is wrong....")

    def slot_remove(self):
        global slot
        try:
            self.id = input("enter vehicle id")
            for l in self.lt:
                if l['id'] == int(self.id):
                    self.r = self.lt.index(l)

                    self.lt.remove(self.lt[self.r])
                    slot = slot + 1
                    print("removed....")
                    break
            else:
                print("id not matched.....")
        except Exception:
            print("maybe your your input is wrong....")

    def view(self):
        print("view....")
        print("Id " ,"  Name",  "    Time")
        for l in self.lt:
            print( f"{l['id']}  , {l['name']} ,   {l['time']}")

    def uniq(self):
         for l in self.lt:
             if l['id'] == int(self.id):
                 return True


if __name__ == '__main__':
    slot= 4
    p = park()
    while True:
        print('''
        1 add slot
        2 remove slot 
        3 show all slot
        ''')
        try:
            op = input("choice optins")
            print("")
            if int(op) == 1:
                p.slot_add()
            elif int(op)  == 2:
                p.view()
                print("just enter id for delete")
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





