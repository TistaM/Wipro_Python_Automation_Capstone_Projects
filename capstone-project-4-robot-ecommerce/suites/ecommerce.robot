*** Settings ***
Resource         ../resources/store.resource
Variables        ../data/products.py
Test Setup       Open Demo Browser
Test Teardown    Close All Browsers
Test Template    Complete Shopping Flow

*** Test Cases ***
Buy Blue Top      ${PRODUCT_CASES}[0][0]    ${PRODUCT_CASES}[0][1]
Buy Winter Top    ${PRODUCT_CASES}[1][0]    ${PRODUCT_CASES}[1][1]

*** Keywords ***
Complete Shopping Flow
    [Arguments]    ${product_name}    ${quantity}
    Login To Demo Store
    Remove Existing Product From Cart    ${product_name}
    Search And Add Product    ${product_name}    ${quantity}
    Verify Product In Cart    ${product_name}    ${quantity}
    Logout From Demo Store