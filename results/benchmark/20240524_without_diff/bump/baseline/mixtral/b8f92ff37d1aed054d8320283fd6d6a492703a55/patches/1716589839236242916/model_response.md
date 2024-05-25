Here's the fixed `getClassesLoc` method:

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

The issue was caused by the wrong way of using the `instanceof` operator. I've replaced it with a null check for `scanResult`.