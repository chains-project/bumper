Here's a proposed patch to fix the error in the failing client code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classNames = directoryScanner.scan().stream()
                .filter(fileName -> fileName.endsWith(".class"))
                .map(fileName -> fileName.substring(0, fileName.length() - 6))
                .collect(Collectors.toList());
        return classNames;
    }
```
The proposed patch uses the `stream()` method to filter the files returned by the `DirectoryScanner` to only include files with the ".class" extension. Then, it uses the `map()` method to remove the ".class" extension from the file names and returns a list of class names.

This patch addresses the error by avoiding the use of the `getClasses()` method, which is not available in the updated version of the dependency. Instead, it uses the `stream()` and `map()` methods to process the file names and extract the class names.