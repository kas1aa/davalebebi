# # ამოცანები (Dict და Set)

# ## ამოცანა 1. დუბლიკატების მოშორება

# მოცემულია სია:

# ```python
# numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
# ```
numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
# სეტის გამოყენებით:

# 1. მოაშორეთ სიას განმეორებადი ელემენტები და შედეგი დაბეჭდეთ სიის სახით.
unique_numbers = set(numbers)
print('Siis unikaluri elementebi: ' , list(unique_numbers))
# 2. დაბეჭდეთ, რამდენი უნიკალური ელემენტია სიაში.
print('Unikaluri elementebis raodenoba: ' , len(unique_numbers))
# 3. შეამოწმეთ, არის თუ არა რიცხვი `23` უნიკალურ ელემენტებში.
print('Aris tu ara 23 mocemul siashi: ' , 23 in unique_numbers)

# ## ამოცანა 2. სეტების ოპერაციები

# ორმა სტუდენტმა დაასახელა პროგრამირების ენები, რომლებიც იცის:

# ```python
# ana = 'python', 'java', 'c', 'sql'
# nika = 'python', 'javascript', 'sql', 'go'
# ```
ana = {'python', 'java', 'c', 'sql'}
nika = {'python', 'javascript', 'sql', 'go'}
# ოპერატორებითაც და მეთოდებითაც (`union`, `intersection`, `dierence`, `symmetric_dierence`) იპოვეთ და დაბეჭდეთ:

# 1. ყველა ენა, რომელიც იცის ერთმა მაინც მათგანმა.
print(ana | nika)
print('Enebi romlebic 1ma mainc icis: ' , ana.union(nika))

# 2. ენები, რომლებიც ორივემ იცის.
print(ana & nika)
print('Enebi romebic orivem icis: ', ana.intersection(nika))

# 3. ენები, რომლებიც იცის მხოლოდ ანამ.
print(ana - nika)
print('Enebi romlebic icis mxolod anam: ' , ana.difference(nika))

print(ana ^ nika)
print('Enebi romlebic mxolod ertma icis: ' , ana.symmetric_difference(nika))

# ---

# ## ამოცანა 3. კენჭისყრა

# მოცემულია სია, რომელშიც ჩაწერილია, ვის მისცა ხმა სტუდენტებმა:

# ```python
# votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']
# ```
votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']
# 1. შექმენით ცარიელი ლექსიკონი და ციკლით შეავსეთ ისე, რომ გასაღები იყოს სახელი, მნიშვნელობა კი ამ სახელზე მიცემული ხმების რაოდენობა.
vote_count = {}

for name in votes:
    if name in vote_count:
        vote_count[name] += 1
    else:
        vote_count[name] = 1
# 2. დაბეჭდეთ ყველა კანდიდატი თავისი ხმებით ფორმატით: `Ana: 4`.
for name, count in vote_count.items():
    print('name: count')

# ---

# ## ამოცანა 4. მაღაზიის მარაგი

# მაღაზიის მარაგი ინახება ჩადგმულ ლექსიკონში:

# ```python
# inventory = {
#     'laptop': {'price': 2500, 'quantity': 5},
#     'mouse': {'price': 40, 'quantity': 0},
#     'keyboard': {'price': 120, 'quantity': 12},
#     'monitor': {'price': 800, 'quantity': 0},
# }
# ```
inventory = {
    'laptop': {'price': 2500, 'quantity': 5},
    'mouse': {'price': 40, 'quantity': 0},
    'keyboard': {'price': 120, 'quantity': 12},
    'monitor': {'price': 800, 'quantity': 0},
}
# დაწერეთ კოდი, რომელიც:

# 1. დათვლის მარაგის საერთო ღირებულებას.
total = 0

for product in inventory:
    total += inventory[product]['price'] * inventory[product]['quantity']

print('Maragis saerto girebuleba:', total)
# 2. გამოავლენს პროდუქტებს, რომლებიც ამოიწურა (რაოდენობა `0`), და დაბეჭდავს მათ სახელებს.
print('Amowuruli produqtebi:')

for product, info in inventory.items():
    if info['quantity'] == 0:
        print(product)
# 3. მომხმარებლისგან მიიღებს პროდუქტის სახელს და რაოდენობას. თუ პროდუქტი არსებობს და საკმარისი რაოდენობაა მარაგში, შეამცირებს მარაგს და დაბეჭდავს შეძენის ღირებულებას. სხვა შემთხვევაში დაბეჭდავს შესაბამის შეტყობინებას: `პროდუქტი ვერ მოიძებნა` ან `მარაგი არასაკმარისია`.
product = input('Sheiyvanet produqtis saxeli: ')
amount = int(input('Sheiyvanet produqtis raodenoba: '))

if product not in inventory:
    print('Produqti ver moidzebna')

elif inventory[product]['quantity'] >= amount and amount > 0:
    inventory[product]['quantity'] -= amount

    price = inventory[product]['price'] * amount

    print('Girebuleba:', price)

else:
    print('maragi arasakmarisia')

# ---

# ## ამოცანა 5. Comprehension-ები

# მოცემულია სია:

# ```python
# words = ['python', 'java', 'ai', 'sql', 'go', 'python']
# ```
words = ['python', 'java', 'ai', 'sql', 'go', 'python']
# თითოეული შედეგი მიიღეთ **ერთი comprehension-ით**:

# 1. სია, რომელშიც იქნება 1-დან 10-მდე რიცხვების კვადრატები.
squares = [x**2 for x in range(1, 11)]
print('1-dan 10-mde ricxvebis kvadratebi: ' , squares)
# 2. ლექსიკონი `words` სიიდან: გასაღები არის სიტყვა, მნიშვნელობა კი მისი სიგრძე.
word_lengths = {word: len(word) for word in words}
print('Sityvis sigrdze', word_lengths)
# 3. სეტი, რომელშიც იქნება `words` სიის სიტყვების პირველი ასოები.
first_letters = {word[0] for word in words}

print('Siis sityvebis pirveli asoebi: ' , first_letters)
