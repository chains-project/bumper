Here's a proposed patch to fix the error:
```java
static List<String> getClassesLoc(File testSrcFolder) {
    DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses();
}
```
Change the line:
```java
DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard());
```
To:
```java
DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, () -> TestListResolver.getWildcard());
```
The patch creates a lambda expression that returns the wildcard value from the `TestListResolver` class, instead of calling the `getWildcard()` method directly. This allows the code to compile without the need for the removed `getWildcard()` method.