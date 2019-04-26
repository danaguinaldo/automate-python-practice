#! python3
# inventory.py - RPG Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def dispalyInventory(inventory):
    print("Inventory:")
    item_total = 0
    for x, y in inventory.items():
        print(str(y) + ' ' + x)
        item_total += y
    print("Total number of items: " + str(item_total) + "\n")

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        if loot in inventory:
            inventory[loot] += 1;
        else:
            inventory[loot] = 1;

def main():
    dispalyInventory(stuff)
    addToInventory(stuff, dragonLoot)
    dispalyInventory(stuff)

main()