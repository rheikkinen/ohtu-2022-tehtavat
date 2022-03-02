*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  leena
    Set Password  leena123
    Confirm Password  leena123
    Submit Register Info
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  abcdef123
    Confirm Password  abcdef123
    Submit Register Info
    Registration Should Fail With Message  Username is not valid

Register With Valid Username And Too Short Password
    Set Username  leena
    Set password  lyhyt1
    Confirm Password  lyhyt1
    Submit Register Info
    Registration Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  leena
    Set Password  leena123
    Confirm Password  leena456
    Submit Register Info
    Registration Should Fail With Message  Passwords do not match

Login After Succesful Registration
    Register With Valid Credentials  leena  leena123
    Go To Login Page
    Set Username  leena
    Set Password  leena123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Register With Invalid Credentials  leena  lyhyt1
    Registration Should Fail With Message  Password is not valid
    Go To Login Page
    Login With Invalid Credentials  leena  lyhyt1
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}  

Submit Register Info
    Click Button  Register

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}