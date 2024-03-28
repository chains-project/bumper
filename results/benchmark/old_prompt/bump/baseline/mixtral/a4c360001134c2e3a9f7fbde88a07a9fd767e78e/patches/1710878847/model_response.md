Here's a proposed patch to fix the failing `shouldScan` method:
```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".*\\.class").apply(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        packageToScan = packageToScan.trim();
        String regex = String.format(".*?\\.?%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(regex).apply(s)) {
            return true;
        }
    }
    return false;
}
```
The changes made are:

* Added a call to `trim()` on `packageToScan` to remove any leading or trailing whitespace.
* Changed the first `.?` to `.*?` in the regex pattern to make it non-greedy.

These changes should fix the "cannot find symbol" error. The first change is necessary because the original code does not remove leading or trailing whitespace from `packageToScan`, which may cause the regex pattern to fail to match. The second change is necessary because the original regex pattern is too specific, and may not match the desired packages. The non-greedy version of the pattern will match any number of characters before the package name, making it more flexible.