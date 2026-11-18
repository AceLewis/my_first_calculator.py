# test_times_20.py
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


class TestTimes20(unittest.TestCase):

    def test_20_times_0(self):
        self.assertEqual(run_calculator('20', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_1(self):
        self.assertEqual(run_calculator('20', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*1 = 20',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_2(self):
        self.assertEqual(run_calculator('20', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*2 = 40',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_3(self):
        self.assertEqual(run_calculator('20', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*3 = 60',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_4(self):
        self.assertEqual(run_calculator('20', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*4 = 80',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_5(self):
        self.assertEqual(run_calculator('20', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*5 = 100',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_6(self):
        self.assertEqual(run_calculator('20', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*6 = 120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_7(self):
        self.assertEqual(run_calculator('20', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*7 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_8(self):
        self.assertEqual(run_calculator('20', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*8 = 160',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_9(self):
        self.assertEqual(run_calculator('20', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*9 = 180',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_10(self):
        self.assertEqual(run_calculator('20', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*10 = 200',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_11(self):
        self.assertEqual(run_calculator('20', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*11 = 220',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_12(self):
        self.assertEqual(run_calculator('20', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*12 = 240',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_13(self):
        self.assertEqual(run_calculator('20', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*13 = 260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_14(self):
        self.assertEqual(run_calculator('20', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*14 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_15(self):
        self.assertEqual(run_calculator('20', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*15 = 300',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_16(self):
        self.assertEqual(run_calculator('20', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*16 = 320',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_17(self):
        self.assertEqual(run_calculator('20', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*17 = 340',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_18(self):
        self.assertEqual(run_calculator('20', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*18 = 360',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_19(self):
        self.assertEqual(run_calculator('20', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*19 = 380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_20(self):
        self.assertEqual(run_calculator('20', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*20 = 400',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_21(self):
        self.assertEqual(run_calculator('20', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*21 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_22(self):
        self.assertEqual(run_calculator('20', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*22 = 440',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_23(self):
        self.assertEqual(run_calculator('20', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*23 = 460',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_24(self):
        self.assertEqual(run_calculator('20', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*24 = 480',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_25(self):
        self.assertEqual(run_calculator('20', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*25 = 500',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_26(self):
        self.assertEqual(run_calculator('20', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*26 = 520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_27(self):
        self.assertEqual(run_calculator('20', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*27 = 540',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_28(self):
        self.assertEqual(run_calculator('20', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*28 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_29(self):
        self.assertEqual(run_calculator('20', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*29 = 580',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_30(self):
        self.assertEqual(run_calculator('20', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*30 = 600',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_31(self):
        self.assertEqual(run_calculator('20', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*31 = 620',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_32(self):
        self.assertEqual(run_calculator('20', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*32 = 640',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_33(self):
        self.assertEqual(run_calculator('20', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*33 = 660',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_34(self):
        self.assertEqual(run_calculator('20', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*34 = 680',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_35(self):
        self.assertEqual(run_calculator('20', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*35 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_36(self):
        self.assertEqual(run_calculator('20', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*36 = 720',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_37(self):
        self.assertEqual(run_calculator('20', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*37 = 740',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_38(self):
        self.assertEqual(run_calculator('20', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*38 = 760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_39(self):
        self.assertEqual(run_calculator('20', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*39 = 780',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_40(self):
        self.assertEqual(run_calculator('20', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*40 = 800',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_41(self):
        self.assertEqual(run_calculator('20', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*41 = 820',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_42(self):
        self.assertEqual(run_calculator('20', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*42 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_43(self):
        self.assertEqual(run_calculator('20', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*43 = 860',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_44(self):
        self.assertEqual(run_calculator('20', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*44 = 880',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_45(self):
        self.assertEqual(run_calculator('20', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*45 = 900',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_46(self):
        self.assertEqual(run_calculator('20', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*46 = 920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_47(self):
        self.assertEqual(run_calculator('20', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*47 = 940',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_48(self):
        self.assertEqual(run_calculator('20', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*48 = 960',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_49(self):
        self.assertEqual(run_calculator('20', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*49 = 980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_20_times_50(self):
        self.assertEqual(run_calculator('20', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '20*50 = 1000',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
