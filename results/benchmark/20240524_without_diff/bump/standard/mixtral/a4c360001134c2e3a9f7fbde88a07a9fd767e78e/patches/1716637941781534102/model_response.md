Here's a fixed version of the `shouldScan` method. I replaced the usage of `apply(s)` with `match(s)` for the `FilterBuilder` class.

```java
private boolean shouldScan(java.lang.String s) {
    final java.lang.String packagesToScan = java.lang.System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(".+\\.class").match(s);
    }
    final java.lang.String[] packages = packagesToScan.split(",");
    for (java.lang.String packageToScan : packages) {
        java.lang.String regex = java.lang.String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(regex).match(s)) {
            return true;
        }
    }
    return false;
}
```

This should resolve the error related to the `apply` method not being found for the `FilterBuilder` class.