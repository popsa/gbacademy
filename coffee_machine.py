
class CoffeeMachine:
    
    def __init__(self, water = 400, milk = 540, coffee = 120, cups = 9, money = 550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.coffee_type = None
        
    def print_state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee) + " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")
        
    def take(self):        
        print("I gave you $" + str(self.money))
        self.money = 0

    def fill(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
                
    def buy(self):
        
        self.coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")    
        if self.coffee_type == "back":
                return
        else:                       
            if self.cups == 0:
                print("Sorry, not enough cups!")
                return                 
            
            if self.coffee_type == "1":            
                if self.water < 250:
                    print("Sorry, not enough water!")
                    return
            
                if self.coffee < 16:
                    print("Sorry, not enough coffee!")
                    return
            
                self.water -= 250
                self.coffee -= 16
                self.money += 4
            
            elif self.coffee_type == "2":
            
                if self.water < 350:
                    print("Sorry, not enough water!")
                    return
            
                if self.coffee < 20:
                    print("Sorry, not enough coffee!")
                    return
                
                if self.milk < 75:
                    print("Sorry, not enough milk!")
                    return
            
                self.water -= 350
                self.coffee -= 20
                self.milk -= 75
                self.money += 7
                
            elif self.coffee_type == "3":
            
                if self.water < 200:
                    print("Sorry, not enough water!")
                    return
            
                if self.coffee < 12:
                    print("Sorry, not enough coffee!")
                    return
                
                if self.milk < 100:
                    print("Sorry, not enough milk!")
                    return
                
                self.water -= 200        
                self.coffee -= 12
                self.milk -= 100
                self.money += 6    
        
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
                
    def run(self):
        action = input("Write action (buy, fill, take, remaining, exit):")
        while action != "exit":
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill(int(input("Write how many ml of water do you want to add:")), 
                            int(input("Write how many ml of milk do you want to add:")), 
                            int(input("Write how many grams of coffee beans do you want to add:")), 
                            int(input("Write how many disposable cups of coffee do you want to add:")))
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_state()            
            else:
                print("Action " + action + " not supported")        
                break
            
            action = input("Write action (buy, fill, take, remaining, exit):")
    
                    
machine = CoffeeMachine()
machine.run()
