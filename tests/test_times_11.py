# test_times_11.py
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


class TestTimes11(unittest.TestCase):

    def test_11_times_0(self):
        self.assertEqual(run_calculator('11', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_1(self):
        self.assertEqual(run_calculator('11', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*1 = 11',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_2(self):
        self.assertEqual(run_calculator('11', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*2 = 22',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_3(self):
        self.assertEqual(run_calculator('11', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*3 = 33',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_4(self):
        self.assertEqual(run_calculator('11', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*4 = 44',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_5(self):
        self.assertEqual(run_calculator('11', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*5 = 55',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_6(self):
        self.assertEqual(run_calculator('11', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*6 = 66',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_7(self):
        self.assertEqual(run_calculator('11', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*7 = 77',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_8(self):
        self.assertEqual(run_calculator('11', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*8 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_9(self):
        self.assertEqual(run_calculator('11', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*9 = 99',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_10(self):
        self.assertEqual(run_calculator('11', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*10 = 110',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_11(self):
        self.assertEqual(run_calculator('11', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*11 = 121',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_12(self):
        self.assertEqual(run_calculator('11', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*12 = 132',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_13(self):
        self.assertEqual(run_calculator('11', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*13 = 143',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_14(self):
        self.assertEqual(run_calculator('11', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*14 = 154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_15(self):
        self.assertEqual(run_calculator('11', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*15 = 165',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_16(self):
        self.assertEqual(run_calculator('11', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*16 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_17(self):
        self.assertEqual(run_calculator('11', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*17 = 187',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_18(self):
        self.assertEqual(run_calculator('11', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*18 = 198',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_19(self):
        self.assertEqual(run_calculator('11', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*19 = 209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_20(self):
        self.assertEqual(run_calculator('11', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*20 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_21(self):
        self.assertEqual(run_calculator('11', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*21 = 231',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_22(self):
        self.assertEqual(run_calculator('11', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*22 = 242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_23(self):
        self.assertEqual(run_calculator('11', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*23 = 253',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_24(self):
        self.assertEqual(run_calculator('11', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*24 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_25(self):
        self.assertEqual(run_calculator('11', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*25 = 275',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_26(self):
        self.assertEqual(run_calculator('11', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*26 = 286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_27(self):
        self.assertEqual(run_calculator('11', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*27 = 297',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_28(self):
        self.assertEqual(run_calculator('11', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*28 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_29(self):
        self.assertEqual(run_calculator('11', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*29 = 319',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_30(self):
        self.assertEqual(run_calculator('11', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*30 = 330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_31(self):
        self.assertEqual(run_calculator('11', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*31 = 341',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_32(self):
        self.assertEqual(run_calculator('11', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*32 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_33(self):
        self.assertEqual(run_calculator('11', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*33 = 363',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_34(self):
        self.assertEqual(run_calculator('11', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*34 = 374',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_35(self):
        self.assertEqual(run_calculator('11', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*35 = 385',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_36(self):
        self.assertEqual(run_calculator('11', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*36 = 396',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_37(self):
        self.assertEqual(run_calculator('11', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*37 = 407',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_38(self):
        self.assertEqual(run_calculator('11', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*38 = 418',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_39(self):
        self.assertEqual(run_calculator('11', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*39 = 429',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_40(self):
        self.assertEqual(run_calculator('11', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*40 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_41(self):
        self.assertEqual(run_calculator('11', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*41 = 451',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_42(self):
        self.assertEqual(run_calculator('11', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*42 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_43(self):
        self.assertEqual(run_calculator('11', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*43 = 473',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_44(self):
        self.assertEqual(run_calculator('11', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*44 = 484',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_45(self):
        self.assertEqual(run_calculator('11', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*45 = 495',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_46(self):
        self.assertEqual(run_calculator('11', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*46 = 506',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_47(self):
        self.assertEqual(run_calculator('11', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*47 = 517',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_48(self):
        self.assertEqual(run_calculator('11', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*48 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_49(self):
        self.assertEqual(run_calculator('11', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*49 = 539',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_11_times_50(self):
        self.assertEqual(run_calculator('11', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '11*50 = 550',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
