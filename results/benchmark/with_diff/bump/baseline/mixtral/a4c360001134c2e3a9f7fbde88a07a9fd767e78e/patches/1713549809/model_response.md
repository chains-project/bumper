Here's a possible patch for the given code. I changed the `apply` method to `test` for `FilterBuilder$Include`:

```java
    private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            FilterBuilder filterBuilder = new FilterBuilder();
            return filterBuilder.include(e -> e.endsWith(".class")).test(s);
        }
        final String[] packages = packagesToScan.split(",");
        for (String packageToScan : packages) {
            String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
            FilterBuilder filterBuilder = new FilterBuilder();
            if (filterBuilder.include(e -> e.matches(regex)).test(s)) {
                return true;
            }
        }
        return false;
    }
```

I also added a lambda expression for the `include` method, which is now required by the new version of the library.