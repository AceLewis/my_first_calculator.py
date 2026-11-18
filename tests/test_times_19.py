# test_times_19.py
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


class TestTimes19(unittest.TestCase):

    def test_19_times_0(self):
        self.assertEqual(run_calculator('19', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_1(self):
        self.assertEqual(run_calculator('19', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*1 = 19',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_2(self):
        self.assertEqual(run_calculator('19', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*2 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_3(self):
        self.assertEqual(run_calculator('19', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*3 = 57',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_4(self):
        self.assertEqual(run_calculator('19', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*4 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_5(self):
        self.assertEqual(run_calculator('19', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*5 = 95',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_6(self):
        self.assertEqual(run_calculator('19', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*6 = 114',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_7(self):
        self.assertEqual(run_calculator('19', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*7 = 133',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_8(self):
        self.assertEqual(run_calculator('19', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*8 = 152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_9(self):
        self.assertEqual(run_calculator('19', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*9 = 171',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_10(self):
        self.assertEqual(run_calculator('19', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*10 = 190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_11(self):
        self.assertEqual(run_calculator('19', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*11 = 209',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_12(self):
        self.assertEqual(run_calculator('19', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*12 = 228',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_13(self):
        self.assertEqual(run_calculator('19', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*13 = 247',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_14(self):
        self.assertEqual(run_calculator('19', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*14 = 266',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_15(self):
        self.assertEqual(run_calculator('19', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*15 = 285',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_16(self):
        self.assertEqual(run_calculator('19', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*16 = 304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_17(self):
        self.assertEqual(run_calculator('19', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*17 = 323',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_18(self):
        self.assertEqual(run_calculator('19', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*18 = 342',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_19(self):
        self.assertEqual(run_calculator('19', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*19 = 361',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_20(self):
        self.assertEqual(run_calculator('19', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*20 = 380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_21(self):
        self.assertEqual(run_calculator('19', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*21 = 399',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_22(self):
        self.assertEqual(run_calculator('19', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*22 = 418',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_23(self):
        self.assertEqual(run_calculator('19', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*23 = 437',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_24(self):
        self.assertEqual(run_calculator('19', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*24 = 456',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_25(self):
        self.assertEqual(run_calculator('19', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*25 = 475',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_26(self):
        self.assertEqual(run_calculator('19', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*26 = 494',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_27(self):
        self.assertEqual(run_calculator('19', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*27 = 513',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_28(self):
        self.assertEqual(run_calculator('19', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*28 = 532',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_29(self):
        self.assertEqual(run_calculator('19', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*29 = 551',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_30(self):
        self.assertEqual(run_calculator('19', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*30 = 570',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_31(self):
        self.assertEqual(run_calculator('19', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*31 = 589',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_32(self):
        self.assertEqual(run_calculator('19', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*32 = 608',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_33(self):
        self.assertEqual(run_calculator('19', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*33 = 627',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_34(self):
        self.assertEqual(run_calculator('19', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*34 = 646',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_35(self):
        self.assertEqual(run_calculator('19', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*35 = 665',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_36(self):
        self.assertEqual(run_calculator('19', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*36 = 684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_37(self):
        self.assertEqual(run_calculator('19', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*37 = 703',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_38(self):
        self.assertEqual(run_calculator('19', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*38 = 722',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_39(self):
        self.assertEqual(run_calculator('19', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*39 = 741',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_40(self):
        self.assertEqual(run_calculator('19', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*40 = 760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_41(self):
        self.assertEqual(run_calculator('19', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*41 = 779',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_42(self):
        self.assertEqual(run_calculator('19', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*42 = 798',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_43(self):
        self.assertEqual(run_calculator('19', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*43 = 817',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_44(self):
        self.assertEqual(run_calculator('19', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*44 = 836',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_45(self):
        self.assertEqual(run_calculator('19', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*45 = 855',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_46(self):
        self.assertEqual(run_calculator('19', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*46 = 874',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_47(self):
        self.assertEqual(run_calculator('19', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*47 = 893',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_48(self):
        self.assertEqual(run_calculator('19', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*48 = 912',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_49(self):
        self.assertEqual(run_calculator('19', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*49 = 931',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_19_times_50(self):
        self.assertEqual(run_calculator('19', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '19*50 = 950',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
