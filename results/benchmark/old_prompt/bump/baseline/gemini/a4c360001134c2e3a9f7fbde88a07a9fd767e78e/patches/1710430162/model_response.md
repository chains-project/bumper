```java
  private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
      return new FilterBuilder().include(".+\\.class").apply(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
      String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
      if (new FilterBuilder().include(regex).apply(s)) {
        return true;
      }
    }
    return false;
  }
```