Here's the updated `shouldScan` method that should fix the error:

```java
private boolean shouldScan(String s) {
    final String packagesToScan = System.getenv(PACKAGE_TO_SCAN);
    if (packagesToScan == null || packagesToScan.isEmpty()) {
        return new FilterBuilder().include(e -> e.endsWith(".class")).test(s);
    }
    final String[] packages = packagesToScan.split(",");
    for (String packageToScan : packages) {
        String regex = String.format(".?\\.??%s\\..+\\.class", packageToScan);
        if (new FilterBuilder().include(e -> e.matches(regex)).test(s)) {
            return true;
        }
    }
    return false;
}
```

The changes made are:

* Replaced `apply` method with `test` method for `FilterBuilder$Include` and `FilterBuilder$Exclude`.
* Updated lambda expression to match the new method signature of `test` method.
* Added parameter `e` to lambda expression for `test` method.
* Added import statement for `java.util.function.Predicate` to use lambda expressions.

These changes allow the code to use the new version of the library while maintaining the same functionality.