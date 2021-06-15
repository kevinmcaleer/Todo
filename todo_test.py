# Todo test suite
# Kevin McAleer
# June 2021

from todo import Item, Todo, Status, Priority


item1 = Item("Item 1")
item2 = Item("Item 2")
item3 = Item("Item 3")
item1.priority = Priority.HIGH
item2.status = Status.IN_PROGRESS



l = Todo()

l.new_item(item1)
l.new_item(item2)
l.new_item(item3)

l.show()