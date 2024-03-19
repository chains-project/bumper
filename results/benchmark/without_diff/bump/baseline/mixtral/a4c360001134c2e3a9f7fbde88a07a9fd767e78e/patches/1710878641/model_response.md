Here's a patch to fix the failing `shouldScan` method:
```java
    private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        Predicate<String> packageFilter = (str) -> true;
        if (packagesToScan != null && !packagesToScan.isEmpty()) {
            final String[] packages = packagesToScan.split(",");
            packageFilter = str -> {
                for (String packageToScan : packages) {
                    String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan.trim());
                    if (str.matches(regex)) {
                        return true;
                    }
                }
                return false;
            };
        }
        FilterBuilder filterBuilder = new FilterBuilder();
        return packageFilter.and(filterBuilder.include(".+\\.class")).apply(s);
    }
```
The issue is caused by the usage of a `FilterBuilder` class, which seems to be removed in the new version. To resolve this, we can use Java 8's `Predicate` functional interface to create a custom filter in place of the `FilterBuilder`.

The `packageFilter` variable will be used if `packagesToScan` is not empty, otherwise, it defaults to a filter that accepts any string. The `and` method from the `Predicate` interface is used to combine the custom filter with the original filter created by the `FilterBuilder`.

This solution assumes that the `include` method from `FilterBuilder` returns a `Predicate<String>`. If it returns a different functional interface, you may need to adjust the code accordingly.