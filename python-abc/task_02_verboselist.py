#!/usr/bin/python3


class VerboseList(list):
    def append(self, obj):
        super().append(obj)
        print(f"Added [{obj}] to the list.")

    def extend(self, nb):
        super().extend(nb)
        print(f"Extended the list with [{nb}] items.")

    def remove(self, obj):
        print(f"Removed [{obj}] from the list.")
        super().remove(obj)

    def pop(self, obj):
        print(f"Popped [{obj}] from the list.")
        super().append(obj)