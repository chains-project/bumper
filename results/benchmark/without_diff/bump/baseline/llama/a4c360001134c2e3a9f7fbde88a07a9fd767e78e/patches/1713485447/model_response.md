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

Replace the `FilterBuilder` class with `JavaFilterBuilder`, like this:
```
  private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            return new JavaFilterBuilder().include(".+\\.class").apply(s);
        }
        final String[] packages = packagesToScan.split(",");
        for (String packageToScan : packages) {
            String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
            if (new JavaFilterBuilder().include(regex).apply(s)) {
                return true;
            }
        }
        return false;
    }
```
The `JavaFilterBuilder` class is a part of the Java API, and it provides a way to create filters for packages. The `include()` method is used to specify a pattern for the filter, and the `apply()` method is used to apply the filter to a given string.

In this case, we are using the `JavaFilterBuilder` class to create a filter that matches packages that start with the packages specified in the `PACKAGE_TO_SCAN` environment variable, followed by any number of digits, followed by the string ".class". This should match all classes in the packages specified in the environment variable.

Note that the `JavaFilterBuilder` class is only available in Java 8 and later versions. If you're using an earlier version of Java, you'll need to use a different approach to create the filter.