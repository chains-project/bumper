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


The `apply` method is no longer available in the updated version of the library, so it's being replaced with the `test` method, which serves the same purpose.

Additionally, we're using the `new` keyword to create a new instance of the `FilterBuilder` class, since the `FilterBuilder.apply` method is not static.