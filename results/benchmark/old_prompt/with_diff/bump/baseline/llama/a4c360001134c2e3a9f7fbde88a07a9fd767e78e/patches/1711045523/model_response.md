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


The reason for these changes is that the `apply` method has been removed in the new version of the library, and the `test` method has been added. The `test` method does the same thing as the `apply` method, but it returns a boolean value indicating whether the given input matches the filter, which is what we need in this case.

Additionally, we can remove the `Override` annotation on the `shouldScan` method since it's not overriding any method in the new version of the library.