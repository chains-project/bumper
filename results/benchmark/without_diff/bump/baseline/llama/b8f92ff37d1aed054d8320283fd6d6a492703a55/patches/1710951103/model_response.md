Here's a proposed patch to fix the error in the provided code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        return directoryScanner.scan().stream()
                .filter(className -> !className.contains("$"))
                .map(className -> testSrcFolder + File.separator + className)
                .collect(Collectors.toList());
    }
```
The proposed patch makes the following changes to the original code:

1. Instead of using `DirectoryScanner.scan().getClasses()`, which is deprecated, we use `DirectoryScanner.scan().stream()` to iterate over the files in the directory.
2. We filter out any file names that contain a '$' character, as these are likely to be inner classes or anonymous classes, which should not be included in the list of classes.
3. We use `map()` to transform each file name into a fully qualified class name by concatenating the testSrcFolder path and the file name separated by a File.separator.
4. Finally, we collect the transformed list of class names into a List<String> using `Collectors.toList()`.

This patch should fix the error and provide a list of fully qualified class names located in the test source folder.