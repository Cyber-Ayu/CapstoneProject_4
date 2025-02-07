Feature: Web Element Verification

  Scenario: Verify webpage elements
    Given User launches "http://the-internet.herokuapp.com/"
    Then Verify the title of the page is "The Internet"

    When User clicks on "A/B Testing" link
    Then Verify the text on the page is "A/B Test Variation 1"

    When User navigates back to home page and clicks on "Dropdown" link
    Then Select "Option 1" from dropdown and verify it is selected

    When User navigates back to home page and clicks on "Frames" link
    Then Verify "Nested Frames" and "iFrame" hyperlinks are present
