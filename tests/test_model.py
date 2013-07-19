import gtk
import unittest
import copy

from rdc.model import RdpSettingsReader, RdpSettingsWriter, create_liststore

mock_file_content = ["abc:def:123:456",
                    "zxy:ttt:098:765",
                    "iii:ooo::",
                    ]

parsed_file = [ ["abc", "def", "123", "456"],
                ["zxy", "ttt", "098", "765"],
                ["iii", "ooo", "", ""],
              ]

class TestModel(unittest.TestCase):
    def test_populate_liststore(self):
        rdp_settings = RdpSettingsReader(mock_file_content)
        liststore = create_liststore()
        liststore = rdp_settings.populate_liststore(liststore)
        iter = liststore.get_iter_first()
        expected_liststore_values = parsed_file

        # compare liststore to expected_values
        for expected_values in expected_liststore_values:
            self.assertTrue(iter is not None, "Expected more items in liststore")

            i = 0
            for expected_value in expected_values:
                value = liststore.get_value(iter, i)
                self.assertEquals(expected_value, value)
                i += 1

            iter = liststore.iter_next(iter)

    def test_save_file(self):
        fake_vals1 = ["1234", "5678", "abcd", "qwez"]
        fake_vals2 = ["a", "z", "", ""]

        liststore = create_liststore()

        liststore.append(fake_vals1)
        liststore.append(fake_vals2)

        rdp_settings_writer = RdpSettingsWriter(liststore)
        expected_file = "%s:%s:%s:%s\n" % tuple(fake_vals1)
        expected_file += "%s:%s:%s:%s" % tuple(fake_vals2)

        out = rdp_settings_writer.__str__()

        self.assertEquals(expected_file, out)
