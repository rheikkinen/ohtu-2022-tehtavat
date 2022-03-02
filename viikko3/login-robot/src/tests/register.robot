*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And password
    Input Credentials  leena  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  salasana123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  leena  lyhyt1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  leena  salasana
    Output Should Contain  Password must contain at least one digit or special character

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command
