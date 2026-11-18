# test_times_26.py
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


class TestTimes26(unittest.TestCase):

    def test_26_times_0(self):
        self.assertEqual(run_calculator('26', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_1(self):
        self.assertEqual(run_calculator('26', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*1 = 26',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_2(self):
        self.assertEqual(run_calculator('26', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*2 = 52',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_3(self):
        self.assertEqual(run_calculator('26', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*3 = 78',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_4(self):
        self.assertEqual(run_calculator('26', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*4 = 104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_5(self):
        self.assertEqual(run_calculator('26', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*5 = 130',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_6(self):
        self.assertEqual(run_calculator('26', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*6 = 156',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_7(self):
        self.assertEqual(run_calculator('26', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*7 = 182',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_8(self):
        self.assertEqual(run_calculator('26', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*8 = 208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_9(self):
        self.assertEqual(run_calculator('26', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*9 = 234',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_10(self):
        self.assertEqual(run_calculator('26', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*10 = 260',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_11(self):
        self.assertEqual(run_calculator('26', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*11 = 286',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_12(self):
        self.assertEqual(run_calculator('26', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*12 = 312',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_13(self):
        self.assertEqual(run_calculator('26', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*13 = 338',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_14(self):
        self.assertEqual(run_calculator('26', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*14 = 364',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_15(self):
        self.assertEqual(run_calculator('26', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*15 = 390',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_16(self):
        self.assertEqual(run_calculator('26', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*16 = 416',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_17(self):
        self.assertEqual(run_calculator('26', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*17 = 442',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_18(self):
        self.assertEqual(run_calculator('26', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*18 = 468',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_19(self):
        self.assertEqual(run_calculator('26', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*19 = 494',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_20(self):
        self.assertEqual(run_calculator('26', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*20 = 520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_21(self):
        self.assertEqual(run_calculator('26', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*21 = 546',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_22(self):
        self.assertEqual(run_calculator('26', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*22 = 572',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_23(self):
        self.assertEqual(run_calculator('26', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*23 = 598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_24(self):
        self.assertEqual(run_calculator('26', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*24 = 624',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_25(self):
        self.assertEqual(run_calculator('26', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*25 = 650',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_26(self):
        self.assertEqual(run_calculator('26', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*26 = 676',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_27(self):
        self.assertEqual(run_calculator('26', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*27 = 702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_28(self):
        self.assertEqual(run_calculator('26', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*28 = 728',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_29(self):
        self.assertEqual(run_calculator('26', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*29 = 754',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_30(self):
        self.assertEqual(run_calculator('26', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*30 = 780',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_31(self):
        self.assertEqual(run_calculator('26', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*31 = 806',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_32(self):
        self.assertEqual(run_calculator('26', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*32 = 832',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_33(self):
        self.assertEqual(run_calculator('26', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*33 = 858',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_34(self):
        self.assertEqual(run_calculator('26', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*34 = 884',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_35(self):
        self.assertEqual(run_calculator('26', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*35 = 910',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_36(self):
        self.assertEqual(run_calculator('26', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*36 = 936',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_37(self):
        self.assertEqual(run_calculator('26', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*37 = 962',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_38(self):
        self.assertEqual(run_calculator('26', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*38 = 988',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_39(self):
        self.assertEqual(run_calculator('26', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*39 = 1014',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_40(self):
        self.assertEqual(run_calculator('26', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*40 = 1040',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_41(self):
        self.assertEqual(run_calculator('26', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*41 = 1066',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_42(self):
        self.assertEqual(run_calculator('26', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*42 = 1092',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_43(self):
        self.assertEqual(run_calculator('26', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*43 = 1118',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_44(self):
        self.assertEqual(run_calculator('26', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*44 = 1144',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_45(self):
        self.assertEqual(run_calculator('26', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*45 = 1170',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_46(self):
        self.assertEqual(run_calculator('26', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*46 = 1196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_47(self):
        self.assertEqual(run_calculator('26', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*47 = 1222',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_48(self):
        self.assertEqual(run_calculator('26', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*48 = 1248',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_49(self):
        self.assertEqual(run_calculator('26', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*49 = 1274',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_26_times_50(self):
        self.assertEqual(run_calculator('26', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '26*50 = 1300',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
