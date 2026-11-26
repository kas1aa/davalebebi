# # ამოცანები (ფუნქციები)

# ## ამოცანა 1. ბილეთების ბეჭდვა (DRY და პარამეტრები)

# ქვემოთ მოცემული კოდი სამჯერ იმეორებს ერთსა და იმავე ლოგიკას:


# 1. გადაწერეთ ეს კოდი ისე, რომ DRY პრინციპი არ დაირღვეს: შექმენით ფუნქცია `print_ticket`, რომელიც ბეჭდავს ბილეთს იგივე ფორმატში.
def print_ticket(passenger, destination, ticket_class):
    print('--- TICKET ---')
    print('Passenger: ' , passenger)
    print('Destination: ' , destination)
    print('Class: ' , ticket_class)

print_ticket('Nika', 'Batumi', 'Economy')

# 2. გამოიძახეთ ფუნქცია სამივე მგზავრისთვის: ერთხელ მხოლოდ პოზიციური არგუმენტებით, ერთხელ მხოლოდ keyword არგუმენტებით და ერთხელ keyword არგუმენტად გადააწოდეთ მხოლოდ კლასი
print_ticket(
    passenger='Mari',
    destination='Kutaisi',
    ticket_class='Business'
)

print_ticket('Luka', 'Batumi', ticket_class='Economy')

# ---

# ## ამოცანა 2. ტემპერატურა (`return` და default პარამეტრი)

# 1. დაწერეთ ფუნქცია `celsius_to_fahrenheit`, რომელიც ატრიბუტად იღებს ცელსიუსის მნიშვნელობას და **აბრუნებს** ტემპერატურას ფარენჰაიტში (ფორმულა: `celsius * 9 / 5 + 32`) და არაფერს ბეჭდავს.
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 2. გამოიძახეთ ფუნქცია რიცხვებზე `0`, `37` და `100`, შედეგები შეინახეთ ცვლადებში და დაბეჭდეთ ფორმატით: `37C = 98.6F`.
temp1 = celsius_to_fahrenheit(0)
temp2 = celsius_to_fahrenheit(37)
temp3 = celsius_to_fahrenheit(100)

print(f'0C = {temp1}F')
print(f'37C = {temp2}F')
print(f'100C = {temp3}F')

# 3. დაწერეთ ფუნქცია `is_warm(celsius, limit=20)`, რომელიც აბრუნებს `True`-ს, თუ `celsius` მეტია `limit`-ზე, და `False`-ს, თუ არა.
def is_warm(celsius, limit=20):
    return celsius > limit

# 4. გამოიძახეთ `is_warm` სამჯერ და შედეგები დაბეჭდეთ:
#    - მხოლოდ ტემპერატურის გადაცემით (`25`);
#    - ტემპერატურისა და ლიმიტის გადაცემით (`25` და `30`);
#    - ორივე არგუმენტი keyword-ით, შებრუნებული რიგით (`limit=10`, `celsius=15`).
print(is_warm(25))

print(is_warm(25, 30))

print(is_warm(limit=10, celsius=15))

# ---

# ## ამოცანა 3. რიცხვების ანალიზი (რამდენიმე მნიშვნელობის დაბრუნება)

# 1. დაწერეთ ფუნქცია `analyze_numbers(numbers)`, რომელიც იღებს რიცხვების სიას და **ერთდროულად** აბრუნებს სამ მნიშვნელობას: უმცირეს რიცხვს, უდიდეს რიცხვს და საშუალო არითმეტიკულს.
def analyze_numbers(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average

# 2. ფუნქცია გამოიძახეთ სიაზე `[12, 7, 25, 3, 18]` და შედეგი ერთ ხაზზე გახსენით სამ ცვლადში (unpacking).
numbers = [12, 7, 25, 3, 18]

min_num, max_num, avg = analyze_numbers(numbers)

# 3. დაბეჭდეთ შედეგი ფორმატით: `Min: 3, Max: 25, Average: 13.0`.
print(f'Min: {min_num}, Max: {max_num}, Average: {avg}')

# 4. ფუნქცია ისევ გამოიძახეთ, ოღონდ შედეგი ამჯერად ერთ ცვლადში ჩაწერეთ და დაბეჭდეთ ეს ცვლადი.
result = analyze_numbers(numbers)

print(result)

# ---

# ## ამოცანა 4. ჯგუფის სია (ცვალებადი default მნიშვნელობა)

# 1. დაწერეთ ფუნქცია `add_student(name, group=None)`, რომელიც ამატებს სტუდენტს ჯგუფის სიაში და აბრუნებს განახლებულ სიას.
#    - თუ `group` არ გადაეცა, ფუნქციამ უნდა შექმნას ახალი ცარიელი სია.
#    - თუ სტუდენტი უკვე არის სიაში, ფუნქციამ ხელახლა არ უნდა დაამატოს.
def add_student(name, group=None):

    if group is None:
        group = []

    if name not in group:
        group.append(name)

    return group
    
# 2. გამოიძახეთ ფუნქცია შემდეგნაირად და შედეგები დაბეჭდეთ:
group_a = add_student('Ana')
group_b = add_student('Nika')
group_a = add_student('Mari', group_a)
group_a = add_student('Ana', group_a)

print('Group A:', group_a)
print('Group B:', group_b)

# 3. დარწმუნდით, რომ `group_a` და `group_b` ერთმანეთისგან დამოუკიდებელი სიებია (`group_a` უნდა იყოს `['Ana', 'Mari']`, `group_b` კი `['Nika']`).
print('A jgufi da B jgufi erti da igivea? ' , group_a is group_b)

# ---

# ## ამოცანა 5. პაროლის სიძლიერე (რამდენიმე `return`)

# დაწერეთ ფუნქცია `check_password(password)`, რომელიც აბრუნებს პაროლის შეფასებას. პირობები შეამოწმეთ თანმიმდევრობით და გამოიყენეთ ადრეული `return` (`else` და `elif` არ გამოიყენოთ):

def check_password(password):

# 1. თუ პაროლი 6 სიმბოლოზე მოკლეა, დააბრუნეთ `'Too short'`.
    if len(password) < 6:
        return 'Paroli moklea'
# 2. თუ პაროლი მხოლოდ ციფრებისგან შედგება (`isdigit()`), დააბრუნეთ `'Weak'`.
    if password.isdigit():
        return 'Paroli dzalian sustia'
# 3. თუ პაროლში არ არის ციფრი ან არ არის ასო, დააბრუნეთ `'Medium'`.
    if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return 'Uketesi parolis mofiqreba shegidzia'
# 4. სხვა შემთხვევაში დააბრუნეთ `'Strong'`.
    return 'Kargi parolia'

# შემდეგ ციკლით გადაუარეთ ამ სიას და თითოეული პაროლისთვის დაბეჭდეთ შედეგი ფორმატით `{password} -> Too short`:

passwords = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi2024']

for password in passwords:
    print(f'{password} -> {check_password(password)}')