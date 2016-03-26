#!/usr/bin/env python3.5

import subprocess
import unittest

curl_args = [
    '-X', 'POST',
    '-d', '@test.html',
    '--header', 'Content-Type:application/html',
]

host = "http://127.0.0.1:5001"

class TestAPI(unittest.TestCase):

    def test_headers(self):
        cmd = ['curl', '-I'] + curl_args + [host + '/sample']
        got_headers = subprocess.run(curl)
        expect_headers = [
            'Content-Type: application/pdf',
            'Content-Disposition: inline; filename=sample.pdf'
        ]
        for expected in expect_headers:
            self.assertEqual(got_headers, expected)

    def test_body(self):
        cmd = ['curl'] + curl_args + [host]
        body = subprocess.run(cmd)
        self.assertEqual(body[:4], b'%PDF')


if __name__ == '__main__':
    unittest.main()
