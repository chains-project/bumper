Here's a fixed version of the `shouldScan` method that uses the `match` method instead of the `apply` method, as the latter is not available in the version of the `FilterBuilder` class being used:

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

Note that I replaced the `apply` method with the `match` method in the following lines:

* `return new org.reflections.util.FilterBuilder().include(".+\\.class").match(s);`
* `if (new org.reflections.util.FilterBuilder().include(regex).match(s)) {`

This should fix the "cannot find symbol" error related to the `apply` method.