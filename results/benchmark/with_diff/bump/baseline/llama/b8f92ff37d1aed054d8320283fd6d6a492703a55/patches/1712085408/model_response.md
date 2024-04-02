Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    List<String> classes = directoryScanner.scan();
    classes.stream().filter(className -> !className.contains("$")).collect(Collectors.toList());
    return classes;
}
```
Explanation:

The error is caused by the fact that the `TestListResolver` class has been updated to use a different method to get the wildcard, which is not compatible with the version of the Surefire plugin that is being used.

To fix the error, we can use the `getWildcard()` method from the `TestListResolver` class, which is available in the new version of the Surefire plugin. We can also remove the `Override` annotation, as it is not needed.

Additionally, we can simplify the code by using a stream to filter out classes that contain a dollar sign, instead of using the `ArrayList` and `Iterator` classes.

This patch should fix the error and allow the code to compile and run correctly.