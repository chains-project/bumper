```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv("PACKAGE_TO_SCAN");
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return Pattern.compile(".+\\.class").matcher(s).matches();
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (Pattern.compile(regex).matcher(s).matches()) {
            return true;
        }
    }
    return false;
}
```