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
In the original code, the `TestListResolver.getWildcard()` method is removed in the new version of the library, so we need to replace it with an alternative method that achieves the same result.

We can use the `DirectoryScanner.scan()` method to get a list of files in the directory, and then filter out any files that contain a dollar sign ("$"), which is the wildcard character used in the `TestListResolver.getWildcard()` method.

This change should fix the error and allow the code to compile and run correctly.