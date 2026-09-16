inventory = {
    "iphone": {"full_name": "iphone_duo", "price":1999.99, "quantity":11},
    "cdj": {"full_name": "cdj_3000x", "price":2999.00, "quantity": 15},
    "usb": {"full_name": "sandisk_usb_2_set","price": 40.00, "quantity": 12},
    "djm": {"full_name": "djm_900nxs2_mixer","price": 2850.00, "quantity":15}
}

def display_full_inventory():
    print("\n" + "=" * 40)
    print("          Full Inventory")
    print( "=" * 40)


    if not inventory:
        print("Nothing in inventory yet.")
        return

    item_total_value = 0.00
    inventory_total_value = 0.00

    for item, info in inventory.items():
        print(f"\n\033[1;4m{info["full_name"]}\033[0m")
        print(f"price: ${info["price"]}")
        print(f"quantity: {info["quantity"]}")
        item_total_value = info["price"] * info["quantity"]
        print(f"item total = {item_total_value:.2f}")
        inventory_total_value += item_total_value
        
    print(f"\nTotal Value of Inventory:  {inventory_total_value}")
    print( "=" * 40)


display_full_inventory()


search = input("\nWhich item would you like to look up: ").lower()
item = inventory.get(search)

if search in inventory:
    print(f"\nFound:  {item['full_name']}")
    print(f"Price:  {item['price']}")
    print(f"Quantity:  {item['quantity']}")
else:
    print(f"No item found for {search}")

while True:
#To allow the user to update the quantity of a product
    print("\n--- Update Item Quantity ---")
    item_for_quantity_update = input("Which item would you like to update the quantity for:  ").lower()

    if item_for_quantity_update in inventory:
        break
    else:
        print(f"'{item_for_quantity_update}' is not a valid item. Please try again.")


item_detail_dictionary = inventory.get(item_for_quantity_update)

if item_for_quantity_update in inventory:
    print(f"We have {item_detail_dictionary['quantity']} {item_for_quantity_update}'s in stock right now.")
    user_update_int=input(f"\nBy how much would you like to update the {item_for_quantity_update}'s count by"\
          "(postive number for number restocked or negative number for products sold):  ")

    try:
        value = int(user_update_int)
        item_detail_dictionary['quantity']+= value
        print(f"{item_for_quantity_update}'s quantity has been updated to {item_detail_dictionary['quantity']}")
    except ValueError:
        print(f"You must input an integer.")


low_stock = set()

for item, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(item)

if low_stock:
    message = ", ".join(low_stock)
    print(f"\n{message} are low on stock, please restock that/those items!")
    