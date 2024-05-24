Here's the fixed `shouldScan` method:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(e -> e.endsWith(".class")).test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(e -> e.startsWith(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

The changes made are:

1. Replaced the `apply` method with `test` for `FilterBuilder$Include`.
2. Changed the `include` method to accept a `Predicate` instead of a `String`.
3. Modified the `Predicate` implementation to match the required conditions.

These changes make use of the new methods added in the updated library version, and avoid using the removed ones.