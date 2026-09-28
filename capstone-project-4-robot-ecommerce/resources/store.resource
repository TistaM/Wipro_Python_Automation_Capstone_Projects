*** Settings ***
Library     SeleniumLibrary
Resource    common.resource

*** Keywords ***
Remove Existing Product From Cart
    [Arguments]    ${product_name}
    Go To    ${BASE_URL}/view_cart
    Wait Until Page Contains Element    id:cart_info
    ${row}=    Set Variable    xpath://tr[.//a[normalize-space()='${product_name}']]
    ${count}=    Get Element Count    ${row}
    IF    ${count} > 0
        Click Element    xpath://tr[.//a[normalize-space()='${product_name}']]//a[contains(@class,'cart_quantity_delete')]
        Wait Until Page Does Not Contain Element    ${row}
    END

Search And Add Product
    [Arguments]    ${product_name}    ${quantity}
    Go To    ${BASE_URL}/products
    Wait Until Element Is Visible    id:search_product
    Input Text    id:search_product    ${product_name}
    Execute Javascript    document.getElementById('submit_search').click()
    Wait Until Page Contains Element    xpath://div[contains(@class,'productinfo')]//p[normalize-space()='${product_name}']

    ${link}=    Get Element Attribute
    ...    xpath://div[contains(@class,'product-image-wrapper')][.//p[normalize-space()='${product_name}']]//a[contains(.,'View Product')]
    ...    href
    Go To    ${link}
    Wait Until Element Is Visible    id:quantity
    Clear Element Text    id:quantity
    Input Text    id:quantity    ${quantity}
    Click Button    xpath://button[contains(.,'Add to cart')]
    Wait Until Element Is Visible    xpath://div[@id='cartModal']//a[contains(.,'View Cart')]
    Click Link    xpath://div[@id='cartModal']//a[contains(.,'View Cart')]

Verify Product In Cart
    [Arguments]    ${product_name}    ${quantity}
    ${row}=    Set Variable    xpath://tr[.//a[normalize-space()='${product_name}']]
    Wait Until Page Contains Element    ${row}
    ${actual_quantity}=    Get Text    xpath://tr[.//a[normalize-space()='${product_name}']]//td[contains(@class,'cart_quantity')]//button
    Should Be Equal As Strings    ${actual_quantity}    ${quantity}