Here is a possible patch for the `getClassesLoc` method:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, new TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The only change I made is to create a new instance of `TestListResolver` and call `getWildcard()` on it, instead of calling the static method `TestListResolver.getWildcard()`. This is because the `getWildcard` method is no longer static in the new version of the library.

Note that this change may not be sufficient if the `TestListResolver` constructor or the `getWildcard` method have different behavior or require different arguments in the new version. In that case, you may need to modify the code further based on the documentation or implementation of the new version.