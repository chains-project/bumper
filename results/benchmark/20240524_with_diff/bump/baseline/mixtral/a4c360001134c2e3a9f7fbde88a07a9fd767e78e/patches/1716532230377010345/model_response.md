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

1. Replace the `apply` method with the `test` method in `FilterBuilder` when checking for a match.
2. Use a lambda expression for the `include` method, as the `apply` method has been removed.

This should fix the "cannot find symbol" error related to the missing `apply` method.