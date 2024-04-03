Here's the fixed `shouldScan` method with the required changes to adapt to the new library version:

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

The changes include:

1. Replacing `apply` method with the new `test` method in `FilterBuilder`.
2. Changing the `include` method to accept a `Predicate` function instead of a `String`.

These changes allow the code to compile and work with the new library version.