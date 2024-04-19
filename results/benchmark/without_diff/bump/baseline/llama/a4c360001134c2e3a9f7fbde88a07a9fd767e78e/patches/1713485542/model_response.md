```
  private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv("PACKAGE_TO_SCAN");
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
Replace the line:
```
final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
```
with:
```
final String packagesToScan = System.getenv("PACKAGE_TO_SCAN");
```
The error was caused by the environment variable `PACKAGE_TO_SCAN` not being defined. By changing the line to `System.getenv("PACKAGE_TO_SCAN")` we are ensuring that the environment variable is properly referenced, and the error should be fixed.