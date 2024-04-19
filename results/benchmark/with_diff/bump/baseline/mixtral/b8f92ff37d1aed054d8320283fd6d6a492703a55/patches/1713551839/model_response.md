Here's the updated `getClassesLoc` method that should work with the new library version:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    return new DefaultSurefireTestSetFactory().createTestSetManagerProvider(null).createTestSetFactory(null).getTestListResolver();
}
```

The issue is caused by the fact that the `TestListResolver.getWildcard()` method is not static in the new library version. To fix this, you need to create an instance of `TestListResolver` and then call the `getWildcard()` method on that instance.

To create the instance of `TestListResolver`, you need to go through a series of classes that use to have a default constructor, but now require a null argument.

Note that this solution assumes that you are using Surefire 3.0.0-M5 or later. If you are using an earlier version, you may need to adjust the code accordingly.