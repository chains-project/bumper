Here's the updated `getClassesLoc` method with the necessary changes to fix the error:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The change is creating a new instance of `TestListResolver` instead of using the static method `TestListResolver.getWildcard()`. This is due to the removal of the static `getWildcard()` method in the updated library version.