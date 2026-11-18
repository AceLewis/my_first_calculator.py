# test_times_16.py
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


class TestTimes16(unittest.TestCase):

    def test_16_times_0(self):
        self.assertEqual(run_calculator('16', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_1(self):
        self.assertEqual(run_calculator('16', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*1 = 16',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_2(self):
        self.assertEqual(run_calculator('16', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*2 = 32',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_3(self):
        self.assertEqual(run_calculator('16', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*3 = 48',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_4(self):
        self.assertEqual(run_calculator('16', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*4 = 64',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_5(self):
        self.assertEqual(run_calculator('16', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*5 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_6(self):
        self.assertEqual(run_calculator('16', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*6 = 96',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_7(self):
        self.assertEqual(run_calculator('16', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*7 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_8(self):
        self.assertEqual(run_calculator('16', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*8 = 128',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_9(self):
        self.assertEqual(run_calculator('16', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*9 = 144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_10(self):
        self.assertEqual(run_calculator('16', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*10 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_11(self):
        self.assertEqual(run_calculator('16', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*11 = 176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_12(self):
        self.assertEqual(run_calculator('16', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*12 = 192',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_13(self):
        self.assertEqual(run_calculator('16', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*13 = 208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_14(self):
        self.assertEqual(run_calculator('16', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*14 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_15(self):
        self.assertEqual(run_calculator('16', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*15 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_16(self):
        self.assertEqual(run_calculator('16', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*16 = 256',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_17(self):
        self.assertEqual(run_calculator('16', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*17 = 272',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_18(self):
        self.assertEqual(run_calculator('16', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*18 = 288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_19(self):
        self.assertEqual(run_calculator('16', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*19 = 304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_20(self):
        self.assertEqual(run_calculator('16', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*20 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_21(self):
        self.assertEqual(run_calculator('16', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*21 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_22(self):
        self.assertEqual(run_calculator('16', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*22 = 352',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_23(self):
        self.assertEqual(run_calculator('16', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*23 = 368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_24(self):
        self.assertEqual(run_calculator('16', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*24 = 384',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_25(self):
        self.assertEqual(run_calculator('16', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*25 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_26(self):
        self.assertEqual(run_calculator('16', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*26 = 416',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_27(self):
        self.assertEqual(run_calculator('16', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*27 = 432',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_28(self):
        self.assertEqual(run_calculator('16', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*28 = 448',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_29(self):
        self.assertEqual(run_calculator('16', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*29 = 464',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_30(self):
        self.assertEqual(run_calculator('16', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*30 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_31(self):
        self.assertEqual(run_calculator('16', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*31 = 496',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_32(self):
        self.assertEqual(run_calculator('16', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*32 = 512',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_33(self):
        self.assertEqual(run_calculator('16', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*33 = 528',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_34(self):
        self.assertEqual(run_calculator('16', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*34 = 544',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_35(self):
        self.assertEqual(run_calculator('16', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*35 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_36(self):
        self.assertEqual(run_calculator('16', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*36 = 576',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_37(self):
        self.assertEqual(run_calculator('16', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*37 = 592',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_38(self):
        self.assertEqual(run_calculator('16', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*38 = 608',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_39(self):
        self.assertEqual(run_calculator('16', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*39 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_40(self):
        self.assertEqual(run_calculator('16', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*40 = 640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_41(self):
        self.assertEqual(run_calculator('16', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*41 = 656',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_42(self):
        self.assertEqual(run_calculator('16', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*42 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_43(self):
        self.assertEqual(run_calculator('16', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*43 = 688',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_44(self):
        self.assertEqual(run_calculator('16', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*44 = 704',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_45(self):
        self.assertEqual(run_calculator('16', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*45 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_46(self):
        self.assertEqual(run_calculator('16', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*46 = 736',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_47(self):
        self.assertEqual(run_calculator('16', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*47 = 752',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_48(self):
        self.assertEqual(run_calculator('16', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*48 = 768',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_49(self):
        self.assertEqual(run_calculator('16', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*49 = 784',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_16_times_50(self):
        self.assertEqual(run_calculator('16', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '16*50 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
