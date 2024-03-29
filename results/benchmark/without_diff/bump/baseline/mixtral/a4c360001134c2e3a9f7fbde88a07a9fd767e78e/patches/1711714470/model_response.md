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

This version of the method uses the `String.endsWith` method to check if the input string ends with `.class`, and the `String.matches` method to check if the input string matches the regex pattern. This avoids the need to use the `FilterBuilder` class, which was causing the compilation error.