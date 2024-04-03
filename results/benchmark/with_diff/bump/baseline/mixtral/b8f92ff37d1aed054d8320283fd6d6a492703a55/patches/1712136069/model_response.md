Here is a possible patch for the `getClassesLoc` method:
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
This patch creates an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard` method to return the default wildcard. This way, the code no longer depends on the static `getWildcard` method of the `TestListResolver` class, which is no longer available in the new library version.