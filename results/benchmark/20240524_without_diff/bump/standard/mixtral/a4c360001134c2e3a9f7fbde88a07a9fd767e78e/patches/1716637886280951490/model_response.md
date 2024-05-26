Here's the patched method:

```java
private boolean shouldScan(java.lang.String s) {
    final java.lang.String packagesToScan = java.lang.System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_TO_SCAN);
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(new org.reflections.util.ClasspathHelper().forClassLoader()).matcher(s);
    }
    final java.lang.String[] packages = packagesToScan.split(",");
    for (java.lang.String packageToScan : packages) {
        java.lang.String regex = java.lang.String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(new org.reflections.util.ClasspathHelper().forPackage(packageToScan)).matcher(s)) {
            return true;
        }
    }
    return false;
}
```

The `apply` method has been replaced with `matcher` for the `FilterBuilder` instances. Also, a new `ClasspathHelper` instance is used to get the classpath for the classloader and the package.