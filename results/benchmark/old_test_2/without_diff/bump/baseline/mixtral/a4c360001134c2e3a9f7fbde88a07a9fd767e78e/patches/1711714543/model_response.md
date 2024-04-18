Here's a proposed patch to fix the failing `shouldScan` method:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(".*\\.class").apply(s);
    }
    final String[] packages = packagesToScan.split(",");
    Pattern pattern = Pattern.compile("(?:\\.?)\\.?(?:[^.]+)\\.(?:[^.]+)\\.class");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        Matcher matcher = pattern.matcher(s);
        if (matcher.find() && matcher.group().matches(regex)) {
            return true;
        }
    }
    return false;
}
```

The changes made include:

* Adding a `Pattern` object `pattern` to match against the input string `s` with a regular expression that includes the package name.
* Using a `Matcher` object `matcher` to check if the input string `s` matches the pattern.
* Updating the `regex` string to match the pattern.
* Updating the `if` statement to check if the input string `s` matches the pattern using the `matcher.find()` method.

These changes should fix the "cannot find symbol" error by providing a more robust way of checking if the input string `s` matches the pattern.