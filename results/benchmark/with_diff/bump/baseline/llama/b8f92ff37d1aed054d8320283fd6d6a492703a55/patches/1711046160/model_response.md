Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        return directoryScanner.scan().getClasses();
    }
```

We can see that the `TestListResolver` class has been modified in the new library version, and the `getWildcard()` method is no longer available. Instead, we can use the `getClasses()` method of the `DirectoryScanner` class to get a list of classes.

Here's the modified code that should fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder);
        return directoryScanner.getClasses();
    }
```
By removing the `TestListResolver` dependency and using the `DirectoryScanner` class directly, we can fix the error and make the code compatible with the new library version.