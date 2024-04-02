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
The proposed patch adds a filter step to the stream returned by `directoryScanner.scan()`, which removes any class names that contain a dollar sign ("$"), which is a common indicator of a synthetic class. This change should allow the method to compile without issues.