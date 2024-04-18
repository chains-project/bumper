Here's a proposed patch to fix the error in the failing client code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan().stream()
                .filter(f -> f.endsWith(".class"))
                .map(f -> f.substring(0, f.length() - 6))
                .collect(Collectors.toList());
        return classes;
    }
```
The proposed patch uses the `stream()` method to filter the files returned by the `DirectoryScanner` to only include files with the `.class` extension. Then, it uses the `map()` method to remove the `.class` extension from the file names, and finally, it collects the resulting list of file names to a list of strings using the `Collectors.toList()` method.

This patch addresses the error by avoiding the use of the `getClasses()` method, which is not available in the updated version of the dependency. Instead, it uses the `stream()` method to process the files returned by the `DirectoryScanner` and extract the class names.