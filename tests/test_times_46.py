# test_times_46.py
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


class TestTimes46(unittest.TestCase):

    def test_46_times_0(self):
        self.assertEqual(run_calculator('46', '*', '0'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*0 = 0',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_1(self):
        self.assertEqual(run_calculator('46', '*', '1'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*1 = 46',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_2(self):
        self.assertEqual(run_calculator('46', '*', '2'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*2 = 92',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_3(self):
        self.assertEqual(run_calculator('46', '*', '3'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*3 = 138',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_4(self):
        self.assertEqual(run_calculator('46', '*', '4'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*4 = 184',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_5(self):
        self.assertEqual(run_calculator('46', '*', '5'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*5 = 230',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_6(self):
        self.assertEqual(run_calculator('46', '*', '6'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*6 = 276',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_7(self):
        self.assertEqual(run_calculator('46', '*', '7'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*7 = 322',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_8(self):
        self.assertEqual(run_calculator('46', '*', '8'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*8 = 368',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_9(self):
        self.assertEqual(run_calculator('46', '*', '9'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*9 = 414',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_10(self):
        self.assertEqual(run_calculator('46', '*', '10'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*10 = 460',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_11(self):
        self.assertEqual(run_calculator('46', '*', '11'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*11 = 506',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_12(self):
        self.assertEqual(run_calculator('46', '*', '12'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*12 = 552',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_13(self):
        self.assertEqual(run_calculator('46', '*', '13'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*13 = 598',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_14(self):
        self.assertEqual(run_calculator('46', '*', '14'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*14 = 644',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_15(self):
        self.assertEqual(run_calculator('46', '*', '15'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*15 = 690',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_16(self):
        self.assertEqual(run_calculator('46', '*', '16'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*16 = 736',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_17(self):
        self.assertEqual(run_calculator('46', '*', '17'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*17 = 782',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_18(self):
        self.assertEqual(run_calculator('46', '*', '18'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*18 = 828',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_19(self):
        self.assertEqual(run_calculator('46', '*', '19'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*19 = 874',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_20(self):
        self.assertEqual(run_calculator('46', '*', '20'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*20 = 920',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_21(self):
        self.assertEqual(run_calculator('46', '*', '21'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*21 = 966',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_22(self):
        self.assertEqual(run_calculator('46', '*', '22'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*22 = 1012',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_23(self):
        self.assertEqual(run_calculator('46', '*', '23'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*23 = 1058',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_24(self):
        self.assertEqual(run_calculator('46', '*', '24'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*24 = 1104',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_25(self):
        self.assertEqual(run_calculator('46', '*', '25'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*25 = 1150',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_26(self):
        self.assertEqual(run_calculator('46', '*', '26'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*26 = 1196',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_27(self):
        self.assertEqual(run_calculator('46', '*', '27'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*27 = 1242',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_28(self):
        self.assertEqual(run_calculator('46', '*', '28'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*28 = 1288',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_29(self):
        self.assertEqual(run_calculator('46', '*', '29'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*29 = 1334',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_30(self):
        self.assertEqual(run_calculator('46', '*', '30'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*30 = 1380',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_31(self):
        self.assertEqual(run_calculator('46', '*', '31'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*31 = 1426',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_32(self):
        self.assertEqual(run_calculator('46', '*', '32'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*32 = 1472',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_33(self):
        self.assertEqual(run_calculator('46', '*', '33'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*33 = 1518',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_34(self):
        self.assertEqual(run_calculator('46', '*', '34'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*34 = 1564',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_35(self):
        self.assertEqual(run_calculator('46', '*', '35'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*35 = 1610',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_36(self):
        self.assertEqual(run_calculator('46', '*', '36'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*36 = 1656',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_37(self):
        self.assertEqual(run_calculator('46', '*', '37'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*37 = 1702',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_38(self):
        self.assertEqual(run_calculator('46', '*', '38'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*38 = 1748',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_39(self):
        self.assertEqual(run_calculator('46', '*', '39'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*39 = 1794',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_40(self):
        self.assertEqual(run_calculator('46', '*', '40'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*40 = 1840',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_41(self):
        self.assertEqual(run_calculator('46', '*', '41'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*41 = 1886',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_42(self):
        self.assertEqual(run_calculator('46', '*', '42'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*42 = 1932',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_43(self):
        self.assertEqual(run_calculator('46', '*', '43'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*43 = 1978',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_44(self):
        self.assertEqual(run_calculator('46', '*', '44'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*44 = 2024',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_45(self):
        self.assertEqual(run_calculator('46', '*', '45'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*45 = 2070',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_46(self):
        self.assertEqual(run_calculator('46', '*', '46'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*46 = 2116',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_47(self):
        self.assertEqual(run_calculator('46', '*', '47'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*47 = 2162',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_48(self):
        self.assertEqual(run_calculator('46', '*', '48'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*48 = 2208',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_49(self):
        self.assertEqual(run_calculator('46', '*', '49'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*49 = 2254',
            'Thanks for using this calculator, goodbye :)',
        ])

    def test_46_times_50(self):
        self.assertEqual(run_calculator('46', '*', '50'), [
            'Welcome to this calculator!',
            'It can add, subtract, multiply and divide whole numbers from 0 to 50',
            '46*50 = 2300',
            'Thanks for using this calculator, goodbye :)',
        ])


if __name__ == '__main__':
    unittest.main()
