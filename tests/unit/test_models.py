import unittest

import devkit.sql as sql
import models
import os

DB_FILE = "test.db"

class TestSimpleModelInteractions(unittest.TestCase):

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

    def test_01_create_models(self):
        address_with_name = models.Address("Random name")
        address_without_name = models.Address(None)
        
        self.assertEqual(address_with_name.id, 1)
        self.assertEqual(address_with_name.name, "Random name")
        
        self.assertEqual(address_without_name.id, 2)
        self.assertEqual(address_without_name.name, None)

    def test_02_fetch_model(self):
        first_model = models.Address.find_by_id(1)
        
        self.assertNotEqual(first_model, None)
        if first_model != None:
            self.assertEqual(first_model.id, 1)
            self.assertEqual(first_model.name, "Random name")
            
        second_model = models.Address.find_by_id(2)
        
        self.assertNotEqual(second_model, None)
        if second_model != None:
            self.assertEqual(second_model.id, 2)
            self.assertEqual(second_model.name, None)
        
    def test_03_fetch_all_models(self):
        all_models = models.Address.find_all()
        
        self.assertEqual(len(all_models), 2)
        
    def test_04_modify_model(self):
        second_model = models.Address.find_by_id(2)
        self.assertNotEqual(second_model, None)
        
        if second_model != None:
            second_model.name = "Another name"
            second_model.store()
            
            second_model_fetch = models.Address.find_by_id(2)
            self.assertNotEqual(second_model_fetch, None)
            if second_model_fetch != None:
                self.assertEqual(second_model_fetch.id, 2)
                self.assertEqual(second_model_fetch.name, "Another name")

    def test_05_delete_model(self):
        first_model = models.Address.find_by_id(1)
        self.assertNotEqual(first_model, None)
        
        if first_model != None:
            first_model.delete()
            
            first_model_fetch = models.Address.find_by_id(1)
            self.assertEqual(first_model_fetch, None)

        all_models = models.Address.find_all()
        self.assertEqual(len(all_models), 1)

    def test_06_create_another_model(self):
        another_address = models.Address("Random name two")
        
        self.assertEqual(another_address.id, 3)
        self.assertEqual(another_address.name, "Random name two")
        
        another_address_fetch = models.Address.find_by_id(3)
        self.assertNotEqual(another_address_fetch, None)
        
        if another_address_fetch != None:
            self.assertEqual(another_address_fetch.id, 3)
            self.assertEqual(another_address_fetch.name, "Random name two")

    def test_07_delete_all_models(self):
        for address in models.Address.find_all():
            address.delete()

        self.assertEqual(len(models.Address.find_all()), 0)

    def test_08_create_new_models(self):
        models.Address("Street!")
        models.Address("I enter fake info")
        models.Address(None)
        models.Address("Another street")

        self.assertEqual(len(models.Address.find_all()), 4)

        self.assertEqual(models.Address.find_all()[0].name, "Street!")
        self.assertEqual(models.Address.find_all()[1].name, "I enter fake info")
        self.assertEqual(models.Address.find_all()[2].name, None)
        self.assertEqual(models.Address.find_all()[3].name, "Another street")

if __name__ == '__main__':
    unittest.main()
