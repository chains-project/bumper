Here's a patch for the `shouldScan` method. The issue seems to be caused by the use of the `FilterBuilder` class which is no longer available. I replaced it with a simple implementation using regular expressions:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return s.endsWith(".class");
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".*\\.?%s\\..+\\.class", packageToScan.replaceAll("\\.", "\\."));
        if (s.matches(regex)) {
            return true;
        }
    }
    return false;
}
```

This implementation has the same behavior as the original code, but uses Java's built-in `String#matches` method with a regular expression instead of the `FilterBuilder`. This should resolve the compilation error.