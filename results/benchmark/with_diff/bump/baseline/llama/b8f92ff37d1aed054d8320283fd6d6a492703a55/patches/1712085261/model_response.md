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
DirectoryScanner directoryScanner = new DirectoryScanner(testSrcFolder, TestListResolver.getWildcard() != null ? TestListResolver.getWildcard() : "**/*.class");
```
The patch checks if `TestListResolver.getWildcard()` is null, and if it is, it sets the value of the second parameter of the `DirectoryScanner` constructor to `"**/*.class"` instead. This will tell the `DirectoryScanner` to scan for any file with the ".class" extension in the `testSrcFolder` directory, which should fix the error.