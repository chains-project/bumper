Here's a possible patch for the `classToInclude` method:

```java
private boolean classToInclude(String className) {
    if (config.getJacocoIncludes().isEmpty() && config.getJacocoExcludes().isEmpty()) {
        return isClassPresent(config.getBinJavaDir(), className) || isClassPresent(config.getBinTestDir(), className);
    }

    for (String pattern : config.getJacocoExcludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }

    for (String pattern : config.getJacocoIncludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return !isClassPresentInExcluded(config.getJacocoExcludes(), className);
        }
    }

    return isClassPresent(config.getBinJavaDir(), className) || isClassPresent(config.getBinTestDir(), className);
}

private boolean isClassPresent(List<String> dirs, String className) {
    for (String dir : dirs) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), TestListResolver.getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }
    return false;
}

private boolean isClassPresentInExcluded(List<String> excludePatterns, String className) {
    for (String pattern : excludePatterns) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return true;
        }
    }
    return false;
}
```

The patch introduces two helper methods `isClassPresent` and `isClassPresentInExcluded` to simplify the main method. It also moves the check for the presence of the class in the binary directories to the beginning of the method, so it is only executed if no include/exclude patterns are specified. This reduces the number of `DirectoryScanner` instances that need to be created and makes the method more efficient.