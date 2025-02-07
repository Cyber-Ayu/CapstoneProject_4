package com.virtusa.stepDefinitions;

import com.virtusa.base.BaseClass;
import io.cucumber.java.After;
import io.cucumber.java.Before;

public class Hooks {

    BaseClass base = new BaseClass();  // Instance of BaseClass

    @Before
    public void setUp() {
        base.initializeDriver();  // Initialize WebDriver
    }

    @After
    public void tearDown() {
        base.quitDriver();  // Quit WebDriver after test
    }
}
