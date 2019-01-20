import unittest

import tests.utils

import os
import subprocess
import sys


class SubmitAtCoderTest(unittest.TestCase):

    def test_call_submit_practice(self):
        if 'CI' in os.environ:
            print('NOTE: this test is skipped since login is required')
            return

        url = 'https://atcoder.jp/contests/practice/tasks/practice_1'
        code = '''\
#include <bits/stdc++.h>
using namespace std;
int main() {
    int a; cin >> a;
    int b, c; cin >> b >> c;
    string s; cin >> s;
    cout << a + b + c << ' ' << s << endl;
    return 0;
}
'''
        files = [
            { 'path': 'main.cpp', 'data': code },
        ]

        ojtools = os.path.abspath('oj')
        with tests.utils.sandbox(files):
            subprocess.check_call([ ojtools, 'submit', '-y', '--no-open', url, 'main.cpp' ], stdout=sys.stdout, stderr=sys.stderr)

    def test_call_submit_practice_with_history(self):
        if 'CI' in os.environ:
            print('NOTE: this test is skipped since login is required')
            return

        url = 'https://atcoder.jp/contests/practice/tasks/practice_1'
        files = [
            { 'path': 'a.pl', 'data': 'print<>+(<>=~$",$`+$\'),$",<>' },
        ]
        ojtools = os.path.abspath('oj')
        with tests.utils.sandbox(files):
            subprocess.check_call([ ojtools, 'dl', url ], stdout=sys.stdout, stderr=sys.stderr)
            subprocess.check_call([ ojtools, 's', '-y', '--no-open', 'a.pl' ], stdout=sys.stdout, stderr=sys.stderr)
