package com.project.runners;

import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions(features = "src/test/resources/features",
        glue = "com.project.stepDefinitions", plugin = {"pretty", "html:test-output/cucumber-reports.html"})
public class TestRunner extends AbstractTestNGCucumberTests {
}
