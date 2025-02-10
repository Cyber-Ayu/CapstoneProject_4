package com.virtusa.tests;

import com.virtusa.utils.ExtentReportManager;
import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.annotations.AfterSuite;
import org.testng.annotations.BeforeSuite;
import org.testng.annotations.DataProvider;
import com.virtusa.utils.ExcelUtils;
import org.testng.annotations.Test;

import java.io.IOException;
import java.util.Iterator;
import java.util.List;


import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.notNullValue;

public class CountryTranslationTest {

    @BeforeSuite
    public void setup() {
        ExtentReportManager.initReport();
    }

    @DataProvider(name = "translationData")
    public Iterator<Object[]> translationData() throws IOException {
        ExcelUtils excelUtils = new ExcelUtils("src/test/resources/TestData.xlsx");
        List<String> translations = excelUtils.getTranslations("Sheet1");
        return translations.stream().map(t -> new Object[]{t}).iterator();
    }

    @Test(dataProvider = "translationData")
    public void testCountryTranslation(String translation) {

        ExtentReportManager.startTest("API Test for: " + translation);

        RestAssured.baseURI = "https://restcountries.com/v3.1/translation";

        Response response = given()
                .pathParam("translation", translation)
                .when()
                .get("/{translation}")
                .then()
                .statusCode(200)  // Validate HTTP status
                .body("[0].name.common", notNullValue())  // Ensure response contains country name
                .extract().response();

        ExtentReportManager.logInfo("Response: " + response.asString());
        ExtentReportManager.logPass("API Test Passed for: " + translation);

        System.out.println("Response for " + translation + " : " + response.asString());
    }

    @AfterSuite
    public void tearDown() {
        ExtentReportManager.finalizeReport();
    }
}
