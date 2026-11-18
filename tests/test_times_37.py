# test_times_37.py
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


class TestTimes37(unittest.TestCase):

    def test_37_times_0(self):
        self.assertEqual(run_calculator('37', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_1(self):
        self.assertEqual(run_calculator('37', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*1 = 37',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_2(self):
        self.assertEqual(run_calculator('37', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*2 = 74',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_3(self):
        self.assertEqual(run_calculator('37', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*3 = 111',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_4(self):
        self.assertEqual(run_calculator('37', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*4 = 148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_5(self):
        self.assertEqual(run_calculator('37', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*5 = 185',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_6(self):
        self.assertEqual(run_calculator('37', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*6 = 222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_7(self):
        self.assertEqual(run_calculator('37', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*7 = 259',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_8(self):
        self.assertEqual(run_calculator('37', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*8 = 296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_9(self):
        self.assertEqual(run_calculator('37', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*9 = 333',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_10(self):
        self.assertEqual(run_calculator('37', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*10 = 370',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_11(self):
        self.assertEqual(run_calculator('37', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*11 = 407',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_12(self):
        self.assertEqual(run_calculator('37', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*12 = 444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_13(self):
        self.assertEqual(run_calculator('37', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*13 = 481',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_14(self):
        self.assertEqual(run_calculator('37', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*14 = 518',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_15(self):
        self.assertEqual(run_calculator('37', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*15 = 555',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_16(self):
        self.assertEqual(run_calculator('37', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*16 = 592',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_17(self):
        self.assertEqual(run_calculator('37', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*17 = 629',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_18(self):
        self.assertEqual(run_calculator('37', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*18 = 666',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_19(self):
        self.assertEqual(run_calculator('37', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*19 = 703',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_20(self):
        self.assertEqual(run_calculator('37', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*20 = 740',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_21(self):
        self.assertEqual(run_calculator('37', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*21 = 777',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_22(self):
        self.assertEqual(run_calculator('37', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*22 = 814',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_23(self):
        self.assertEqual(run_calculator('37', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*23 = 851',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_24(self):
        self.assertEqual(run_calculator('37', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*24 = 888',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_25(self):
        self.assertEqual(run_calculator('37', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*25 = 925',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_26(self):
        self.assertEqual(run_calculator('37', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*26 = 962',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_27(self):
        self.assertEqual(run_calculator('37', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*27 = 999',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_28(self):
        self.assertEqual(run_calculator('37', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*28 = 1036',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_29(self):
        self.assertEqual(run_calculator('37', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*29 = 1073',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_30(self):
        self.assertEqual(run_calculator('37', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*30 = 1110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_31(self):
        self.assertEqual(run_calculator('37', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*31 = 1147',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_32(self):
        self.assertEqual(run_calculator('37', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*32 = 1184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_33(self):
        self.assertEqual(run_calculator('37', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*33 = 1221',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_34(self):
        self.assertEqual(run_calculator('37', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*34 = 1258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_35(self):
        self.assertEqual(run_calculator('37', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*35 = 1295',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_36(self):
        self.assertEqual(run_calculator('37', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*36 = 1332',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_37(self):
        self.assertEqual(run_calculator('37', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*37 = 1369',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_38(self):
        self.assertEqual(run_calculator('37', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*38 = 1406',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_39(self):
        self.assertEqual(run_calculator('37', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*39 = 1443',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_40(self):
        self.assertEqual(run_calculator('37', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*40 = 1480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_41(self):
        self.assertEqual(run_calculator('37', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*41 = 1517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_42(self):
        self.assertEqual(run_calculator('37', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*42 = 1554',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_43(self):
        self.assertEqual(run_calculator('37', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*43 = 1591',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_44(self):
        self.assertEqual(run_calculator('37', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*44 = 1628',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_45(self):
        self.assertEqual(run_calculator('37', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*45 = 1665',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_46(self):
        self.assertEqual(run_calculator('37', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*46 = 1702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_47(self):
        self.assertEqual(run_calculator('37', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*47 = 1739',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_48(self):
        self.assertEqual(run_calculator('37', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*48 = 1776',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_49(self):
        self.assertEqual(run_calculator('37', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*49 = 1813',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_37_times_50(self):
        self.assertEqual(run_calculator('37', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '37*50 = 1850',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
