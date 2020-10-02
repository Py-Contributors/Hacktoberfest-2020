"""
Usage:
* Download chromedriver and set binaty path in #9
* Fill in your username and password in #37 and #38 resp.
* Give full path of Source File and complete problem link
* Current Version supports only C++17 language, though you can change this in #46

Happy Coding!
Tanuj Raghav <anwailuisa>

For more details and better version visit anwailuisa/Sloth
Work still in progress, open to PRs!
"""
#!/usr/bin/env python3

import sys, subprocess
from selenium import webdriver

def submit(*args):

	options=webdriver.ChromeOptions()

	options.add_argument("--no-sandbox")
	options.add_argument("--start-maximized")

	driver=webdriver.Chrome(executable_path=r"/usr/bin/chromedriver",options=options)
	
	driver.get("https://codeforces.com/enter?back=%2F")

	username=""
	password=""

	driver.find_element_by_id("handleOrEmail").send_keys(username);
	driver.find_element_by_id("password").send_keys(password);
	driver.find_element_by_id("remember").click();

	driver.find_element_by_class_name("submit").click();

	driver.get(args[0][1])

	js="""
	var list = document.getElementsByTagName("option");
	for(var i=0;i<list.length;i++){
		if(list[i].innerHTML==arguments[0]){
				list[i].setAttribute("selected","selected");
			}
		}
	"""

	driver.execute_script(js,"GNU G++17 7.3.0")

	driver.find_element_by_name("sourceFile").send_keys(args[0][2]);

	driver.find_element_by_class_name("submit").click();

	return driver

def main()
	link=input("Please enter problem link (e.g. https://codeforces.com/problemset/1/A): ")
	source=input("Please enter full path to source file (e.g. /home/user/test.cpp): ")

	submit(link,source)

if __name__ == "__main__":
	main()
