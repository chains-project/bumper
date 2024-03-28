Here's a proposed patch to fix the failing `shouldScan` method:
```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".*\\.class").apply(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".*%s.*\\.class", packageToScan.replace(".", "\\."));
        if (new FilterBuilder().include(regex).apply(s)) {
            return true;
        }
    }
    return false;
}
```
Here are the changes I made:

* Replaced `.?\\.??` with `.*` in the regex for the `packagesToScan` variable to ensure it matches any number of leading dots.
* Replaced `\\.` with `\\.` in the regex for the `packageToScan` variable to ensure it matches the package name as a literal string.
* Added `.*` before and after `packageToScan` in the regex for the `packageToScan` variable to ensure it matches any number of leading or trailing dots.

These changes should fix the "cannot find symbol" error by ensuring the regex is correctly formed.