from generators.ext import SqlClassGenerator
from python_file import python_file
    
with python_file("models.py") as pf:
    pf.add_future_import("annotations")
    
    sql_class_generator = SqlClassGenerator()
    sql_class_generator.set_table("User")
    sql_class_generator.add_attribute("name", "str")
    
    pf.add_generator(sql_class_generator)
