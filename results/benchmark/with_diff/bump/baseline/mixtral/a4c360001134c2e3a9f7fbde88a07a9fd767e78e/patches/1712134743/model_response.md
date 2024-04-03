Here's a possible patch for the `shouldScan` method:

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

In this patch, I replaced the deprecated `apply` method with the new `test` method for `FilterBuilder` and `FilterBuilder$Include`. I also changed the parameter type of the `include` method from `String` to `Predicate<String>` to match the new method signature.

Note that the `Predicate` interface is a part of the `java.util.function` package, which is a part of Java 8 and later versions. If you are using an earlier version of Java, you may need to use an anonymous class to implement the `Predicate` interface instead of a lambda expression.