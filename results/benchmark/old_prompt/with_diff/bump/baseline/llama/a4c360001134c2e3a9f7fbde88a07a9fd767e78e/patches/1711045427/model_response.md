Here's a proposed patch to fix the error:
```java
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

* `FilterBuilder().include(".+\\.class").apply(s)` was changed to `new FilterBuilder().include(".+\\.class").test(s)`
* `FilterBuilder().include(regex).apply(s)` was changed to `new FilterBuilder().include(regex).test(s)`


The `apply` method is not available in the new version of the library, so it was replaced with the `test` method, which serves the same purpose.

Additionally, the `FilterBuilder` constructor was changed to `new FilterBuilder()` to match the changes in the library.

This patch should fix the error and allow the code to compile and run correctly.