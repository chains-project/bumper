Here is a possible patch for the given code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    Collection<String> classes = new ArrayList<>();
    for (File file : directoryScanner.scan().getFiles()) {
        if (file.isFile() && file.getName().endsWith(".class")) {
            classes.add(file.getAbsolutePath());
        }
    }
    return new ArrayList<>(classes);
}
```

This patch uses the `getFiles()` method of the `ScanResult` class, which is an added method in the new version of the library. It also creates a new `ArrayList` from the `classes` collection before returning it. This is because the `getClasses()` method is not available in the new version of the library.