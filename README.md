



How to run the automation

Run the test suite using the Robot Framework command:

bash

robot Automate_Test.robot


Settings Section:

implement custom keywords using CustomKeywords.py


Test Cases Section:


Test Scenario 1

Add And Validate User:

1.Open the browser and navigate to the specified URL.
2.Click the "Add User" button.
3.Fill in the user details using the custom keyword Fill User Details.
4.Click the "Save" button.
5.Validate that the user has been added using the custom keyword Validate User Added.
6.Take Screenshot
7.Close the browser.

Test Scenario 2

1.Delete And Validate User:
2.Open the browser and navigate to the specified URL.
3.Validate that the user exists using the custom keyword Validate User Exists.
4.Delete the user using the custom keyword Delete User.
5.Validate that the user has been deleted using the custom keyword Validate User Deleted.
6.Close the browser.












