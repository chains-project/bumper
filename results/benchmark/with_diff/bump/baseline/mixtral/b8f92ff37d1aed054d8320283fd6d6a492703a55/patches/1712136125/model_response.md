Here's a possible patch for the `getClassesLoc` method to fix the error:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver() {
        @Override
        protected String getWildcard() {
            return TestListResolver.getDefaultWildcard();
        }
    });
    return directoryScanner.scan().getClasses();
}
```

The patch creates an anonymous subclass of `TestListResolver` and overrides the `getWildcard` method to call the `getDefaultWildcard` method instead of the original `getWildcard` method, which was removed in the new library version.