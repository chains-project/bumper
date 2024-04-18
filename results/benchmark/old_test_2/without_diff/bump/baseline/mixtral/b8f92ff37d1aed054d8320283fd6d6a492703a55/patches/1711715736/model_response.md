Here is a possible patch for the failing code:
```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        directoryScanner.scan();
        List<String> classes = new ArrayList<>();
        for (String classFile : directoryScanner.getIncludedFiles()) {
            classes.add(classFile.substring(0, classFile.length() - 6));
        }
        return classes;
    }
```
This patch uses a different approach to extract the class names from the scanned files. Instead of calling `getClasses()` on the `DirectoryScanner` object, it iterates over the included files and manually extracts the class names by removing the ".class" suffix.

Note that the `DirectoryScanner` class is not part of the standard Java library, so it is not possible to say for sure whether this patch will work without more context about the library that provides this class. However, this patch should at least be a good starting point for further investigation.