Here's the updated method with the necessary changes to fix the error:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```

The issue is caused by the missing `getWildcard()` method from the `TestListResolver` class. The `TestListResolver` class is instantiated directly, and the `getWildcard()` method is called on the instantiated object. This way, the code should work even with the updated library version.