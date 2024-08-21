
(input("Привіт! Я - перша програма Роми, яка хоче тобі допомогти з рецептами.\nЗараз я напішу тобі список рецептів, а ти напишеш що тобі сподобається.\nНатисни Ентер, якщо зрозумів правила:)\n"))
#Так і треба, я хочу, щоб кнопкою підтверджувався наступний крок, але не знайшов
#як змусити її реагувати тільки на Ентер
  
strava = (input("Біляші\nПіца\nПюре\nХліб\n"))
strava = strava.strip().lower().capitalize()

match strava:
    case "Піца": 
        with open('pizza_recipe.txt', 'r') as pizza:
            pizza_recipe = pizza.read()
            print(pizza_recipe)
            pizza.close()

    case "Біляші":
        with open('bilyash_recipe.txt', 'r') as bilyash:
            bilyash_recipe = bilyash.read()
            print(bilyash_recipe)
            bilyash.close()

    case "Пюре": 
        with open('potatoe_recipe.txt', 'r') as potatoe:
            potatoe_recipe = potatoe.read()
            print(potatoe_recipe)
            potatoe.close()

    case "Хліб": 
        with open('bread_recipe.txt', 'r') as bread:
            bread_recipe = bread.read()
            print(bread_recipe)
            bread.close()
    case _:
        print("Щось пішло не так, давай спробуємо ще раз")

question = input("Приготуємо щось ще? ('Так' або 'Ні')")
question = question.strip().lower().capitalize()

if question == "Так":
    strava = (input("Біляші\nПіца\nПюре\nХліб\n"))
    match strava:
        case "Піца": 
            with open('pizza_recipe.txt', 'r') as pizza:
                pizza_recipe = pizza.read()
                print(pizza_recipe)
                pizza.close()

        case "Біляші":
            with open('bilyash_recipe.txt', 'r') as bilyash:
                bilyash_recipe = bilyash.read()
                print(bilyash_recipe)
                bilyash.close()

        case "Пюре": 
            with open('potatoe_recipe.txt', 'r') as potatoe:
                potatoe_recipe = potatoe.read()
                print(potatoe_recipe)
                potatoe.close()

        case "Хліб": 
            with open('bread_recipe.txt', 'r') as bread:
                bread_recipe = bread.read()
                print(bread_recipe)
                bread.close()

        case _:
            print("Щось пішло не так, давай спробуємо ще раз")
            
else:
    print("ну давай тоді")
    
#Але воно повторюється тільки один раз, там мабуть треба буде якусь рекурсію зробити чи щось таке...
