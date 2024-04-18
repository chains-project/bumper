Here's a possible patch for the given code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    Collection<SpoonAPI> scannedElements = directoryScanner.scan();
    if (scannedElements instanceof Collection) {
        return ((Collection<SpoonAPI>) scannedElements).stream()
            .filter(SpoonAPI::isType)
            .map(SpoonAPI::getQualifiedName)
            .collect(Collectors.toList());
    }
    throw new IllegalStateException("scan() method did not return a Collection");
}
```

This patch uses the `SpoonAPI` interface's `isType()` and `getQualifiedName()` methods to filter and map the scanned elements to their qualified names. These methods were added in a newer version of the library, so they should be available in the updated version that is causing the compilation error.

Note that this patch assumes that the `scan()` method always returns a `Collection` of some sort. If this is not the case, a more robust error-handling mechanism would be needed.