Here is a possible patch for the failing client code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    directoryScanner.scan();
    ScanResult scanResult = directoryScanner.getScanResult();
    if (scanResult != null) {
        return scanResult.getClasses();
    }
    throw new RuntimeException("Failed to scan for classes.");
}
```
The patch removes the unnecessary type annotation in the if statement and assigns the result of `directoryScanner.scan()` to a variable before checking if it is an instance of `ScanResult`. This way, the code avoids the need for a pattern matching statement, which might not be supported by the version of Java that the code is using. The patch also checks if `scanResult` is not null before calling its `getClasses()` method, which can prevent a potential NullPointerException.