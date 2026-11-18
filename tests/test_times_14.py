# test_times_14.py
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


class TestTimes14(unittest.TestCase):

    def test_14_times_0(self):
        self.assertEqual(run_calculator('14', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_1(self):
        self.assertEqual(run_calculator('14', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*1 = 14',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_2(self):
        self.assertEqual(run_calculator('14', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*2 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_3(self):
        self.assertEqual(run_calculator('14', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*3 = 42',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_4(self):
        self.assertEqual(run_calculator('14', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*4 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_5(self):
        self.assertEqual(run_calculator('14', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*5 = 70',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_6(self):
        self.assertEqual(run_calculator('14', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*6 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_7(self):
        self.assertEqual(run_calculator('14', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*7 = 98',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_8(self):
        self.assertEqual(run_calculator('14', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*8 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_9(self):
        self.assertEqual(run_calculator('14', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*9 = 126',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_10(self):
        self.assertEqual(run_calculator('14', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*10 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_11(self):
        self.assertEqual(run_calculator('14', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*11 = 154',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_12(self):
        self.assertEqual(run_calculator('14', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*12 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_13(self):
        self.assertEqual(run_calculator('14', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*13 = 182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_14(self):
        self.assertEqual(run_calculator('14', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*14 = 196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_15(self):
        self.assertEqual(run_calculator('14', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*15 = 210',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_16(self):
        self.assertEqual(run_calculator('14', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*16 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_17(self):
        self.assertEqual(run_calculator('14', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*17 = 238',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_18(self):
        self.assertEqual(run_calculator('14', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*18 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_19(self):
        self.assertEqual(run_calculator('14', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*19 = 266',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_20(self):
        self.assertEqual(run_calculator('14', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*20 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_21(self):
        self.assertEqual(run_calculator('14', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*21 = 294',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_22(self):
        self.assertEqual(run_calculator('14', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*22 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_23(self):
        self.assertEqual(run_calculator('14', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*23 = 322',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_24(self):
        self.assertEqual(run_calculator('14', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*24 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_25(self):
        self.assertEqual(run_calculator('14', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*25 = 350',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_26(self):
        self.assertEqual(run_calculator('14', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*26 = 364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_27(self):
        self.assertEqual(run_calculator('14', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*27 = 378',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_28(self):
        self.assertEqual(run_calculator('14', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*28 = 392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_29(self):
        self.assertEqual(run_calculator('14', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*29 = 406',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_30(self):
        self.assertEqual(run_calculator('14', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*30 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_31(self):
        self.assertEqual(run_calculator('14', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*31 = 434',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_32(self):
        self.assertEqual(run_calculator('14', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*32 = 448',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_33(self):
        self.assertEqual(run_calculator('14', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*33 = 462',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_34(self):
        self.assertEqual(run_calculator('14', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*34 = 476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_35(self):
        self.assertEqual(run_calculator('14', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*35 = 490',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_36(self):
        self.assertEqual(run_calculator('14', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*36 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_37(self):
        self.assertEqual(run_calculator('14', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*37 = 518',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_38(self):
        self.assertEqual(run_calculator('14', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*38 = 532',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_39(self):
        self.assertEqual(run_calculator('14', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*39 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_40(self):
        self.assertEqual(run_calculator('14', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*40 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_41(self):
        self.assertEqual(run_calculator('14', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*41 = 574',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_42(self):
        self.assertEqual(run_calculator('14', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*42 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_43(self):
        self.assertEqual(run_calculator('14', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*43 = 602',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_44(self):
        self.assertEqual(run_calculator('14', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*44 = 616',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_45(self):
        self.assertEqual(run_calculator('14', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*45 = 630',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_46(self):
        self.assertEqual(run_calculator('14', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*46 = 644',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_47(self):
        self.assertEqual(run_calculator('14', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*47 = 658',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_48(self):
        self.assertEqual(run_calculator('14', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*48 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_49(self):
        self.assertEqual(run_calculator('14', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*49 = 686',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_14_times_50(self):
        self.assertEqual(run_calculator('14', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '14*50 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
