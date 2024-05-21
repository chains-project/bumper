Here's the proposed patch for the `shouldScan` method:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".+\\.class").filter(s).isTrue();
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(regex).filter(s).isTrue()) {
            return true;
        }
    }
    return false;
}
```

The changes made are:

1. Replace `org.reflections.util.FilterBuilder` with `org.reflections.util.ConfigurationBuilder.FilterBuilder`.
2. Replace `.apply(s)` with `.filter(s).isTrue()`.

This patch uses the `ConfigurationBuilder.FilterBuilder` class which has the `include` method and returns a `Filter` instance. The `Filter` instance has the `filter` method which can be used to filter a string and returns a `Filter` instance again. The `isTrue` method can be used to check if the filter matches the input string.