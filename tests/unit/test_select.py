import unittest

import devkit.sql as sql
import models
import os

DB_FILE = "test.db"

class TestSelectQuery(unittest.TestCase):

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

    def test_02_select(self):
        addresses = sql.select(models.ADDRESS).fetch()

        self.assertEqual(len(addresses), 3)
        self.assertEqual(addresses[0].id, 1)
        self.assertEqual(addresses[1].id, 2)
        self.assertEqual(addresses[2].id, 3)

    def test_03_select_conditional(self):
        addresses = sql.select(models.ADDRESS).where(models.ADDRESS.ID.eq(1)).fetch()

        self.assertEqual(len(addresses), 1)
        self.assertEqual(addresses[0].id, 1)

        address = sql.select(models.ADDRESS).where(models.ADDRESS.ID.eq(1)).fetch_one()
        self.assertNotEqual(address, None)

        if address != None:
            self.assertEqual(address.id, 1)

    def test_04_select_conditional_extra(self):
        addresses_1 = sql.select(models.ADDRESS).where(models.ADDRESS.ID.in_([1, 2])).fetch()
        self.assertEqual(len(addresses_1), 2)

        addresses_2 = sql.select(models.ADDRESS).where(models.ADDRESS.ID.gt(2)).fetch()
        self.assertEqual(len(addresses_2), 1)

        addresses_3 = sql.select(models.ADDRESS).where(models.ADDRESS.ID.lt(2)).fetch()
        self.assertEqual(len(addresses_3), 1)

        addresses_4 = sql.select(models.ADDRESS).where(models.ADDRESS.ID.ge(2)).fetch()
        self.assertEqual(len(addresses_4), 2)

        addresses_5 = sql.select(models.ADDRESS).where(models.ADDRESS.ID.le(2)).fetch()
        self.assertEqual(len(addresses_5), 2)

    def test_05_select_limit(self):
        addresses_1 = sql.select(models.ADDRESS).limit(1).fetch()
        self.assertEqual(len(addresses_1), 1)

        addresses_2 = sql.select(models.ADDRESS).limit(2).fetch()
        self.assertEqual(len(addresses_2), 2)

        addresses_3 = sql.select(models.ADDRESS).limit(3).fetch()
        self.assertEqual(len(addresses_3), 3)

if __name__ == '__main__':
    unittest.main()
