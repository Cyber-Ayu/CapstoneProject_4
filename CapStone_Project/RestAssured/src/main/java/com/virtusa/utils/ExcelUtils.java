package com.virtusa.utils;

import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.usermodel.WorkbookFactory;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ExcelUtils {
    private String filePath;

    public ExcelUtils(String filePath) {
        this.filePath = filePath;
    }

    public List<String> getTranslations(String sheetName) throws IOException {
        List<String> transaltions = new ArrayList<>();
        try (FileInputStream fis = new FileInputStream(filePath);
             Workbook workbook = WorkbookFactory.create(fis)) {
            Sheet sheet = workbook.getSheet(sheetName);
            for (Row row : sheet) {
                if (row.getRowNum() == 0) continue;
                transaltions.add(row.getCell(1).getStringCellValue());
            }
        }
        return transaltions;
    }
}
