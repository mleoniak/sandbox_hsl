# import xml.etree.ElementTree as ET

# # Define the XML data
# xml_data = """<?xml version="1.0" encoding="utf-8"?>
# <testsuites>
#     <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="3" time="33.880" timestamp="2024-07-09T13:14:07.105918" hostname="DESKTOP-MFPGNL3">
#         <testcase classname="tests.test_00_search" name="test_search_this_website_functionality" time="11.931" />
#         <testcase classname="tests.test_01_nav_visibility" name="test_nav_vis" time="10.767" />
#         <testcase classname="tests.test_02_nav_content" name="test_nav_content" time="11.149" />
#     </testsuite>
# </testsuites>
# """
# # Parse the XML data
# root = ET.fromstring(xml_data)

# # Find all testcase elements within the testsuite
# testcases = root.findall('.//testcase')
# testsuite = root.findall('.//testsuite')

# # Get the second testcase element (index 1)
# second_testcase = testcases[1]

# # Extract attributes from the second testcase
# classname = second_testcase.get('classname')
# name = second_testcase.get('name')
# time = second_testcase.get('time')
# elapsed_computed = testsuite[0].get('time')
# print(elapsed_computed)
# print(len(testsuite))

# # Extract the time attribute from the first testcase
# # print(time)
# # print(name)
# # print(len(testcases))

# # for testcase in range(len(testcases)):
# #     classname = testcases[testcase].get('classname')
# #     print(classname.replace('tests.', ''))


    
