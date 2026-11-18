# test_times_28.py
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


class TestTimes28(unittest.TestCase):

    def test_28_times_0(self):
        self.assertEqual(run_calculator('28', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_1(self):
        self.assertEqual(run_calculator('28', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*1 = 28',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_2(self):
        self.assertEqual(run_calculator('28', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*2 = 56',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_3(self):
        self.assertEqual(run_calculator('28', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*3 = 84',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_4(self):
        self.assertEqual(run_calculator('28', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*4 = 112',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_5(self):
        self.assertEqual(run_calculator('28', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*5 = 140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_6(self):
        self.assertEqual(run_calculator('28', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*6 = 168',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_7(self):
        self.assertEqual(run_calculator('28', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*7 = 196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_8(self):
        self.assertEqual(run_calculator('28', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*8 = 224',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_9(self):
        self.assertEqual(run_calculator('28', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*9 = 252',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_10(self):
        self.assertEqual(run_calculator('28', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*10 = 280',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_11(self):
        self.assertEqual(run_calculator('28', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*11 = 308',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_12(self):
        self.assertEqual(run_calculator('28', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*12 = 336',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_13(self):
        self.assertEqual(run_calculator('28', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*13 = 364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_14(self):
        self.assertEqual(run_calculator('28', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*14 = 392',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_15(self):
        self.assertEqual(run_calculator('28', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*15 = 420',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_16(self):
        self.assertEqual(run_calculator('28', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*16 = 448',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_17(self):
        self.assertEqual(run_calculator('28', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*17 = 476',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_18(self):
        self.assertEqual(run_calculator('28', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*18 = 504',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_19(self):
        self.assertEqual(run_calculator('28', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*19 = 532',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_20(self):
        self.assertEqual(run_calculator('28', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*20 = 560',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_21(self):
        self.assertEqual(run_calculator('28', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*21 = 588',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_22(self):
        self.assertEqual(run_calculator('28', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*22 = 616',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_23(self):
        self.assertEqual(run_calculator('28', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*23 = 644',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_24(self):
        self.assertEqual(run_calculator('28', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*24 = 672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_25(self):
        self.assertEqual(run_calculator('28', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*25 = 700',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_26(self):
        self.assertEqual(run_calculator('28', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*26 = 728',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_27(self):
        self.assertEqual(run_calculator('28', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*27 = 756',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_28(self):
        self.assertEqual(run_calculator('28', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*28 = 784',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_29(self):
        self.assertEqual(run_calculator('28', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*29 = 812',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_30(self):
        self.assertEqual(run_calculator('28', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*30 = 840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_31(self):
        self.assertEqual(run_calculator('28', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*31 = 868',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_32(self):
        self.assertEqual(run_calculator('28', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*32 = 896',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_33(self):
        self.assertEqual(run_calculator('28', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*33 = 924',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_34(self):
        self.assertEqual(run_calculator('28', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*34 = 952',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_35(self):
        self.assertEqual(run_calculator('28', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*35 = 980',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_36(self):
        self.assertEqual(run_calculator('28', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*36 = 1008',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_37(self):
        self.assertEqual(run_calculator('28', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*37 = 1036',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_38(self):
        self.assertEqual(run_calculator('28', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*38 = 1064',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_39(self):
        self.assertEqual(run_calculator('28', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*39 = 1092',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_40(self):
        self.assertEqual(run_calculator('28', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*40 = 1120',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_41(self):
        self.assertEqual(run_calculator('28', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*41 = 1148',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_42(self):
        self.assertEqual(run_calculator('28', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*42 = 1176',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_43(self):
        self.assertEqual(run_calculator('28', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*43 = 1204',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_44(self):
        self.assertEqual(run_calculator('28', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*44 = 1232',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_45(self):
        self.assertEqual(run_calculator('28', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*45 = 1260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_46(self):
        self.assertEqual(run_calculator('28', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*46 = 1288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_47(self):
        self.assertEqual(run_calculator('28', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*47 = 1316',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_48(self):
        self.assertEqual(run_calculator('28', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*48 = 1344',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_49(self):
        self.assertEqual(run_calculator('28', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*49 = 1372',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_28_times_50(self):
        self.assertEqual(run_calculator('28', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '28*50 = 1400',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
