
# ### 1. საყიდლების სია (დამატება და წაშლა)
# დაიწყეთ სიით `shopping = ['milk', 'bread', 'eggs']` და თანმიმდევრულად შეასრულეთ მოქმედებები. ყოველი ნაბიჯის შემდეგ დაბეჭდეთ სია.
shopping = ['milk', 'bread', 'eggs']

# 1. ბოლოში დაამატეთ `'cheese'`
shopping.append('cheese')
print(shopping)

# 2. სიის დასაწყისში ჩასვით `'apples'`
shopping.insert(0, 'apples')
print(shopping)

# 3. ბოლო ელემენტი შეცვალეთ `'butter'`-ით
shopping[-1] = 'butter'
print(shopping)

# 4. სია დაუმატეთ სხვა სია `['tea', 'coffee']`
shopping.extend(['tea', 'coffee'])
print(shopping)

# 5. წაშალეთ `'bread'`
shopping.remove('bread')
print(shopping)

# 6. წაშალეთ ელემენტი ინდექსით `1` და დაბეჭდეთ, რომელი ელემენტი წაიშალა
removed = shopping.pop(1)
print("Removed:", removed)
print(shopping)

# ### 2. გამოცდის ქულები
# ჯგუფის გამოცდის ქულები ჩაწერილია სიაში `scores = [85, 92, 78, 92, 65, 88, 92]`. ორიგინალი სია არ უნდა შეიცვალოს, ამიტომ მოქმედებები შეასრულეთ მის **ასლებზე**.

# დაბეჭდეთ:
scores = [85, 92, 78, 92, 65, 88, 92]

# 1. რამდენ სტუდენტს აქვს ქულა `92`
print("Count of 92:", scores.count(92))

# 2. რომელ ინდექსზეა ქულა `78`
print("Index of 78:", scores.index(78))

# 3. ქულები ზრდადობით დალაგებული (`asc_scores`)
asc_scores = scores.copy()
asc_scores.sort()
print("Ascending:", asc_scores)

# 4. ქულები კლებადობით დალაგებული (`desc_scores`)
desc_scores = scores.copy()
desc_scores.sort(reverse=True)
print("Descending:", desc_scores)

# 5. ყველაზე მაღალი და ყველაზე დაბალი ქულა, დალაგებული სიიდან ინდექსით
print("Highest:", desc_scores[0], "Lowest:", desc_scores[-1])

# 6. ორიგინალი სია, რომ დარწმუნდეთ, რომ არ შეცვლილა
print("Original:", scores)

# ### 3. ჩადგმული სია (მატრიცა)
# შექმენით სია `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` და დაბეჭდეთ:
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

# 1. რამდენი სტრიქონია მატრიცაში
print("Rows:", len(matrix))

# 2. ბოლო სტრიქონი
print("Last row:", matrix[-1])

# 3. რიცხვი `6` ორმაგი ინდექსით(დადებითი და უარყოფითი)
print("Positive indexes:", matrix[1][2])
print("Negative indexes:", matrix[-2][-1])

# 4. რიცხვი `7`, ბოლო სტრიქონის პირველი ელემენტის სახით (უარყოფითი ინდექსით)
print("Number 7:", matrix[-1][0])

# ამის შემდეგ ცენტრალური ელემენტი `5` შეცვალეთ `50`-ით და დაბეჭდეთ მთლიანი მატრიცა.
matrix[1][1] = 50

print("Matrix:", matrix)

# >მინიშნება: `matrix[1]` არის მეორე სტრიქონი, `matrix[1][2]` კი ამ სტრიქონის მესამე ელემენტი


# ### 4. სიის შევსება (`while`)
# შექმენით ცარიელი სია `numbers = []`. `while` ციკლში მომხმარებელს ერთიმეორის მიყოლებით შეაყვანინეთ რიცხვები და თითოეული დაამატეთ სიაში. პროგრამა მუშაობს მანამ, სანამ მომხმარებელი არ ჩაწერს `stop`-ს.

# ციკლის დასრულების შემდეგ დაბეჭდეთ:

# 1. სია
# 2. რამდენი რიცხვი შეიყვანეს
# 3. პირველი და ბოლო ელემენტი
# 4. სია კლებადობით დალაგებული

numbers = []

while True:
    num = input("Sheiyvanet ricxvi: ")

    if num == "stop":
        break

    numbers.append(int(num))

print("Sia:", numbers)
print("Ricxvebis raodenoba: ", len(numbers))

if len(numbers) > 0:
    print("Pirveli:", numbers[0], "Bolo:", numbers[-1])

    desc_numbers = numbers.copy()
    desc_numbers.sort(reverse=True)

    print("Sia klebadobis mixedvit: ", desc_numbers)
else:
    print("Sia carielia: ")