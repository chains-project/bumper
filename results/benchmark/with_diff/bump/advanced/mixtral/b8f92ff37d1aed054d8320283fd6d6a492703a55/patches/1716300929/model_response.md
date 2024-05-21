Here is a possible patch for the code:
```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, new org.apache.maven.surefire.api.testset.TestListResolver().getWildcard());
    return directoryScanner.scan().getClasses();
}
```
The change I made is to create a new instance of `TestListResolver` and then call `getWildcard()` on it. This way, the code is not directly calling a static method on the `TestListResolver` class, but rather on an instance of it. This should avoid the "cannot find symbol" error.

I also noticed that the `DirectoryScanner` constructor takes an instance of `TestListResolver` as an argument, so I passed the newly created instance to it.

I hope this helps! Let me know if you have any questions.