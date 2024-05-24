Here's the updated method with the necessary changes to fix the error:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        FilterBuilder filterBuilder = new FilterBuilder();
        return filterBuilder.include(String.format(".+\\.class")).test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        FilterBuilder filterBuilder = new FilterBuilder();
        if (filterBuilder.include(regex).test(s)) {
            return true;
        }
    }
    return false;
}
```

The main change is the use of the `test` method instead of `apply` for the `FilterBuilder`. The `FilterBuilder` has been reinitialized before every test.