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
        if (new FilterBuilder().include(e -> e.startsWith(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

In this version, I replaced the `apply` method with the new `test` method for the `FilterBuilder` class. Also, I changed the `include` method to accept a `Predicate` instead of a `String`. This way, the code uses the new library version's methods and can be compiled successfully.