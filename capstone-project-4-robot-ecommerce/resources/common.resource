*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BASE_URL}    https://automationexercise.com
${BROWSER}     Chrome

*** Keywords ***
Open Demo Browser
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    15 seconds

Login To Demo Store
    Go To    ${BASE_URL}/login
    Wait Until Element Is Visible    css:form[action='/login'] input[name='email']
    Input Text    css:form[action='/login'] input[name='email']    %{AE_TEST_EMAIL}
    Input Password    css:form[action='/login'] input[name='password']    %{AE_TEST_PASSWORD}
    Click Button    css:form[action='/login'] button[type='submit']
    Wait Until Page Contains    Logged in as

Logout From Demo Store
    Click Link    xpath=//a[contains(@href, '/logout')]
    Wait Until Location Contains    /login