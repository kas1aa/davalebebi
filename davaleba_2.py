
# ### 1. ინდექსები და Slicing
# შექმენით ცვლადი `word = 'programming'` და დაბეჭდეთ:

word = 'programming'
# - პირველი სიმბოლო
print("pirveli simbolo", word [0])
# - ბოლო სიმბოლო
print("bolo simbolo", word [-1])
# - ბოლოდან მესამე სიმბოლო
print("polodan mesame simbolo", word[-3])
# - პირველი 4 სიმბოლო
print("pirveli 4 simbolo", word[:4])
# - ბოლო 4 სიმბოლო
print("bolo 4 simbolo", word[-4:])
# - ყოველი მეორე სიმბოლო (პირველიდან დაწყებული)
print("yoveli meore simbolo", word[::2])
# - სიტყვა შებრუნებული თანმიმდევრობით
print("sityva shebrunebuli mimdevrobit", word[::-1])


# ### 2. ელფოსტის დაშლა

# მომხმარებელს შეაყვანინეთ ელფოსტა (მაგ. `student@mail.example.com`) და დაბეჭდეთ:
mail = input("sheiyvanet tqveni maili: ")
# - მომხმარებლის სახელი (`@`-მდე ნაწილი)
at_position = mail.index("@")
username = mail[:at_position]
print("momxamrblis saxeli: ", username)
# - დომენი (`@`-ს შემდეგ ნაწილი)
domain = mail[at_position +1:]
print("mailis domeini: ", domain)
# - დომენის პირველი ნაწილი, ანუ პირველ წერტილამდე (`mail`)
dom_position = domain.index(".")
first_part = domain[:dom_position]
print("domeinis pirveli nawili: ", first_part)
# >მინიშნება: `@`-ის პოზიცია იპოვეთ `index()`-ით, წერტილის პოზიცია კი უკვე ამოჭრილ დომენში. ორივე შემთხვევაში გამოიყენეთ slicing


# ### 3. ტელეფონის ნომრის გასუფთავება
# მომხმარებელს შეაყვანინეთ ტელეფონის ნომერი ნებისმიერი ფორმატით, მაგალითად: `+995 555 12-34-56`.
number = str(input("sheiyvanet tqveni telefonis nomeri: +995"))
# დაბეჭდეთ ნომერი, საიდანაც ამოღებულია:
# - ყველა გამოტოვება
# - ყველა ტირე
print(number.replace(" ", "").replace("-", ""))


### 4. URL-მისამართის (slug) გენერატორი
# ბლოგის სტატიის სათაურიდან ხშირად აკეთებენ ვებ-მისამართის ნაწილს. მომხმარებელს შეაყვანინეთ სათაური, მაგალითად `'  My First Python   Program '` და დაბეჭდეთ:

# ```
# my-first-python-program
# ```

# წესები:
# - ყველა ასო პატარაა
# - სიტყვები გამოყოფილია `-`-ით
# - წინ და უკან გამოტოვებები არ არის, სიტყვებს შორის ერთზე მეტი გამოტოვება არ არის
title = input("Sheiyvanet satauri: ")
slug = "-".join(title.lower().split())
print(slug)
# >მინიშნება: `split()` + `join()` + `lower()`


# ### 5. სტუდენტის ბარათი (f-string)
# მომხმარებელს შეაყვანინეთ:
# 1. სახელი
name = input("Sheiyvanet tqveni saxeli: ")
# 2. ასაკი
age = int(input("Sheiyvanet tqveni asaki: "))
# 3. ქალაქი
city = input("Sheiyvanet tqveni dabadebis qalaqi: ")
# 4. საყვარელი პროგრამირების ენა
fav_lang = input("Sheiyvanet tqveni sayvareli programirebis ena: ")

# f-string-ის გამოყენებით დაბეჭდეთ შემდეგი სახის ბარათი (თითოეული ხაზი ცალკე `print()`-ით):
print("STUDENT CARD")
print(f"Name: {name.title()}")
print(f"Age: {age}")
print(f"City: {city.title()}")
print(f"Favorite programming language: {fav_lang.upper()}")

# - ენის სახელი უნდა დაიბეჭდოს დიდი ასოებით
# - სახელი და ქალაქი უნდა დაიბეჭდოს სწორად, მაშინაც კი, თუ მომხმარებელმა პატარა ასოებით ჩაწერა (`title()`)