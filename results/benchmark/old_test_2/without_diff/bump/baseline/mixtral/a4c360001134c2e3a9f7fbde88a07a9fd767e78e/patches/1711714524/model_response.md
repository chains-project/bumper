Here is a fixed version of the `shouldScan` method that removes the usage of the `FilterBuilder` class, which seems to be the cause of the "cannot find symbol" error:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return s.endsWith(".class");
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan.replace(".", "\\."));
        if (s.matches(".*.class" + regex)) {
            return true;
        }
    }
    return false;
}
```

The changes made to the original code are:

* Replaced the usage of `FilterBuilder` with a simpler check using the `endsWith` method.
* Replaced the usage of `FilterBuilder` with a regular expression check using the `matches` method.
* Added an escape to the `replace` method call to properly match dots in the package name.

These changes should fix the "cannot find symbol" error and make the method work as before.