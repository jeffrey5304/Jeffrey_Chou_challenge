*** Settings ***
Library    CustomKeywords.py
Library    ScreenCapLibrary

*** Variables ***
${URL}       http://www.way2automation.com/angularjs-protractor/webtables/
${BROWSER}   chrome
${USERNAME}  novak
@{USER_DETAILS}    Jeffrey    Chou    jchou    password123    Company AAA    Admin    jchou@test.com    1234567890

*** Test Cases ***
Add And Validate User
    [Documentation]    Add a user and validate the user has been added to the table
    Open Browser    ${URL}    ${BROWSER}
    Click Button    Add User
    Fill User Details    ${USER_DETAILS[0]}    ${USER_DETAILS[1]}    ${USER_DETAILS[2]}    ${USER_DETAILS[3]}    ${USER_DETAILS[4]}    ${USER_DETAILS[5]}    ${USER_DETAILS[6]}    ${USER_DETAILS[7]}
    Click Button    Save
    Validate User Added    ${USER_DETAILS[2]}
    Take Screenshot
    Close Browser

Delete And Validate User
    [Documentation]    Delete user with User Name: ${USERNAME} and validate user has been deleted
    Open Browser    ${URL}    ${BROWSER}
    Delete User
    Take Screenshot
    Validate User Deleted    ${USERNAME}
    Take Screenshot
    Close Browser


