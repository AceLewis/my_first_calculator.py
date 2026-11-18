# test_times_33.py
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


class TestTimes33(unittest.TestCase):

    def test_33_times_0(self):
        self.assertEqual(run_calculator('33', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_1(self):
        self.assertEqual(run_calculator('33', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*1 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_2(self):
        self.assertEqual(run_calculator('33', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*2 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_3(self):
        self.assertEqual(run_calculator('33', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*3 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_4(self):
        self.assertEqual(run_calculator('33', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*4 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_5(self):
        self.assertEqual(run_calculator('33', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*5 = 165',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_6(self):
        self.assertEqual(run_calculator('33', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*6 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_7(self):
        self.assertEqual(run_calculator('33', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*7 = 231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_8(self):
        self.assertEqual(run_calculator('33', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*8 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_9(self):
        self.assertEqual(run_calculator('33', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*9 = 297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_10(self):
        self.assertEqual(run_calculator('33', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*10 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_11(self):
        self.assertEqual(run_calculator('33', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*11 = 363',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_12(self):
        self.assertEqual(run_calculator('33', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*12 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_13(self):
        self.assertEqual(run_calculator('33', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*13 = 429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_14(self):
        self.assertEqual(run_calculator('33', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*14 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_15(self):
        self.assertEqual(run_calculator('33', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*15 = 495',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_16(self):
        self.assertEqual(run_calculator('33', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*16 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_17(self):
        self.assertEqual(run_calculator('33', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*17 = 561',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_18(self):
        self.assertEqual(run_calculator('33', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*18 = 594',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_19(self):
        self.assertEqual(run_calculator('33', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*19 = 627',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_20(self):
        self.assertEqual(run_calculator('33', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*20 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_21(self):
        self.assertEqual(run_calculator('33', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*21 = 693',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_22(self):
        self.assertEqual(run_calculator('33', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*22 = 726',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_23(self):
        self.assertEqual(run_calculator('33', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*23 = 759',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_24(self):
        self.assertEqual(run_calculator('33', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*24 = 792',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_25(self):
        self.assertEqual(run_calculator('33', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*25 = 825',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_26(self):
        self.assertEqual(run_calculator('33', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*26 = 858',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_27(self):
        self.assertEqual(run_calculator('33', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*27 = 891',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_28(self):
        self.assertEqual(run_calculator('33', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*28 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_29(self):
        self.assertEqual(run_calculator('33', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*29 = 957',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_30(self):
        self.assertEqual(run_calculator('33', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*30 = 990',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_31(self):
        self.assertEqual(run_calculator('33', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*31 = 1023',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_32(self):
        self.assertEqual(run_calculator('33', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*32 = 1056',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_33(self):
        self.assertEqual(run_calculator('33', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*33 = 1089',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_34(self):
        self.assertEqual(run_calculator('33', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*34 = 1122',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_35(self):
        self.assertEqual(run_calculator('33', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*35 = 1155',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_36(self):
        self.assertEqual(run_calculator('33', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*36 = 1188',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_37(self):
        self.assertEqual(run_calculator('33', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*37 = 1221',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_38(self):
        self.assertEqual(run_calculator('33', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*38 = 1254',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_39(self):
        self.assertEqual(run_calculator('33', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*39 = 1287',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_40(self):
        self.assertEqual(run_calculator('33', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*40 = 1320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_41(self):
        self.assertEqual(run_calculator('33', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*41 = 1353',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_42(self):
        self.assertEqual(run_calculator('33', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*42 = 1386',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_43(self):
        self.assertEqual(run_calculator('33', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*43 = 1419',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_44(self):
        self.assertEqual(run_calculator('33', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*44 = 1452',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_45(self):
        self.assertEqual(run_calculator('33', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*45 = 1485',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_46(self):
        self.assertEqual(run_calculator('33', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*46 = 1518',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_47(self):
        self.assertEqual(run_calculator('33', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*47 = 1551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_48(self):
        self.assertEqual(run_calculator('33', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*48 = 1584',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_49(self):
        self.assertEqual(run_calculator('33', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*49 = 1617',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_33_times_50(self):
        self.assertEqual(run_calculator('33', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '33*50 = 1650',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
