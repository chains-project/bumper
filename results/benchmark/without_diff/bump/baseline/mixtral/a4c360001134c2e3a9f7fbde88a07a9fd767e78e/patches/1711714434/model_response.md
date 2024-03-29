Here is a fixed version of the `shouldScan` method:
```java
    private boolean shouldScan(String s) {
        final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
        if (packagesToScan == null || packagesToScan.isEmpty()) {
            return new FilterBuilder().include(".*\\.class").apply(s);
        }
        final String[] packages = packagesToScan.split(",");
        for (String packageToScan : packages) {
            String regex = String.format(".*\\.?%s\\..+\\.class", packageToScan.replaceAll("\\.", "\\\\."));
            if (new FilterBuilder().include(regex).apply(s)) {
                return true;
            }
        }
        return false;
    }
```
The changes made are:

* Escape the `.` characters in the regular expression used to match the package name, so that they match a literal `.` instead of any character.
* Use `.*` at the beginning of the regular expression, so that it matches any prefix of the class name, not just classes that are directly under the package.
* Escape the backslash characters in the regular expression used to match the package name, so that they match a literal backslash instead of being interpreted as special characters.

These changes should allow the regular expressions to match the intended class names, and avoid the "cannot find symbol" error.