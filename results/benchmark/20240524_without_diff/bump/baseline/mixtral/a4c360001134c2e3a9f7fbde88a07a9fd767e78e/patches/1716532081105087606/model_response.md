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

The following changes have been made:

1. The `apply` method has been replaced with `test` for both `FilterBuilder.Include` and `FilterBuilder.Exclude`.
2. A lambda expression has been used to create the required `Predicate` instances.
3. The lambda expressions use the `endsWith` and `matches` methods to test the input string.

Note that the `FilterBuilder.apply` method has been removed in the updated library. Instead, the `test` method should be used with a lambda expression to define the filtering logic.