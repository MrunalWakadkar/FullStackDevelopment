Details ={"sita":{"age":20 ,"marks":90} , "gita":{"age":19 ,"marks":75} , "mita":{"age":22 , "marks":88},"tina":{"age":16 ,"marks":65} ,"nita":{"age":19 ,"marks":85}
          }

#exitchoice=input("Enter your choice: ")

def Addentry():
    name=input("Enter name of the student : ")
    age=int(input("Enter age :"))
    marks=int(input("Enter marks :"))
    Details[name1]={age,marks}

def updateentry():
    name2=input("Enter name of the student which you want to update  : ")
    age=int(input("Enter updated age :"))
    marks=int(input("Enter updated marks :"))
    Details.update({name2:{age,marks}})

Addentry()
updateentry()

    




