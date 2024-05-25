Here is a potential patch for the code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    ScanResult scanResult = directoryScanner.scan();
    if (scanResult != null) {
        return scanResult.getClasses();
    }
    throw new RuntimeException("Failed to scan for classes.");
}
```

In this patch, I have removed the pattern matching feature that was introduced in Java 14. This feature might not be supported by the version of Java that you are using. Instead, I have used a null check to verify that the scan was successful. If the scan result is not null, then the classes are returned. Otherwise, a runtime exception is thrown.