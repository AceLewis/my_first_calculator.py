# test_times_8.py
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


class TestTimes8(unittest.TestCase):

    def test_8_times_0(self):
        self.assertEqual(run_calculator('8', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_1(self):
        self.assertEqual(run_calculator('8', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*1 = 8',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_2(self):
        self.assertEqual(run_calculator('8', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*2 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_3(self):
        self.assertEqual(run_calculator('8', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*3 = 24',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_4(self):
        self.assertEqual(run_calculator('8', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*4 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_5(self):
        self.assertEqual(run_calculator('8', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*5 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_6(self):
        self.assertEqual(run_calculator('8', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*6 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_7(self):
        self.assertEqual(run_calculator('8', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*7 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_8(self):
        self.assertEqual(run_calculator('8', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*8 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_9(self):
        self.assertEqual(run_calculator('8', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*9 = 72',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_10(self):
        self.assertEqual(run_calculator('8', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*10 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_11(self):
        self.assertEqual(run_calculator('8', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*11 = 88',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_12(self):
        self.assertEqual(run_calculator('8', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*12 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_13(self):
        self.assertEqual(run_calculator('8', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*13 = 104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_14(self):
        self.assertEqual(run_calculator('8', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*14 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_15(self):
        self.assertEqual(run_calculator('8', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*15 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_16(self):
        self.assertEqual(run_calculator('8', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*16 = 128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_17(self):
        self.assertEqual(run_calculator('8', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*17 = 136',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_18(self):
        self.assertEqual(run_calculator('8', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*18 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_19(self):
        self.assertEqual(run_calculator('8', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*19 = 152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_20(self):
        self.assertEqual(run_calculator('8', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*20 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_21(self):
        self.assertEqual(run_calculator('8', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*21 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_22(self):
        self.assertEqual(run_calculator('8', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*22 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_23(self):
        self.assertEqual(run_calculator('8', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*23 = 184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_24(self):
        self.assertEqual(run_calculator('8', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*24 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_25(self):
        self.assertEqual(run_calculator('8', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*25 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_26(self):
        self.assertEqual(run_calculator('8', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*26 = 208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_27(self):
        self.assertEqual(run_calculator('8', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*27 = 216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_28(self):
        self.assertEqual(run_calculator('8', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*28 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_29(self):
        self.assertEqual(run_calculator('8', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*29 = 232',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_30(self):
        self.assertEqual(run_calculator('8', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*30 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_31(self):
        self.assertEqual(run_calculator('8', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*31 = 248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_32(self):
        self.assertEqual(run_calculator('8', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*32 = 256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_33(self):
        self.assertEqual(run_calculator('8', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*33 = 264',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_34(self):
        self.assertEqual(run_calculator('8', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*34 = 272',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_35(self):
        self.assertEqual(run_calculator('8', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*35 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_36(self):
        self.assertEqual(run_calculator('8', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*36 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_37(self):
        self.assertEqual(run_calculator('8', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*37 = 296',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_38(self):
        self.assertEqual(run_calculator('8', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*38 = 304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_39(self):
        self.assertEqual(run_calculator('8', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*39 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_40(self):
        self.assertEqual(run_calculator('8', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*40 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_41(self):
        self.assertEqual(run_calculator('8', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*41 = 328',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_42(self):
        self.assertEqual(run_calculator('8', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*42 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_43(self):
        self.assertEqual(run_calculator('8', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*43 = 344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_44(self):
        self.assertEqual(run_calculator('8', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*44 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_45(self):
        self.assertEqual(run_calculator('8', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*45 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_46(self):
        self.assertEqual(run_calculator('8', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*46 = 368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_47(self):
        self.assertEqual(run_calculator('8', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*47 = 376',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_48(self):
        self.assertEqual(run_calculator('8', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*48 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_49(self):
        self.assertEqual(run_calculator('8', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*49 = 392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_8_times_50(self):
        self.assertEqual(run_calculator('8', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '8*50 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
