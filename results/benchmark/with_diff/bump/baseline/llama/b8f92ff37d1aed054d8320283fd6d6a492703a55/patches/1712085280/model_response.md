Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        return directoryScanner.scan().getClasses();
    }
```
Modified code:
```java
static List<String> getClassesLoc(File testSrcFolder) {
        DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
        List<String> classes = directoryScanner.scan();
        return classes.stream().filter(className -> !className.contains("$")).collect(Collectors.toList());
    }
```
Explanation:

The error is caused by the fact that the `TestListResolver` class has been updated to use a different method to retrieve the wildcard, which is not compatible with the version of the Surefire plugin that is being used.

In the modified code, we use the `filter` method to remove any classes that contain a dollar sign ($), which is the identifier for the wildcard character in the new version of Surefire. This should fix the issue and allow the code to compile without errors.