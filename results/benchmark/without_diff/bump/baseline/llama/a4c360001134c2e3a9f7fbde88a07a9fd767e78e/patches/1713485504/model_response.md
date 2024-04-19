Here's a proposed patch to fix the error:
```
private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            return new FilterBuilder().include(".+\\.class").apply(s);
        }
        final String[] packages = packagesToScan.split(",");
        for (String packageToScan : packages) {
            String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
            if (new FilterBuilder().include(regex).apply(s)) {
                return true;
            }
        }
        return false;
    }
```
The error was caused by the fact that the `FilterBuilder` class has been removed in the new version of the library. To fix this, we can replace `FilterBuilder` with `PatternFilter` from the same package, which has the same functionality. Here's the modified code:
```
private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            return PatternFilter.include(".+\\.class").apply(s);
        }
        final String[] packages = packagesToScan.split(",");
        for (String packageToScan : packages) {
            String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
            if (PatternFilter.include(regex).apply(s)) {
                return true;
            }
        }
        return false;
    }
```
This modification should fix the error and allow the code to compile and run correctly.