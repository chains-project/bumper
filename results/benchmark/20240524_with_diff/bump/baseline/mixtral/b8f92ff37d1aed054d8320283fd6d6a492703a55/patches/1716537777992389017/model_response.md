Here's the updated method with the necessary changes to fix the error:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

The change is to create a new method `getTestListResolver()` that returns a new instance of `TestListResolver`, and then use it to call the `getWildcard()` method. This way, the error is resolved without relying on the deprecated `TestListResolver.getWildcard()` method.