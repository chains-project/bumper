Here's a patch for the given code:
```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".+\\.class").matches(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan.trim());
        if (new FilterBuilder().include(regex).matches(s)) {
            return true;
        }
    }
    return false;
}
```
Changes made:

* Replaced `apply` method with `matches` method for `FilterBuilder` as `apply` method is not a standard method for `FilterBuilder` and might have been removed in the new version.
* Added `trim` method for `packageToScan` variable to remove any unwanted white spaces.

Note: The changes made in the code are based on assumptions as there is no information about the `FilterBuilder` class and its methods. If `FilterBuilder` class or its methods are not changed, then it's recommended to use `apply` method instead of `matches` method to maintain consistency in the code.