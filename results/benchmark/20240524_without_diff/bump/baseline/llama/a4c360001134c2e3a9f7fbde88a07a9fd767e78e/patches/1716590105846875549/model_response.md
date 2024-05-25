```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return s.endsWith(".class");
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        if (s.contains(packageToScan.replace('.', '/')) {
            return true;
        }
    }
    return false;
}
```