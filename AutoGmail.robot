*** Settings ***
Suite Setup       Go to Gmail
Suite Teardown    Close All Browsers
Test Template     Gmail Login with Invalid Credentials should fail
Library           Selenium2Library    timeout=10    implicit_wait=10

*** Variables ***
${signInElem}     id=signIn
${vemail}         nstest739@gmail.com
${emailPass}      pass
${emailElem}      id=Email
${emailPassElem}    id=Passwd
${inboxElem}      xpath=//a[contains(@title,'Inbox')]
${browser}        ff
${homepage}       http://www.gmail.com

*** Test Cases ***
Invalid Username
    invalid@gmail.com    ${emailPass}

Invalid Password
    ${vemail}    invalidpass

*** Keywords ***
Gmail Login with Invalid Credentials should fail
    [Arguments]    ${email}    ${pass}
    Is Visible    ${signInElem}
    Input Text    ${emailElem}    ${email}
    Input Password    ${emailPassElem}    ${pass}
    Click Button    ${signInElem}
    #Is Visible    ${inboxElem}

Is Visible
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}

Go to Gmail
    Open Browser    ${homepage}    ${browser}

Login should have failed
    Wait Until Page Cointains    The email or password you entered is incorrect.
