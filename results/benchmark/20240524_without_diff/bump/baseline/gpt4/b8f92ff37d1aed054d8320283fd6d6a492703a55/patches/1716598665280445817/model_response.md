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
            File directory = new File(dir);
            if(directory.exists() && directory.isDirectory()) {
                DirectoryScanner directoryScanner = new DirectoryScanner(directory, TestListResolver.getWildcard());
                if (directoryScanner.scan().getClasses().contains(className)) {
                    return true;
                }
            }
        }
        for (String dir : config.getBinTestDir()) {
            File directory = new File(dir);
            if(directory.exists() && directory.isDirectory()) {
                DirectoryScanner directoryScanner = new DirectoryScanner(directory, TestListResolver.getWildcard());
                if (directoryScanner.scan().getClasses().contains(className)) {
                    return true;
                }
            }
        }

        return false;
    }
```