Here's the fixed version of the `classToInclude` method that takes into account the changes in the new library version:

```java
private boolean classToInclude(String className) {
    // False if it matches an excludes pattern
    for (String pattern : config.getJacocoExcludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }
    // True if it matches an includes pattern and doesn't match any excludes pattern
    for (String pattern : config.getJacocoIncludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return true;
        }
    }

    // True if it is present in the available binaries
    for (String dir : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), getTestListResolver().getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }
    for (String dir : config.getBinTestDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), getTestListResolver().getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }

    return false;
}

private TestListResolver getTestListResolver() {
    return new TestListResolver();
}
```

The main change is the introduction of the `getTestListResolver()` method that returns a new instance of `TestListResolver`. This allows the usage of the `getWildcard()` method, which was moved to this class in the new library version.