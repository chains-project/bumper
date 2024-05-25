```java
private boolean classToInclude(String className) {
    boolean included = false;
    for (String pattern : config.getJacocoIncludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            included = true;
        }
    }
    for (String pattern : config.getJacocoExcludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }
    if (!included) {
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
    }
    return included;
}
```