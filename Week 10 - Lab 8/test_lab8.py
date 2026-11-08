from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier
from inventory import Inventory
from OrderLine import Order, OrderLine

# # Part 2 Test Code
# print("PART 2 TEST CODE")
# supplier_physical = Supplier("S201", "Physical Supplier", "sup_physical@email.com")
# supplier_digital = Supplier("S202", "Digital Supplier", "sup_digital@email.com")

# phys = PhysicalProduct("P201", "Phy Test2", 1000, 10, 50.5, supplier_physical)
# digi = DigitalProduct("P202", "Digi Test2", 20, 2, 25.0, supplier_digital)

# print("Supplier Objects")
# phys.supplier.display_information()
# print("")
# digi.supplier.display_information()
# print("")
# print("Product Objects")
# phys.display_information()
# digi.display_information()

# # Part 3 Test Code
# print("PART 3 TEST CODE")
# inv_A = Inventory()
# inv_B = Inventory()

# supplier_physical = Supplier("S301", "Physical Supplier", "sup_physical@email.com")
# phys = PhysicalProduct("P301", "Phy Test3", 1000, 10, 50.5, supplier_physical)

# inv_A.add_product(phys)
# inv_A.remove_product("P301")
# phys.display_information()
# inv_B.add_product(phys)

# Part 4 Test Code
# supplier_physical = Supplier("S401", "Physical Supplier", "sup_physical@email.com")
# supplier_digital = Supplier("S402", "Digital Supplier", "sup_digital@email.com")

# phys = PhysicalProduct("P401", "Phy Test4", 1000, 10, 50.5, supplier_physical)
# digi = DigitalProduct("P402", "Digi Test4", 20, 2, 25.0, supplier_digital)

# order1 = Order("O401")
# order1.add_order_line(phys, 5)
# order1.add_order_line(digi, 1)

# print(f"Details for Order: {order1.order_id}")
# print(f"Total Cost: {order1.calculate_total()}")

# order2 = Order("O402")
# order2.add_order_line(phys, 1)
# print(f"Details for Order: {order2.order_id}")
# print(f"Total Cost: {order2.calculate_total()}")


# Part 6 Test Code
# print("PART 6 TEST CODE")
# sup = Supplier("S100", "SupTest", "sup@email.com")
# phys = PhysicalProduct("P100", "Test", 1000, 10, 50.5, sup)
# digi = DigitalProduct("P200", "Digi_Test", 20, 2, 25.0, sup)

# inv = Inventory()
# inv.show_product_details(phys)
# inv.show_product_details(digi)


# print("")

# # Part 7 Test Code
# print("PART 7 TEST CODE")
# inv.add_product(phys)
# inv.add_product(digi)

# for product in inv.get_inventory():
#     product.display_information()
#     product.get_fulfilment_info()