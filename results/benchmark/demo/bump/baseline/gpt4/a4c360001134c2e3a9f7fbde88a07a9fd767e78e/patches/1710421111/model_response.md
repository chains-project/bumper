```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".+\\.class").match(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(regex).match(s)) {
            return true;
        }
    }
    return false;
}
```
In the above code, I have replaced the `apply(s)` method with `match(s)`. The error message suggests that the `apply(s)` method does not exist in the `FilterBuilder` class, so I replaced it with the `match(s)` method, which is a common method in filtering classes.