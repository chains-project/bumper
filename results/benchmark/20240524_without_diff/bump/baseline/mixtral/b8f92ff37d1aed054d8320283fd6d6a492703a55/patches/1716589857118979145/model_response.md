Here's the fixed method:

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

The issue was caused by the incorrect usage of the `instanceof` operator. I replaced it with a null check on `scanResult`.