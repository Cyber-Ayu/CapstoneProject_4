package com.virtusa.stepDefinitions;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import com.virtusa.base.BaseClass;
import io.cucumber.java.en.*;

import java.time.Duration;

public class VerifyWebElementsSteps {

    @Given("User launches {string}")
    public void user_launches(String url) {
        BaseClass.driver.get(url);  // Use BaseClass.driver directly
    }

    @Then("Verify the title of the page is {string}")
    public void verify_the_title_of_the_page_is(String expectedTitle) {
        Assert.assertEquals(BaseClass.driver.getTitle(), expectedTitle);
    }

    @When("User clicks on {string} link")
    public void user_clicks_on_link(String linkText) {
        BaseClass.driver.findElement(By.linkText(linkText)).click();
    }

    @Then("Verify the text on the page is {string}")
    public void verify_the_text_on_the_page_is(String expectedText) {
        WebDriverWait wait = new WebDriverWait(BaseClass.driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.textToBePresentInElementLocated(By.tagName("body"), expectedText));

        WebElement body = BaseClass.driver.findElement(By.tagName("body"));
        String actualText = body.getText().trim();

        // Debugging output
        System.out.println("Actual Page Text: " + actualText);

        Assert.assertTrue(actualText.contains(expectedText.trim()),
                "Expected text: '" + expectedText + "' not found! Actual text: '" + actualText + "'");
    }


    @Then("Select {string} from dropdown and verify it is selected")
    public void select_from_dropdown_and_verify_it_is_selected(String option) {
        Select dropdown = new Select(BaseClass.driver.findElement(By.id("dropdown")));
        dropdown.selectByVisibleText(option);
        Assert.assertEquals(dropdown.getFirstSelectedOption().getText(), option);
    }

    @Then("Verify {string} and {string} hyperlinks are present")
    public void verify_and_hyperlinks_are_present(String link1, String link2) {
        Assert.assertTrue(BaseClass.driver.findElement(By.linkText(link1)).isDisplayed());
        Assert.assertTrue(BaseClass.driver.findElement(By.linkText(link2)).isDisplayed());
    }

    @When("User navigates back to home page and clicks on {string} link")
    public void user_navigates_back_to_home_page_and_clicks_on_link(String linkText) {
        BaseClass.driver.navigate().back();
        WebElement link = BaseClass.driver.findElement(By.linkText(linkText));
        link.click();
    }



}
