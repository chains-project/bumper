Here's a fixed version of the `getClassesLoc` method that should work with the updated library:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

The change here is that we create a new instance of `TestListResolver` and call `getWildcard()` on it. This is because the `getWildcard()` method is no longer a static method in the new version of the library.