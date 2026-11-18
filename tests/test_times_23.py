# test_times_23.py
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


class TestTimes23(unittest.TestCase):

    def test_23_times_0(self):
        self.assertEqual(run_calculator('23', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_1(self):
        self.assertEqual(run_calculator('23', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*1 = 23',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_2(self):
        self.assertEqual(run_calculator('23', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*2 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_3(self):
        self.assertEqual(run_calculator('23', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*3 = 69',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_4(self):
        self.assertEqual(run_calculator('23', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*4 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_5(self):
        self.assertEqual(run_calculator('23', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*5 = 115',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_6(self):
        self.assertEqual(run_calculator('23', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*6 = 138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_7(self):
        self.assertEqual(run_calculator('23', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*7 = 161',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_8(self):
        self.assertEqual(run_calculator('23', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*8 = 184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_9(self):
        self.assertEqual(run_calculator('23', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*9 = 207',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_10(self):
        self.assertEqual(run_calculator('23', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*10 = 230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_11(self):
        self.assertEqual(run_calculator('23', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*11 = 253',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_12(self):
        self.assertEqual(run_calculator('23', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*12 = 276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_13(self):
        self.assertEqual(run_calculator('23', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*13 = 299',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_14(self):
        self.assertEqual(run_calculator('23', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*14 = 322',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_15(self):
        self.assertEqual(run_calculator('23', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*15 = 345',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_16(self):
        self.assertEqual(run_calculator('23', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*16 = 368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_17(self):
        self.assertEqual(run_calculator('23', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*17 = 391',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_18(self):
        self.assertEqual(run_calculator('23', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*18 = 414',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_19(self):
        self.assertEqual(run_calculator('23', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*19 = 437',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_20(self):
        self.assertEqual(run_calculator('23', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*20 = 460',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_21(self):
        self.assertEqual(run_calculator('23', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*21 = 483',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_22(self):
        self.assertEqual(run_calculator('23', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*22 = 506',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_23(self):
        self.assertEqual(run_calculator('23', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*23 = 529',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_24(self):
        self.assertEqual(run_calculator('23', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*24 = 552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_25(self):
        self.assertEqual(run_calculator('23', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*25 = 575',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_26(self):
        self.assertEqual(run_calculator('23', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*26 = 598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_27(self):
        self.assertEqual(run_calculator('23', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*27 = 621',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_28(self):
        self.assertEqual(run_calculator('23', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*28 = 644',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_29(self):
        self.assertEqual(run_calculator('23', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*29 = 667',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_30(self):
        self.assertEqual(run_calculator('23', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*30 = 690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_31(self):
        self.assertEqual(run_calculator('23', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*31 = 713',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_32(self):
        self.assertEqual(run_calculator('23', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*32 = 736',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_33(self):
        self.assertEqual(run_calculator('23', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*33 = 759',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_34(self):
        self.assertEqual(run_calculator('23', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*34 = 782',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_35(self):
        self.assertEqual(run_calculator('23', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*35 = 805',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_36(self):
        self.assertEqual(run_calculator('23', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*36 = 828',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_37(self):
        self.assertEqual(run_calculator('23', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*37 = 851',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_38(self):
        self.assertEqual(run_calculator('23', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*38 = 874',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_39(self):
        self.assertEqual(run_calculator('23', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*39 = 897',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_40(self):
        self.assertEqual(run_calculator('23', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*40 = 920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_41(self):
        self.assertEqual(run_calculator('23', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*41 = 943',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_42(self):
        self.assertEqual(run_calculator('23', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*42 = 966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_43(self):
        self.assertEqual(run_calculator('23', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*43 = 989',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_44(self):
        self.assertEqual(run_calculator('23', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*44 = 1012',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_45(self):
        self.assertEqual(run_calculator('23', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*45 = 1035',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_46(self):
        self.assertEqual(run_calculator('23', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*46 = 1058',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_47(self):
        self.assertEqual(run_calculator('23', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*47 = 1081',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_48(self):
        self.assertEqual(run_calculator('23', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*48 = 1104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_49(self):
        self.assertEqual(run_calculator('23', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*49 = 1127',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_23_times_50(self):
        self.assertEqual(run_calculator('23', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '23*50 = 1150',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
