Here's the fixed version of the method using the new library version:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

I created a helper method `getTestListResolver()` to create a new instance of `TestListResolver` because the `getWildcard()` method is now an instance method instead of a static method.