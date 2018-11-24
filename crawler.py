from splinter import Browser
from json

with Browser("chrome") as browser:
    # Visit URL
    url = "https://leetcode.com/problems/two-sum/description/"
    browser.visit(url)
    if browser.is_text_present('return indices of the two numbers'):
        print(browser.html)
    else:
        print("fUCK!")
