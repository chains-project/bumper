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
The changes made are:

* `FilterBuilder().include(".+\\.class").apply(s)` is replaced with `FilterBuilder().include(".+\\.class").test(s)`,
* `FilterBuilder().include(regex).apply(s)` is replaced with `FilterBuilder().include(regex).test(s)`


In the new version of the library, the `apply` method has been removed and replaced with the `test` method. Therefore, we need to update the code to use the `test` method instead of `apply` to fix the error.