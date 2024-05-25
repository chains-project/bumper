Here is a possible patch for the code:

```java
    static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        Collection<String> classes = directoryScanner.scan().getMatchingFiles();
        List<String> classNames = new ArrayList<>();
        for (String classPath : classes) {
            classNames.add(classPath.substring(classPath.lastIndexOf('/') + 1, classPath.length() - 5));
        }
        return classNames;
    }
```

In this patch, we first get the matching files using the `getMatchingFiles()` method instead of `getClasses()`, as the latter might not be available in the updated version of the external dependency.

Then, we create a new list of class names by extracting the file names from the matching files and removing the file extension.

Note that this patch assumes that the `DirectoryScanner` class and the `getMatchingFiles()` method are still available in the updated version of the external dependency. If this is not the case, you may need to find a different solution.