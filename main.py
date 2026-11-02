
# 1. მონაცემთა ტიპები და type()
# შექმენით შემდეგი ცვლადები მნიშვნელობებით და თითოეულის ტიპი დაბეჭდეთ type()-ით:

# მთელი რიცხვი (ასაკი)
age = 22
# წილადი რიცხვი (სიმაღლე მეტრებში)
height = 166
# სტრიქონი (სახელი)
name = "Kaso"
# ლოგიკური მნიშვნელობა (True ან False)
female = True
canRead = True

print(type(age))
print(type(height))
print(type(name))
print(type(female))


# 2. მათემატიკური ოპერაციები
# მომხმარებელს შეაყვანინეთ ორი რიცხვი (float(input())-ით) და დაბეჭდეთ:
num1 = float(input("Sheiyvanet pirveli ricxvi: "))
num2 = float(input("sheyvanet meore ricxvi: "))

# ჯამი
print("shekreba: ", num1 + num2 )
# სხვაობა
print("gamokleba: ", num1 - num2 )
# ნამრავლი
print("gamravleba: ", num1 * num2 )
# გაყოფა (/)
print("gayofa: ", num1 / num2 )
# მთელი გაყოფა (//)
print("mteli gayofa: ", num1 // num2 )
# ნაშთი (%)
print("nashti: ", num1 % num2 )
# ხარისხი (**)
print("xarisxi: ", num1 ** num2 )


# 3. სტრიქონების მანიპულაცია
# მომხმარებელს შეაყვანინეთ სახელი და გვარი. შემდეგ დაბეჭდეთ:
firstName = input("Sheiyvanet tqveni saxeli: ")
lastName = input("Sheiyvanet tqveni gvari: ")

# სრული სახელი (სახელი + გვარი)
fullName = firstName + ' ' + lastName
print("Sruli saxeli: ", fullName)
# იგივე სახელი დიდი ასოებით (.upper())
print("Saxeli didi asoebit: ", fullName.upper())
# იგივე სახელი პატარა ასოებით (.lower())
print("Saxeli patara asoebit: ", fullName.lower())
# სახელი, სადაც მხოლოდ პირველი ასოა დიდი (.capitalize())
print("Saxelis mxolod pirveli asoa didi: ", fullName.capitalize())


# 4. print()-ის პარამეტრები
# დაბეჭდეთ რამდენიმე სიტყვა/რიცხვი და გამოიყენეთ:

# სხვადასხვა sep (მაგ. "-", "***", "\t")
print("Halloweenze", 100, "mde", "lamazi", "kostumi", "vnaxe", sep="-")
# სხვადასხვა end
print("Halloweenze", 100, "mde", "lamazi", "kostumi", "vnaxe", sep="***")
# სიტყვებს და რიცხვებს მნიშვნელობა არ აქვს
print("Halloweenze", 100, "mde", "lamazi", "kostumi", "vnaxe", sep="\t")


# 5. შედარების და ლოგიკური ოპერატორები
# დაწერეთ და დაბეჭდეთ მოქმედებები, რომლებიც იყენებენ:

# შედარების ოპერატორებს (==, !=, >, <, >=, <=)
print("Asaki: ", age)
print("Simagle: ", height)
print("Ertmanetis tolia: ", age == height)
print("Ar aris toli: ", age != height)
print("Asaki metia simagleze: ", age > height)
print("Asaki naklebia simagleze: ", age < height)
print("Asaki metia an tolia simaglis: ", age >= height)
print("Asaki naklebia an tilia simaglis: ", age <= height)
# ლოგიკურ ოპერატორებს (and, or, not)
print("Asaki metia 6 da sheudzlia kitxva: ", age > 6 and canRead)
print("Asaki metia 18ze an simagle naklebia 123: ", age > 18 or height < 123)
print("Sheudzlia kitxva? ", not canRead)


# 6. input() და ტიპის სწორად გარდაქმნა
# მომხმარებელს შეაყვანინეთ:

# გადააკონვერტირეთ სწორ მონაცემთა ტიპში
# სახელი
name1 = input("Sheiyvane saxeli: ")
# ასაკი
age1 = int(input("Sheiyvane asaki: "))
# სიმაღლე
height1 = int(input("Sheiyvane simagle: "))
# დაბეჭდეთ მისალმება ამ მონაცემებით.
print("Gamarjoba", name1, "rogorc vici ", age1, "wlis xar da smiagleshi ", height1 ) 
