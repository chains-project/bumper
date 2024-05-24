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
        File dirFile = new File(dir);
        if (dirFile.exists() && dirFile.isDirectory()) {
            for (File file : dirFile.listFiles()) {
                if (file.isFile() && file.getName().endsWith(".class") && file.getName().replace(".class", "").equals(className)) {
                    return true;
                }
            }
        }
    }
    for (String dir : config.getBinTestDir()) {
        File dirFile = new File(dir);
        if (dirFile.exists() && dirFile.isDirectory()) {
            for (File file : dirFile.listFiles()) {
                if (file.isFile() && file.getName().endsWith(".class") && file.getName().replace(".class", "").equals(className)) {
                    return true;
                }
            }
        }
    }

    return false;
}
```