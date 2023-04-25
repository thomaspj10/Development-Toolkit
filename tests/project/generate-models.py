from devkit.generators.ext import SqlClassGenerator
from devkit.python_file import python_file
    
with python_file("models.py") as pf:
    pf.add_future_import("annotations")
    
    user_generator = SqlClassGenerator()
    user_generator.set_table("User")
    user_generator.add_column("name", "str")
    user_generator.add_column("address_id", "int")
    user_generator.add_foreign_key("Address", "address_id", False)
    
    address = SqlClassGenerator()
    address.set_table("Address")
    address.add_column("name", "str")
    
    pf.add_generator(user_generator)
    pf.add_generator(address)
