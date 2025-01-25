def add_item():
    #adding each item to the cart and all items are shown at the checkout
    item=input("Enter the item name: ")
    cost=int(input("Enter the cost of the item"))
    return (item,cost)
    
def items_in_cart(all_items):
    #this is used to display the items present in the cart
    for items in all_items:
        print(items)
    
def total_amount(total_cost):
    #it helps in calculating the total amount and displaying it
    print(f"The total amount is {total_cost}")
    
def main():
    total_cost=0
    all_items=[]
    while True:
        print("Enter 1 to add item")
        print("Enter 2 to check items in cart")
        print("Enter 3 for Total cost")
        choice=int(input("Enter the choice"))
        if choice ==1:
            (single_item,item_cost)=add_item()
            all_items.append(single_item)
            total_cost=total_cost+item_cost
        elif choice == 2:
            items_in_cart(all_items)
        elif choice==3:
            total_amount(total_cost)
        else:
            break
main()