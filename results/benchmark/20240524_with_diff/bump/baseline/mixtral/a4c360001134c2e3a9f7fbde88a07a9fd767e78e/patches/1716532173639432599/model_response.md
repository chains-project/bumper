Here's the fixed version of the `shouldScan` method:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(e -> e.endsWith(".class")).test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(e -> e.startsWith(regex) && e.endsWith(".class")).test(s)) {
            return true;
        }
    }
    return false;
}
```

The main changes are:

1. Replacing the `apply` method with the new `test` method for `FilterBuilder` and `FilterBuilder$Include`.
2. Refactoring the regular expressions to use a lambda expression with `startsWith` and `endsWith` methods for filtering the file names.