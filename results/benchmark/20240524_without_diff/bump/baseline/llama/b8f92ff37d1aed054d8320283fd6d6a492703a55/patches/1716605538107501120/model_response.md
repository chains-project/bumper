```java
private boolean classToInclude(String className) {
    boolean matchesExclude = false;
    for (String pattern : config.getJacocoExcludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            matchesExclude = true;
            break;
        }
    }
    if (matchesExclude) {
        return false;
    }

    boolean matchesInclude = false;
    for (String pattern : config.getJacocoIncludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            matchesInclude = true;
            break;
        }
    }
    if (matchesInclude) {
        return true;
    }

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