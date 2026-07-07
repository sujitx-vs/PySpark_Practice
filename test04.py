class LaptopBuilder:

    def __init__(self):
        self.ram = None
        self.storage = None

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return {
            "RAM": self.ram,
            "Storage": self.storage
        }


laptop = (
    LaptopBuilder()
    .set_ram("16GB")
    .set_storage("512GB")
    .build()
)

print(laptop)