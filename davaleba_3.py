
# ### 1. ლუწი თუ კენტი
# მომხმარებელს შეაყვანინეთ მთელი რიცხვი და `if / else`-ის გამოყენებით დაბეჭდეთ, არის თუ არა ის ლუწი.

# >მაგალითი:
# >
# > ```
# > Enter number: 7
# > 7 is odd
# > ```
num = int(input("Semoiyvanet ricxvi: "))
if num % 2 == 0:
    print("luwia")
else:
    print("kentia")




# ### 2. ასაკობრივი კატეგორია
# მომხმარებელს შეაყვანინეთ ასაკი და `if / elif / else`-ის გამოყენებით დაბეჭდეთ კატეგორია:

# | ასაკი | კატეგორია |
# |-------|-----------|
# | 0 – 12 | Child |
# | 13 – 17 | Teenager |
# | 18 – 64 | Adult |
# | 65 და მეტი | Senior |
age = int(input("shemoiyvanet asaki: "))

if age < 0:
    print("Monacemi sheusabamoa (Invalid age)")
elif age <= 12:
    print("Momxmarebeli bavshvia (Child)")
elif age <= 17:
    print("Momxmarebeli tineijeria (Teenager)")
elif age <= 64:
    print("Momxmarebeli zrdasrulia (Adult)")
else:
    print("Momxmarebeli moxucebulia (Senior)")
# - თუ ასაკი უარყოფითია, დაბეჭდეთ `Invalid age`


# ### 3. შეფასების სისტემა
# მომხმარებელს შეაყვანინეთ ქულა (0-დან 100-მდე) და დაბეჭდეთ შესაბამისი ნიშანი:

# | ქულა | ნიშანი |
# |------|--------|
# | 90 – 100 | A |
# | 80 – 89 | B |
# | 70 – 79 | C |
# | 60 – 69 | D |
# | 50 – 59 | E |
# | 50-ზე ნაკლები | F |

grade = int(input("shemoiyvanet asaki: "))

if grade < 0 or grade > 100:
    print("Sheusabamo monacemi")
elif grade >= 90:
    print("Studentis qulaa A")
elif grade >= 80:
    print("Studebtis qulaa B")
elif grade >= 70:
    print("Studentis qulaa C")
elif grade >= 60:
    print("Studentis qulaa D")
elif grade >= 50:
    print("Studentis qulaa E")
else:
    print("Studenti chawrilia F")

# - თუ ქულა 0-ზე ნაკლებია ან 100-ზე მეტი, დაბეჭდეთ `Invalid grade`
# - შეამოწმეთ პროგრამა სხვადასხვა ქულით (`95`, `85`, `70`, `49`, `100`, `-5`, `150`) და დარწმუნდით, რომ შედეგი ყოველთვის სწორია


# ### 4. დიახ / არა
# მომხმარებელს ჰკითხეთ: `Do you like Python? (yes/no)`

# - თუ პასუხია `yes` — დაბეჭდეთ `Great!`
# - თუ პასუხია `no` — დაბეჭდეთ `Maybe you will like it later`
# - ნებისმიერ სხვა შემთხვევაში — დაბეჭდეთ `Please answer yes or no`

# პროგრამამ ერთნაირად უნდა იმუშაოს შემდეგი შეყვანებისთვისაც: `YES`, `  yes `, `No`, `nO\n`.

answer = input("Do you like Python? (yes/no)")

answer = answer.strip().lower()

if answer == "yes":
    print("Great!")
elif answer == "no":
    print("Maybe you will like it later ♥")
else:
    print("Please answer yes or no")

# ### 5. კალკულატორი
# მომხმარებელს შეაყვანინეთ:
# 1. პირველი რიცხვი
# 2. ოპერაცია (`+`, `-`, `*`, `/`)
# 3. მეორე რიცხვი

# დაბეჭდეთ ოპერაციის შედეგი.

# - თუ მომხმარებელმა ჩაწერა ოპერაცია, რომელიც ზემოთ ჩამოთვლილ ოთხში არ შედის, დაბეჭდეთ `Unknown operation`

num1 = float(input("Sheiyvanet pirveli ricxvi: "))
op = input("Sheiyvanet moqmedeba: ")
num2 = float(input("Sheiyvanet meore ricxvi: "))

if op == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == "/":
    if num2 == 0:
        print("Gayofa ar sheidzleba")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("operacia amoucnobia")