Here's a proposed patch for the `shouldScan` method:

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

In this patch, I replaced the `apply` method with the `test` method for the `FilterBuilder` class. This is because the `apply` method has been removed in the new library version and replaced with the `test` method.

I also changed the `include` method to accept a `Predicate` instead of a `String`. This is because the `include` method that accepts a `String` has been removed in the new library version.

Note that I used Java 8 lambda expressions for the `Predicate` objects, so you will need to compile this code with Java 8 or later. If you are using an earlier version of Java, you will need to use anonymous inner classes instead of lambda expressions.