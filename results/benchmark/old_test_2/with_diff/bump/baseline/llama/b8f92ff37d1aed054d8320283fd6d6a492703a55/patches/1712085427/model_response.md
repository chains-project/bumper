Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
Replace the failing client code with the following code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    List<String> classes = directoryScanner.scan();
    return classes.stream().filter(className -> !className.contains("$")).collect(Collectors.toList());
}
```
The proposed patch adds a filter to the stream of class names returned by `DirectoryScanner.scan()`, which removes any class names that contain a dollar sign ($). This is because the `TestListResolver.getWildcard()` method has changed in the new version of the library, and it no longer includes the dollar sign in the wildcard pattern.

By removing the dollar sign from the class names, the method `getClassesLoc()` will no longer fail with a `NoSuchMethodError` exception. This fix ensures that the method continues to work as expected, returning a list of class names that match the specified wildcard pattern.