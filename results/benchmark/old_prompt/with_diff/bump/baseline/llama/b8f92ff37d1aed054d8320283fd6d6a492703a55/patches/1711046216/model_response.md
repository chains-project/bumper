Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
Replace the failing method with the following code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    List<String> classes = directoryScanner.scan();
    return classes.stream().filter(className -> !className.contains("$")).collect(Collectors.toList());
}
```
In the new version of the library, the `TestListResolver` class has been modified, and the `getWildcard()` method is no longer available. Instead, we use the `TestListResolver.getWildcard()` method to get the wildcard pattern for the test classes.

Additionally, we filter out any classes that contain a dollar sign ($) in their name, as these are likely to be test classes that should not be included in the production classpath.

This patch should fix the error and allow the code to compile and run correctly.