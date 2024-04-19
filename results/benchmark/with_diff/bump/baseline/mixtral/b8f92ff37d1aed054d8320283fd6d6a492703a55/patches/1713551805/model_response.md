Here's a proposed patch for the failing client code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

In the new version of the library, the `getWildcard()` method is no longer a static method of `TestListResolver`. Therefore, we need to create an instance of `TestListResolver` and call the `getWildcard()` method on that instance.

Note: I assumed that `TestListResolver` is still in the classpath and can be instantiated. If it's not the case, you may need to adjust the code accordingly.