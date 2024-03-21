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

* `FilterBuilder().include(".+\\.class").apply(s)` was changed to `FilterBuilder().include(".+\\.class").test(s)`
* `new FilterBuilder().include(regex).apply(s)` was changed to `new FilterBuilder().include(regex).test(s)`


The `apply` method is not available in the new version of the library, so it's being replaced with the `test` method, which serves the same purpose.

Note that the ` FilterBuilder().include(".+\\.class")` is not changed, because it's already using the `test` method.

Also, the method signature is not changed, and the code still uses the same variables and method calls as before, but with the updated `test` method.