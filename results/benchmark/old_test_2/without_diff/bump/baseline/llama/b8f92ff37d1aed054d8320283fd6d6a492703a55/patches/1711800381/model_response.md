Here's a proposed patch to fix the error in the provided code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan().stream()
                .filter(f -> f.endsWith(".class"))
                .map(f -> f.substring(0, f.length() - 6)) // remove .class from the end
                .collect(Collectors.toList());
        return classes;
    }
```
The change made was replacing `directoryScanner.scan().getClasses()` with `directoryScanner.scan().stream().filter(f -> f.endsWith(".class")).map(f -> f.substring(0, f.length() - 6)).collect(Collectors.toList());`

The `getClasses()` method is removed as it is not needed, and instead, we use the `stream()` method to filter and map the files to get the list of class names.