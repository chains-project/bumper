Here's the patched method using the new library version:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    CommandLineBuilder commandLineBuilder = new CommandLineBuilder();
    return new TestListResolver(commandLineBuilder);
}
```

The fix is to create a new method `getTestListResolver()` that returns a new instance of `TestListResolver`. Since the constructor of `DirectoryScanner` requires a `TestListResolver` instance, we create a new instance using a `CommandLineBuilder`.