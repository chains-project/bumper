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
        if (new FilterBuilder().include(e -> e.startsWith(regex) && e.endsWith(".class")).test(s)) {
            return true;
        }
    }
    return false;
}
```

The main change is the usage of the new `test` method instead of the removed `apply` method for `FilterBuilder`. The lambda expressions are used to define the filtering logic.