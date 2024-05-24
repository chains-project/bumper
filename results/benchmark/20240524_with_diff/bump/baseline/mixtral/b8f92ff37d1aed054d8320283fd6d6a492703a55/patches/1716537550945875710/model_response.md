Here's the updated method with the required changes:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

The change includes creating a new private method `getTestListResolver()` which returns a new instance of `TestListResolver`. This way, the code doesn't depend on the static method `TestListResolver.getWildcard()`.