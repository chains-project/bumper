Here's the updated `classToInclude` method with the required changes:

```java
private boolean classToInclude(String className) {
    WildcardMatcher matcher = new WildcardMatcher("");

    // False if it matches an excludes pattern
    for (String pattern : config.getJacocoExcludes()) {
        matcher.setPattern(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }

    // True if it matches an includes pattern and doesn't match any excludes pattern
    for (String pattern : config.getJacocoIncludes()) {
        matcher.setPattern(pattern);
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

The changes include creating a `getTestListResolver()` method to instantiate a `TestListResolver` object and using it to call `getWildcard()`. This ensures that the code compiles with the new version of the library.