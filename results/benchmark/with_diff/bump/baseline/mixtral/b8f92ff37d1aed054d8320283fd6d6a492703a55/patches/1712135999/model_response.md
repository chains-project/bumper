Here is a possible patch for the `getClassesLoc` method:
```java
    static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver() {
            @Override
            protected String getWildcard() {
                return ""; // replace with the appropriate wildcard for your use case
            }
        });
        return directoryScanner.scan().getClasses();
    }
```
This patch creates an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard` method to return an empty string. You should replace the empty string with the appropriate wildcard for your use case.

The reason for this patch is that the `TestListResolver` class no longer has a `getWildcard` method in the new library version. By creating an inner class that extends `TestListResolver` and overriding the `getWildcard` method, we can provide the necessary implementation ourselves.

Note that this patch assumes that the `DirectoryScanner` constructor that takes a `TestListResolver` argument is still available in the new library version. If this constructor is no longer available, you may need to modify the patch accordingly.