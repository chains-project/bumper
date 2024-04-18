Here's a proposed patch to fix the error:
```
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".+\\.class").test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(regex).test(s)) {
            return true;
        }
    }
    return false;
}
```
The changes made were:

* `FilterBuilder().include(".+\\.class").apply(s)` was changed to `FilterBuilder().include(".+\\.class").test(s)`
* `FilterBuilder().include(regex).apply(s)` was changed to `FilterBuilder().include(regex).test(s)`


The `test()` method is a new addition in the updated library version, which can be used instead of `apply()` to check if a given string matches the filter.