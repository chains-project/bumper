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
        if (new FilterBuilder().include(e -> e.matches(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

The main changes are:

1. Replaced `apply` method with `test` method for `FilterBuilder` instances.
2. Replaced `include` method with a lambda expression that checks if the string ends with `.class` or matches a specific regex pattern.

These changes utilize the added `test` method and the lambda expression feature introduced in the updated library version.