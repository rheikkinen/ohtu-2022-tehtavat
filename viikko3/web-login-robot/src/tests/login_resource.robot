*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register With Valid Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Confirm Password  ${password}
    Submit Register Info
    Welcome Page Should Be Open

Register With Invalid Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Confirm Password  ${password}
    Submit Register Info

Login With Invalid Credentials
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
