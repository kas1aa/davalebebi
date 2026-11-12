
# ### 1. კინოთეატრი (`and`)
# მომხმარებელს შეაყვანინეთ ასაკი (მთელი რიცხვი) და ფული (მთელი რიცხვი). ბილეთის ფასია `15`.

# - თუ ასაკი არის **12 წელზე მეტი ან ტოლი** და ფული არის **ბილეთის ფასზე მეტი ან ტოლი**, დაბეჭდეთ `Enjoy the movie`
# - ყველა დანარჩენ შემთხვევაში დაბეჭდეთ `Access denied`
age = int(input("Sheiyvanet tqveni asaki: "))
money = int(input("Sheiyvanet biletis tanxa: "))

if age >= 12 and money >= 15:
    print("Isiamovnet filmit (Enjoy the movie)")
else:
    print("SamwuxaroT filmze ar daishvebit (Access denied)")


# ### 2. ნაკიანი წელი
# მომხმარებელს შეაყვანინეთ წელი და დაბეჭდეთ, არის თუ არა ის 'ნაკიანი' (`Leap year` / `Not a leap year`).

# წელი ნაკიანი, თუ:
# - იყოფა 4-ზე, **და** არ იყოფა 100-ზე
# - **ან** იყოფა 400-ზე
year = int(input("Sheiyvanet weli: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Nakiani weliwadia (Leap year)")
else:
    print("Ar aris nakiani weli (Not a leap year)")

# შეამოწმეთ პროგრამა ამ წლებით: `2024` (ნახტომი), `2023` (არა), `1900` (არა), `2000` (ნახტომი).


# ### 3. ბანკომატი (ჩადგმული `if`)
# მომხმარებელს შეაყვანინეთ:
# 1. ბარათის PIN-კოდი (მთელი რიცხვი)
# 2. თანხა, რომლის გატანაც სურს (მთელი რიცხვი)

# ბანკომატში სწორი PIN არის `1234`, ბალანსი კი `500`.
correct_pin = 1234
balance = 500
pin = int(input("Sheiyvanet paroli: "))
# პროგრამამ ჯერ უნდა შეამოწმოს PIN-კოდი, და მხოლოდ სწორი PIN-ის შემთხვევაში გადავიდეს თანხის შემოწმებაზე:

# - თუ PIN არასწორია — `Wrong PIN`
# - თუ PIN სწორია:
#   - თუ თანხა 0-ზე ნაკლები ან ნულია — `Invalid amount`
#   - თუ თანხა ბალანსზე მეტია — `Not enough money`
#   - წინააღმდეგ შემთხვევაში — `Take your money: <თანხა>` და ახალი ბალანსი
if pin != correct_pin:
    print("Paroli arasworia (Wrong PIN)")
else:
    amount = int(input("Sheiyvanet tanxa: "))

    if amount <= 0:
        print("Tanxa sheusabamoa")
    elif amount > balance:
        print("Baratze ar aris sakmarisi tanxa")
    else:
        print(f"Aiget tqveni tanxa: {amount}. Darchenili tanxaa: {balance - amount} gisurvebt warmatebul dges ♥")

# >მინიშნება: გარე `if / else` ამოწმებს PIN-ს, შიდა `if / elif / else` კი თანხას. შიდა ბლოკი უნდა იყოს გარე `if`-ის შიგნით (დამატებითი ინდენტაციით)


# ### 4. შეცდომების დამუშავება (`ValueError`, `ZeroDivisionError`, `TypeError`)
# მოცემულია პროგრამა, რომელიც მომხმარებლისგან იღებს სახელს, ასაკს და რიცხვს:


# **ნაწილი 1.** გაუშვით პროგრამა და ნახეთ, რა შეცდომები ჩნდება შემდეგი შეყვანებისას:
# - `John`, `20`, `5`
# - `John`, `abc`, `5`
# - `John`, `20`, `0`
try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print(f"Hello, {name}! Next year you will be {age + 1} years old.")
# **ნაწილი 2.** მთელი კოდი მოაქციეთ `try`-ში და დაამუშავეთ შეცდომები:
# - `ValueError` — დაბეჭდეთ `Invalid input`
# - `ZeroDivisionError` — დაბეჭდეთ `Cannot divide by zero`
# - `TypeError` — დაბეჭდეთ `Cannot join text and number`
# - ნებისმიერი სხვა შეცდომისთვის (`Exception`) — დაბეჭდეთ თვითონ შეცდომა
except ValueError:
    print('Invalid input')

except ZeroDivisionError:
    print('Cannot divide by zero')

except TypeError:
    print('Cannot join text and number')

except Exception as e:
    print(e)
# **ნაწილი 3.** გაასწორეთ ბოლო `print()` ისე, რომ `TypeError` აღარ გამოვიდეს და პროგრამამ სწორად იმუშაოს (მაგ. `John`, `20`, `5` → `Hello, John! Next year you will be 21 years old.`).

# >მინიშნება: `TypeError` ჩნდება მაშინ, როცა ტექსტს (`str`) რიცხვთან (`int`) აერთებთ `+`-ით. გამოსწორება შეგიძლიათ `str()`-ით ან f-string-ით
# >
# >მინიშნება: `except Exception as e` ყოველთვის ბოლო უნდა იყოს, წინააღმდეგ შემთხვევაში ის დაიჭერს ყველა შეცდომას და კონკრეტული `except`-ები აღარასოდეს შესრულდება
