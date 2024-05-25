Here's a possible patch for the `classToInclude` method:

```java
private boolean classToInclude(String className) {
    if (config.getJacocoIncludes().isEmpty() && config.getJacocoExcludes().isEmpty()) {
        return isClassPresentInBinDirectories(className);
    }

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

    return isClassPresentInBinDirectories(className);
}

private boolean isClassPresentInBinDirectories(String className) {
    for (String dir : config.getBinJavaDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), TestListResolver.getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }
    for (String dir : config.getBinTestDir()) {
        DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), TestListResolver.getWildcard());
        if (directoryScanner.scan().getClasses().contains(className)) {
            return true;
        }
    }

    return false;
}
```

This patch checks if there are any include or exclude patterns. If there are none, it directly checks if the class is present in the binary directories. This way, it avoids creating a `WildcardMatcher` instance and calling the `matches` method, which might be causing the "cannot find symbol" error.