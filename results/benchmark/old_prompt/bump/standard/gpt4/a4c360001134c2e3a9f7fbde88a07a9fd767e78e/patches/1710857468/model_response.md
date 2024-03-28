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
The method `apply` does not exist in the `FilterBuilder` class. Instead, you should use the `test` method. The `test` method is a functional interface method in `java.util.function.Predicate`, which `FilterBuilder` implements. It evaluates this predicate on the given argument, which is the same functionality as the non-existent `apply` method.