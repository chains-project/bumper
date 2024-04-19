Here's the updated `shouldScan` method that should fix the issue:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(e -> e.endsWith(".class")).test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(e -> e.matches(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

I replaced all the `apply` calls with the new `test` method, and updated the lambda expressions accordingly.

Here's a summary of the changes:

* Replace: `new FilterBuilder().include(regex).apply(s)`
* With: `new FilterBuilder().include(e -> e.matches(regex)).test(s)`

This change should fix the compilation error and make the code work with the new library version.