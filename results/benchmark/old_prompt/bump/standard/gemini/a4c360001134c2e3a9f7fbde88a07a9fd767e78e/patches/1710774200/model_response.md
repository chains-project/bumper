```java
private boolean shouldScan(java.lang.String s) {
    final java.lang.String packagesToScan = java.lang.System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(org.reflections.util.FilterBuilder.matchAny(s)).apply(s);
    }
    final java.lang.String[] packages = packagesToScan.split(",");
    for (java.lang.String packageToScan : packages) {
        java.lang.String regex = java.lang.String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(regex).apply(s)) {
            return true;
        }
    }
    return false;
}
```