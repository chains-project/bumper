```java
private boolean shouldScan(String s) {
    String packagesToScan = System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(".+\\.class").apply(s);
    }
    String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(regex).apply(s)) {
            return true;
        }
    }
    return false;
}
```