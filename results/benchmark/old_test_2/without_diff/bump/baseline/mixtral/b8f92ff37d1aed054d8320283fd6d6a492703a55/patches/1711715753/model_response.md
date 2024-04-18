Here is a possible patch for the code:
```java
  static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        Collection<String> classes = directoryScanner.scan().getClasses();
        List<String> result = new ArrayList<>();
        for (String clazz : classes) {
            result.add(clazz.replaceAll("\\.", "/") + ".class");
        }
        return result;
    }
```
This patch changes the way the classes are returned from the `DirectoryScanner` object. Instead of returning a list of classes directly, it returns a collection of classes, which are then converted to a list of strings with the correct format (i.e., with "." replaced by "/" and ".class" appended). This should solve the "cannot find symbol" error, as it ensures that the classes are returned in a format that the rest of the code can handle.