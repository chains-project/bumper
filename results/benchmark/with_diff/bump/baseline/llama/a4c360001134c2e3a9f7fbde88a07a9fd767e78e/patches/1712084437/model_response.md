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
We replaced `apply` with `test` in the `FilterBuilder` instantiation and removed the `Override` annotation since the `apply` method is not overriding any method in the new version of the library. We also changed `FilterBuilder().include(regex).apply(s)` to `FilterBuilder().include(regex).test(s)` in the `for` loop.

This patch should fix the error and allow the code to compile and run correctly.