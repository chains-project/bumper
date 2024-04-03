Here's the proposed patch for the `getClassesLoc` method:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver() {
        @Override
        protected String getWildcard() {
            return "**/*.class";
        }
    });
    return directoryScanner.scan().getClasses();
}
```

The patch creates an anonymous inner class that extends `TestListResolver` and provides the missing `getWildcard` method. This allows the code to work with the new version of the library.