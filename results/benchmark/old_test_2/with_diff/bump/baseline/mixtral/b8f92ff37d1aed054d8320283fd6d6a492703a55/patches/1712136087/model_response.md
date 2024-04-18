Here's the proposed patch for the `getClassesLoc` method:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver() {
        @Override
        protected String getWildcard() {
            return "";
        }
    }.getWildcard());
    return directoryScanner.scan().getClasses();
}
```

In this patch, we create an anonymous inner class that extends `TestListResolver` and provides a custom implementation for the `getWildcard()` method. This way, we can avoid using the removed `TestListResolver.getWildcard()` method and still provide the necessary parameter for the `DirectoryScanner` constructor. Note that we're returning an empty string for the wildcard, which might not be suitable for your specific use case. You may need to adjust the implementation to better fit your requirements.