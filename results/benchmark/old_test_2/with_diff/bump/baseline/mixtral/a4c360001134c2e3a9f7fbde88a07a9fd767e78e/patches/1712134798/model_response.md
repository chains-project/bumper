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
        if (new FilterBuilder().include(e -> e.matches(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

The changes include:

1. Replacing `apply` with `test` for `FilterBuilder.include()`.
2. Changing the argument for `include` to a lambda expression that checks if the string ends with `.class` or matches the given regex.

This patch ensures that the code uses the new method signature of `test` instead of the removed `apply`, and utilizes the lambda expression for the `include` method.