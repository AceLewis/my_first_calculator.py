# test_times_34.py
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


class TestTimes34(unittest.TestCase):

    def test_34_times_0(self):
        self.assertEqual(run_calculator('34', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_1(self):
        self.assertEqual(run_calculator('34', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*1 = 34',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_2(self):
        self.assertEqual(run_calculator('34', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*2 = 68',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_3(self):
        self.assertEqual(run_calculator('34', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*3 = 102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_4(self):
        self.assertEqual(run_calculator('34', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*4 = 136',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_5(self):
        self.assertEqual(run_calculator('34', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*5 = 170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_6(self):
        self.assertEqual(run_calculator('34', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*6 = 204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_7(self):
        self.assertEqual(run_calculator('34', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*7 = 238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_8(self):
        self.assertEqual(run_calculator('34', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*8 = 272',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_9(self):
        self.assertEqual(run_calculator('34', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*9 = 306',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_10(self):
        self.assertEqual(run_calculator('34', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*10 = 340',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_11(self):
        self.assertEqual(run_calculator('34', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*11 = 374',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_12(self):
        self.assertEqual(run_calculator('34', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*12 = 408',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_13(self):
        self.assertEqual(run_calculator('34', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*13 = 442',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_14(self):
        self.assertEqual(run_calculator('34', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*14 = 476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_15(self):
        self.assertEqual(run_calculator('34', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*15 = 510',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_16(self):
        self.assertEqual(run_calculator('34', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*16 = 544',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_17(self):
        self.assertEqual(run_calculator('34', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*17 = 578',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_18(self):
        self.assertEqual(run_calculator('34', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*18 = 612',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_19(self):
        self.assertEqual(run_calculator('34', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*19 = 646',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_20(self):
        self.assertEqual(run_calculator('34', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*20 = 680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_21(self):
        self.assertEqual(run_calculator('34', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*21 = 714',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_22(self):
        self.assertEqual(run_calculator('34', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*22 = 748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_23(self):
        self.assertEqual(run_calculator('34', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*23 = 782',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_24(self):
        self.assertEqual(run_calculator('34', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*24 = 816',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_25(self):
        self.assertEqual(run_calculator('34', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*25 = 850',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_26(self):
        self.assertEqual(run_calculator('34', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*26 = 884',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_27(self):
        self.assertEqual(run_calculator('34', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*27 = 918',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_28(self):
        self.assertEqual(run_calculator('34', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*28 = 952',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_29(self):
        self.assertEqual(run_calculator('34', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*29 = 986',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_30(self):
        self.assertEqual(run_calculator('34', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*30 = 1020',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_31(self):
        self.assertEqual(run_calculator('34', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*31 = 1054',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_32(self):
        self.assertEqual(run_calculator('34', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*32 = 1088',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_33(self):
        self.assertEqual(run_calculator('34', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*33 = 1122',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_34(self):
        self.assertEqual(run_calculator('34', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*34 = 1156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_35(self):
        self.assertEqual(run_calculator('34', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*35 = 1190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_36(self):
        self.assertEqual(run_calculator('34', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*36 = 1224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_37(self):
        self.assertEqual(run_calculator('34', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*37 = 1258',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_38(self):
        self.assertEqual(run_calculator('34', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*38 = 1292',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_39(self):
        self.assertEqual(run_calculator('34', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*39 = 1326',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_40(self):
        self.assertEqual(run_calculator('34', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*40 = 1360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_41(self):
        self.assertEqual(run_calculator('34', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*41 = 1394',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_42(self):
        self.assertEqual(run_calculator('34', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*42 = 1428',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_43(self):
        self.assertEqual(run_calculator('34', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*43 = 1462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_44(self):
        self.assertEqual(run_calculator('34', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*44 = 1496',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_45(self):
        self.assertEqual(run_calculator('34', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*45 = 1530',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_46(self):
        self.assertEqual(run_calculator('34', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*46 = 1564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_47(self):
        self.assertEqual(run_calculator('34', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*47 = 1598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_48(self):
        self.assertEqual(run_calculator('34', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*48 = 1632',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_49(self):
        self.assertEqual(run_calculator('34', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*49 = 1666',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_34_times_50(self):
        self.assertEqual(run_calculator('34', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '34*50 = 1700',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
