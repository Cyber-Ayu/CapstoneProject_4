package com.project.stepDefinitions;

import com.project.base.BaseClass;
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
