Here's a possible patch for the `classToInclude` method:

```java
private boolean classToInclude(String className) {
    if (config.getJacocoIncludes().isEmpty() && config.getJacocoExcludes().isEmpty()) {
        return isClassPresentInAnyDir(className, config.getBinJavaDir())
            || isClassPresentInAnyDir(className, config.getBinTestDir());
    }

    boolean matchesIncludePattern = false;
    for (String pattern : config.getJacocoIncludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            matchesIncludePattern = true;
            break;
        }
    }

    if (matchesIncludePattern) {
        for (String pattern : config.getJacocoExcludes()) {
            WildcardMatcher matcher = new WildcardMatcher(pattern);
            if (matcher.matches(className)) {
                return false;
            }
        }
        return true;
    }

    return false;
}

private boolean isClassPresentInAnyDir(String className, List<String> dirs) {
    return dirs.stream()
        .anyMatch(dir -> isClassPresentInDir(className, dir));
}

private boolean isClassPresentInDir(String className, String dir) {
    DirectoryScanner directoryScanner = new DirectoryScanner(new File(dir), TestListResolver.getWildcard());
    return directoryScanner.scan().getClasses().contains(className);
}
```

The patch checks if the `jacocoIncludes` and `jacocoExcludes` lists are empty. If so, it checks if the class is present in any of the binary directories. This way, we avoid creating `DirectoryScanner` objects and `WildcardMatcher` objects when they are not needed.

The `isClassPresentInAnyDir` method checks if the class is present in any of the directories in the list. The `isClassPresentInDir` method checks if the class is present in a single directory.

Note that this patch assumes that the `config.getBinJavaDir()` and `config.getBinTestDir()` methods return lists of directories. If they return arrays, you should modify the code accordingly.