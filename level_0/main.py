#!/usr/bin/python3
"""Hodor level 1 - Still haven't watched game of thrones"""
import requests

page = "http://158.69.76.135/level0.php"
vote_for_me = {"id": "1716", "holdthedoor":"submit"}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(page, data=vote_for_me)
