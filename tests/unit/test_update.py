import unittest

import devkit.sql as sql
import models
import os

DB_FILE = "test.db"

class TestUpdateQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(DB_FILE):
            os.remove(DB_FILE)

        sql.set_sqlite_file(DB_FILE)
        sql.execute("drop table if exists Address")
        sql.execute("create table Address (id integer primary key autoincrement, name varchar(255))")
    
    @classmethod
    def tearDownClass(cls):
        sql.close_connection()
        os.remove(DB_FILE)

    def test_01_create_data(self):
        address_with_name = models.Address("Random name")
        address_without_name = models.Address(None)
        address_with_name_2 = models.Address("Another random name")
        
        self.assertEqual(address_with_name.id, 1)
        self.assertEqual(address_with_name.name, "Random name")
        
        self.assertEqual(address_without_name.id, 2)
        self.assertEqual(address_without_name.name, None)

        self.assertEqual(address_with_name_2.id, 3)
        self.assertEqual(address_with_name_2.name, "Another random name")

    def test_02_update_conditional(self):
        sql.update(models.ADDRESS).set(models.ADDRESS.NAME, "New name!").where(models.ADDRESS.ID.eq(1)).execute()

        updated_address_1 = models.Address.find_by_id(1)
        self.assertNotEqual(updated_address_1, None)
        if updated_address_1 != None:
            self.assertEqual(updated_address_1.name, "New name!")

        sql.update(models.ADDRESS).set(models.ADDRESS.NAME, "New name!!!").where(models.ADDRESS.NAME.eq("New name!")).execute()

        updated_address_2 = models.Address.find_by_id(1)
        self.assertNotEqual(updated_address_2, None)
        if updated_address_2 != None:
            self.assertEqual(updated_address_2.name, "New name!!!")

    def test_03_update(self):
        sql.update(models.ADDRESS).set(models.ADDRESS.NAME, "@everyone").execute()

        for address in models.Address.find_all():
            self.assertEqual(address.name, "@everyone")

    def test_04_nothing_to_update(self):
        sql.update(models.ADDRESS).set(models.ADDRESS.NAME, "@everyone!!!!!!!").where(models.ADDRESS.ID.gt(3)).execute()

        for address in models.Address.find_all():
            self.assertEqual(address.name, "@everyone")

        address = models.Address.find_by_id(1)
        self.assertNotEqual(address, None)
        if address != None:
            address.delete()

        sql.update(models.ADDRESS).set(models.ADDRESS.NAME, "@here").where(models.ADDRESS.ID.eq(1)).execute()

        for address in models.Address.find_all():
            self.assertEqual(address.name, "@everyone")

if __name__ == '__main__':
    unittest.main()
