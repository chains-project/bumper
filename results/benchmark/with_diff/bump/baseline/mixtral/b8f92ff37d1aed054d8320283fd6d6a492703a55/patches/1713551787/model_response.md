Here's the proposed patch for the failing client code:

```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, getTestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}

private static TestListResolver getTestListResolver() {
    ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
    try {
        return classLoader.loadClass("org.apache.maven.surefire.api.testset.TestListResolver")
            .asSubclass(TestListResolver.class)
            .getDeclaredConstructor()
            .newInstance();
    } catch (ReflectiveOperationException e) {
        throw new RuntimeException("Failed to create TestListResolver instance", e);
    }
}
```

This patch introduces a new private method `getTestListResolver()` that uses reflection to load the required class and create an instance of `TestListResolver`. This way, the code is not dependent on the static method `TestListResolver.getWildcard()`, and it should work with the new version of the library.