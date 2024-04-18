Here is a possible patch for the failing method:
```java
    static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver(){
            @Override
            protected String getWildcard() {
                return TestListResolver.WILDCARD;
            }
        });
        return directoryScanner.scan().getClasses();
    }
```
In this patch, I created an anonymous inner class that extends `TestListResolver` and overrides the `getWildcard()` method to return the wildcard string. This way, the `DirectoryScanner` constructor can still accept a `TestListResolver` object, even though the `getWildcard()` method is no longer a static method in the new version of the library.