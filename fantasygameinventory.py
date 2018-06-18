stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory:dict):
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' +k)
        total += v
    print("Total number of items: " +str(total))

def addToInventory(inventory, addedItems):
    for lootitem in addedItems:
        if lootitem in inventory.keys():
            inventory[lootitem] += 1
        else:
            inventory[lootitem] = 1
    return inventory

displayInventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)