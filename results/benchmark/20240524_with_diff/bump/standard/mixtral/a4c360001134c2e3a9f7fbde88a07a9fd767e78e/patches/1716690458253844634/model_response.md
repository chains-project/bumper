Here's the fixed version of the `shouldScan` method:
```java
private boolean shouldScan(java.lang.String s) {
    final java.lang.String packagesToScan = java.lang.System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(".+\\.class").test(s);
    }
    final java.lang.String[] packages = packagesToScan.split(",");
    for (java.lang.String packageToScan : packages) {
        java.lang.String regex = java.lang.String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(regex).test(s)) {
            return true;
        }
    }
    return false;
}
```
The changes I made are:

* Replace `apply` with `test` for `FilterBuilder` instances.
* The `FilterBuilder` class no longer has an `apply` method, but it has a `test` method that serves the same purpose.
* The `Predicate` type used for the `add` method has changed from `com.google.common.base.Predicate` to `java.util.function.Predicate`.