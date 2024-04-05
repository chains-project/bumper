Here is a fixed version of the `getClassesLoc` method that uses a different approach to get the wildcard:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, getWildcard());
    return directoryScanner.scan().getClasses();
}

static String getWildcard() {
    return "**/*.class";
}
```

In this version, I added a new method `getWildcard` that returns the wildcard string. This way, the `DirectoryScanner` constructor uses the wildcard returned by `getWildcard` method. This should fix the error.