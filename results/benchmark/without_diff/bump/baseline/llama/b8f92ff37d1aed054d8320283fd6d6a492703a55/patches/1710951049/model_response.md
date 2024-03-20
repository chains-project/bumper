Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        return directoryScanner.scan().getClasses().stream()
                .filter(className -> !className.contains("$"))
                .collect(Collectors.toList());
    }
```
The `DirectoryScanner` class has been updated to use the `stream()` method to filter out classes that contain a dollar sign (`$`). The `filter()` method is used to remove classes with the dollar sign, and the resulting list of classes is collected using `Collectors.toList()`.

This patch addresses the error by excluding classes with dollar signs in their names, which are likely to be inner classes or anonymous classes that are not meant to be loaded as separate classes.