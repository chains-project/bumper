Here's a possible patch to fix the error:
```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan().stream()
                .filter(className -> !className.contains("$"))
                .map(className -> testSrcFolder.getAbsolutePath() + File.separator + className)
                .collect(Collectors.toList());
        return classes;
    }
```
The patch removes the usage of `getClasses()` method from `DirectoryScanner` which is not available in the current version of the library. Instead, it uses the `stream()` method to filter and map the files found by the `DirectoryScanner` to a list of class names, and then collects them into a list.

Please note that this patch is just a proposal, it's important to test it thoroughly before applying it to a production environment.