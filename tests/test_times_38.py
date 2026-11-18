# test_times_38.py
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


class TestTimes38(unittest.TestCase):

    def test_38_times_0(self):
        self.assertEqual(run_calculator('38', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_1(self):
        self.assertEqual(run_calculator('38', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*1 = 38',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_2(self):
        self.assertEqual(run_calculator('38', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*2 = 76',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_3(self):
        self.assertEqual(run_calculator('38', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*3 = 114',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_4(self):
        self.assertEqual(run_calculator('38', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*4 = 152',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_5(self):
        self.assertEqual(run_calculator('38', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*5 = 190',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_6(self):
        self.assertEqual(run_calculator('38', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*6 = 228',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_7(self):
        self.assertEqual(run_calculator('38', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*7 = 266',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_8(self):
        self.assertEqual(run_calculator('38', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*8 = 304',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_9(self):
        self.assertEqual(run_calculator('38', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*9 = 342',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_10(self):
        self.assertEqual(run_calculator('38', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*10 = 380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_11(self):
        self.assertEqual(run_calculator('38', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*11 = 418',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_12(self):
        self.assertEqual(run_calculator('38', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*12 = 456',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_13(self):
        self.assertEqual(run_calculator('38', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*13 = 494',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_14(self):
        self.assertEqual(run_calculator('38', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*14 = 532',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_15(self):
        self.assertEqual(run_calculator('38', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*15 = 570',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_16(self):
        self.assertEqual(run_calculator('38', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*16 = 608',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_17(self):
        self.assertEqual(run_calculator('38', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*17 = 646',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_18(self):
        self.assertEqual(run_calculator('38', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*18 = 684',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_19(self):
        self.assertEqual(run_calculator('38', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*19 = 722',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_20(self):
        self.assertEqual(run_calculator('38', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*20 = 760',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_21(self):
        self.assertEqual(run_calculator('38', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*21 = 798',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_22(self):
        self.assertEqual(run_calculator('38', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*22 = 836',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_23(self):
        self.assertEqual(run_calculator('38', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*23 = 874',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_24(self):
        self.assertEqual(run_calculator('38', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*24 = 912',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_25(self):
        self.assertEqual(run_calculator('38', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*25 = 950',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_26(self):
        self.assertEqual(run_calculator('38', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*26 = 988',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_27(self):
        self.assertEqual(run_calculator('38', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*27 = 1026',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_28(self):
        self.assertEqual(run_calculator('38', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*28 = 1064',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_29(self):
        self.assertEqual(run_calculator('38', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*29 = 1102',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_30(self):
        self.assertEqual(run_calculator('38', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*30 = 1140',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_31(self):
        self.assertEqual(run_calculator('38', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*31 = 1178',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_32(self):
        self.assertEqual(run_calculator('38', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*32 = 1216',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_33(self):
        self.assertEqual(run_calculator('38', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*33 = 1254',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_34(self):
        self.assertEqual(run_calculator('38', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*34 = 1292',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_35(self):
        self.assertEqual(run_calculator('38', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*35 = 1330',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_36(self):
        self.assertEqual(run_calculator('38', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*36 = 1368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_37(self):
        self.assertEqual(run_calculator('38', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*37 = 1406',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_38(self):
        self.assertEqual(run_calculator('38', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*38 = 1444',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_39(self):
        self.assertEqual(run_calculator('38', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*39 = 1482',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_40(self):
        self.assertEqual(run_calculator('38', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*40 = 1520',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_41(self):
        self.assertEqual(run_calculator('38', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*41 = 1558',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_42(self):
        self.assertEqual(run_calculator('38', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*42 = 1596',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_43(self):
        self.assertEqual(run_calculator('38', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*43 = 1634',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_44(self):
        self.assertEqual(run_calculator('38', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*44 = 1672',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_45(self):
        self.assertEqual(run_calculator('38', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*45 = 1710',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_46(self):
        self.assertEqual(run_calculator('38', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*46 = 1748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_47(self):
        self.assertEqual(run_calculator('38', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*47 = 1786',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_48(self):
        self.assertEqual(run_calculator('38', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*48 = 1824',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_49(self):
        self.assertEqual(run_calculator('38', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*49 = 1862',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_38_times_50(self):
        self.assertEqual(run_calculator('38', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '38*50 = 1900',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
