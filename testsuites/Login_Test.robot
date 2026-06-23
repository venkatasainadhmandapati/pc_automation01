*** Settings ***
Resource      ../resources/CommonKeywords.robot



*** Variables ***


*** Test Cases ***
Install Software ON IOSXR
    Login pc Application
    Install IOSXR Image
    Close pc Application
