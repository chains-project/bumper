Here's a proposed patch to fix the error in the provided code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        return directoryScanner.scan().getClasses(classLoader);
    }
```
The patch adds a `ClassLoader` object to the `DirectoryScanner` constructor, passing `Thread.currentThread().getContextClassLoader()` as an argument. This sets the class loader to the current thread's context class loader, which should fix the error.

With this change, the `DirectoryScanner` will use the correct class loader to scan for classes, and the `cannot find symbol` error should be resolved.