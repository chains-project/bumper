Here is the updated `shouldScan` method that should resolve the error:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan) == null || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(".+\\.class").get(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(regex).get(s)) {
            return true;
    }
    return false;
}
```

The changes made are:

* Replace `.apply(s)` with `.get(s)` on the `org.reflections.util.FilterBuilder` instances.

The `.get(s)` method was added in the updated library version and can be used instead of `.apply(s)` to test if a string matches a given pattern.