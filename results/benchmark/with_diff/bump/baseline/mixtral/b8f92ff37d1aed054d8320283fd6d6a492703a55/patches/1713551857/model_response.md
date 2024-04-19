Here is a possible patch for the `getClassesLoc` method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```
The change consists of creating a new method `getTestListResolver` that returns a new instance of `TestListResolver`, and using this method to get the `TestListResolver` instance in the `getClassesLoc` method. This way, the `getClassesLoc` method is no longer dependent on the `TestListResolver` class and can work with the new library version.