```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return s.endsWith(".class");
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        if (s.contains(packageToScan.replace(".", "/")) && s.endsWith(".class")) {
            return true;
        }
    }
    return false;
}
```