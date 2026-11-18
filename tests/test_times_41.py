# test_times_41.py
# Every single case gets its own test, to be true to the story

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

SOURCE = Path(__file__).parent.parent / 'my_first_calculator.py'
CODE = compile(SOURCE.read_text(), str(SOURCE), 'exec')


def run_calculator(num1, sign, num2):
    answers = iter([num1, sign, num2])
    out = io.StringIO()
    with mock.patch('builtins.input', lambda prompt='': next(answers)), redirect_stdout(out):
        exec(CODE, {'__name__': '__main__'})
    return out.getvalue().splitlines()


class TestTimes41(unittest.TestCase):

    def test_41_times_0(self):
        self.assertEqual(run_calculator('41', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_1(self):
        self.assertEqual(run_calculator('41', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*1 = 41',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_2(self):
        self.assertEqual(run_calculator('41', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*2 = 82',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_3(self):
        self.assertEqual(run_calculator('41', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*3 = 123',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_4(self):
        self.assertEqual(run_calculator('41', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*4 = 164',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_5(self):
        self.assertEqual(run_calculator('41', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*5 = 205',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_6(self):
        self.assertEqual(run_calculator('41', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*6 = 246',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_7(self):
        self.assertEqual(run_calculator('41', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*7 = 287',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_8(self):
        self.assertEqual(run_calculator('41', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*8 = 328',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_9(self):
        self.assertEqual(run_calculator('41', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*9 = 369',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_10(self):
        self.assertEqual(run_calculator('41', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*10 = 410',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_11(self):
        self.assertEqual(run_calculator('41', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*11 = 451',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_12(self):
        self.assertEqual(run_calculator('41', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*12 = 492',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_13(self):
        self.assertEqual(run_calculator('41', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*13 = 533',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_14(self):
        self.assertEqual(run_calculator('41', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*14 = 574',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_15(self):
        self.assertEqual(run_calculator('41', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*15 = 615',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_16(self):
        self.assertEqual(run_calculator('41', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*16 = 656',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_17(self):
        self.assertEqual(run_calculator('41', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*17 = 697',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_18(self):
        self.assertEqual(run_calculator('41', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*18 = 738',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_19(self):
        self.assertEqual(run_calculator('41', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*19 = 779',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_20(self):
        self.assertEqual(run_calculator('41', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*20 = 820',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_21(self):
        self.assertEqual(run_calculator('41', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*21 = 861',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_22(self):
        self.assertEqual(run_calculator('41', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*22 = 902',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_23(self):
        self.assertEqual(run_calculator('41', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*23 = 943',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_24(self):
        self.assertEqual(run_calculator('41', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*24 = 984',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_25(self):
        self.assertEqual(run_calculator('41', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*25 = 1025',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_26(self):
        self.assertEqual(run_calculator('41', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*26 = 1066',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_27(self):
        self.assertEqual(run_calculator('41', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*27 = 1107',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_28(self):
        self.assertEqual(run_calculator('41', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*28 = 1148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_29(self):
        self.assertEqual(run_calculator('41', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*29 = 1189',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_30(self):
        self.assertEqual(run_calculator('41', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*30 = 1230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_31(self):
        self.assertEqual(run_calculator('41', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*31 = 1271',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_32(self):
        self.assertEqual(run_calculator('41', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*32 = 1312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_33(self):
        self.assertEqual(run_calculator('41', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*33 = 1353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_34(self):
        self.assertEqual(run_calculator('41', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*34 = 1394',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_35(self):
        self.assertEqual(run_calculator('41', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*35 = 1435',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_36(self):
        self.assertEqual(run_calculator('41', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*36 = 1476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_37(self):
        self.assertEqual(run_calculator('41', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*37 = 1517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_38(self):
        self.assertEqual(run_calculator('41', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*38 = 1558',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_39(self):
        self.assertEqual(run_calculator('41', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*39 = 1599',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_40(self):
        self.assertEqual(run_calculator('41', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*40 = 1640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_41(self):
        self.assertEqual(run_calculator('41', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*41 = 1681',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_42(self):
        self.assertEqual(run_calculator('41', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*42 = 1722',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_43(self):
        self.assertEqual(run_calculator('41', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*43 = 1763',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_44(self):
        self.assertEqual(run_calculator('41', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*44 = 1804',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_45(self):
        self.assertEqual(run_calculator('41', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*45 = 1845',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_46(self):
        self.assertEqual(run_calculator('41', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*46 = 1886',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_47(self):
        self.assertEqual(run_calculator('41', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*47 = 1927',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_48(self):
        self.assertEqual(run_calculator('41', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*48 = 1968',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_49(self):
        self.assertEqual(run_calculator('41', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*49 = 2009',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_41_times_50(self):
        self.assertEqual(run_calculator('41', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '41*50 = 2050',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
