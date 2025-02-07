package com.virtusa.base;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class BaseClass {
    public static WebDriver driver;

    public void initializeDriver() {
        if (driver == null) {
            System.setProperty("webdriver.chrome.driver", "src/main/driver/chromedriver-win64/chromedriver.exe");
            driver = new ChromeDriver();
            driver.manage().window().maximize();
        }
    }

    public void quitDriver() {
        if (driver != null) {
            driver.quit();
            driver = null; // Reset driver to null after quitting
        }
    }
}
