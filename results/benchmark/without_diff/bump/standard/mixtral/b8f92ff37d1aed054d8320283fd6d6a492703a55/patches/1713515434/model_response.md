Here's the fixed version of the method using a different approach to get the wildcard:

```java
static java.util.List<java.lang.String> getClassesLoc(java.io.File testSrcFolder) {
    org.apache.maven.plugin.surefire.util.DirectoryScanner directoryScanner = new org.apache.maven.plugin.surefire.util.DirectoryScanner(testSrcFolder, "**/*.class");
    return directoryScanner.scan().getClasses();
}
```

In this version, we removed the dependency on `org.apache.maven.surefire.api.testset.TestListResolver` and used a hardcoded wildcard string `"**/*.class"` instead. This should work as long as the goal is to find all the class files within the specified directory.