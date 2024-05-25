Here's a proposed patch for the `classToInclude` method:

```java
private boolean classToInclude(String className) {
    if (config.getJacocoIncludes().stream()
        .map(pattern -> new WildcardMatcher(pattern))
        .anyMatch(matcher -> matcher.matches(className))) {
        return true;
    }

    for (String pattern : config.getJacocoExcludes()) {
        WildcardMatcher matcher = new WildcardMatcher(pattern);
        if (matcher.matches(className)) {
            return false;
        }
    }

    File binJavaDir = new File(config.getBinJavaDir().get(0));
    File binTestDir = new File(config.getBinTestDir().get(0));

    if (Arrays.stream(binJavaDir.listFiles((dir, name) -> name.equals(className)))
        .findFirst()
        .isPresent()
        || Arrays.stream(binTestDir.listFiles((dir, name) -> name.equals(className)))
        .findFirst()
        .isPresent()) {
        return true;
    }

    return false;
}
```

This patch uses Java 8 features such as streams and lambda expressions to simplify the code and avoid using external libraries where possible. It also uses the `File.listFiles` method to check if the class exists in the binary directories.

Note that this patch assumes that `config.getBinJavaDir()` and `config.getBinTestDir()` always return a non-empty list. If this is not the case, you may need to modify the code accordingly.