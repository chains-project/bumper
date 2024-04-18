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
We changed the `apply` method to `test` in the `FilterBuilder` class, as the former is removed in the new library version. We also removed the `Override` annotation, as the method is not overriding any method in the new version.