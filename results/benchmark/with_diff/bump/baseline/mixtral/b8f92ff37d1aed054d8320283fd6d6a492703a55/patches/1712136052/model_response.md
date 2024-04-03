Here's the proposed patch to fix the error in the client code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver() {
        @Override
        protected String getWildcard() {
            return TestListResolver.getWildcard();
        }
    });
    return directoryScanner.scan().getClasses();
}
```

The change creates an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard()` method to fix the compilation error.