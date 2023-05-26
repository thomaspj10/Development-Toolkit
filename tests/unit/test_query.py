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

    def test_01_create_data(self):
        address_with_name = models.Address("Random name")
        address_without_name = models.Address(None)
        
        self.assertEqual(address_with_name.id, 1)
        self.assertEqual(address_with_name.name, "Random name")
        
        self.assertEqual(address_without_name.id, 2)
        self.assertEqual(address_without_name.name, None)

if __name__ == '__main__':
    unittest.main()
