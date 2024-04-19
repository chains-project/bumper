Here's the updated code snippet that should fix the error:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

The issue is caused by the fact that the `TestListResolver` class no longer has a static `getWildcard()` method. To fix this, we create a new `TestListResolver` instance and call the `getWildcard()` method on it. This way, we avoid using the static method and instead use an instance method.