private boolean shouldScan(java.lang.String s) {
    final java.lang.String packagesToScan = java.lang.System.getenv(com.thoughtworks.gauge.GaugeConstant.PACKAGE_java.lang.String.format("%sTO_SCAN", "PACKAGE"));
    if ((packagesToScan == null) || packagesToScan.isEmpty()) {
        return new org.reflections.util.FilterBuilder().include(java.util.function.Predicate.isEqual(s + ".class")).test(s);
    }
    final java.lang.String[] packages = packagesToScan.split(",");
    for (java.lang.String packageToScan : packages) {
        java.lang.String regex = java.lang.String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new org.reflections.util.FilterBuilder().include(java.util.function.Predicate.isEqual(regex)).test(s)) {
            return true;
        }
    }
    return false;
}