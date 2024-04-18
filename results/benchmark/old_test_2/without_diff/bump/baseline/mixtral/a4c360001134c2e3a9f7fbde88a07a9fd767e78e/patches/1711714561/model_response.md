Here's a possible patch for the failing `shouldScan` method:
```java
    private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            return new FilterBuilder().include(".*\\.class").apply(s);
        }
        final String[] packages = packagesToScan.split(",");
        Pattern pattern = Pattern.compile(".*");
        for (String packageToScan : packages) {
            String regex = String.format(".*?\\.??%s\\..+\\.class", packageToScan);
            pattern = Pattern.compile(regex);
            if (pattern.asPredicate().test(s)) {
                return true;
            }
        }
        return false;
    }
```
In this patch, I added a `Pattern` variable `pattern` to replace the repeated usage of `new FilterBuilder().include(regex)`. This should fix the "cannot find symbol" error, as it seems that the `FilterBuilder` class or method is no longer available.

Note that this patch assumes that the `include` method of `FilterBuilder` has been replaced with a constructor that takes a regular expression as a string, and that the `apply` method has been replaced with a `test` method that takes a string as a parameter. If these assumptions are incorrect, the patch may need to be adjusted accordingly.