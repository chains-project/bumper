Here's a possible patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())));
  }
```

Replace with:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), getClassInfo(coverage, data.getMutatedClass()));
  }

  private static org.pitest.classinfo.ClassInfo getClassInfo(
      final CoverageDatabase coverage, final Class<?> clazz) {
    return new org.pitest.classinfo.ClassInfoBuilder(clazz).build();
  }
```
The patch creates a new method `getClassInfo` that uses the `ClassInfoBuilder` to create a `ClassInfo` instance for the given class. The `getClassInfo` method takes the `CoverageDatabase` and the class to get the `ClassInfo` for as parameters. The `ClassInfoBuilder` is used to create a new `ClassInfo` instance for the given class.


The `createSummaryData` method is then modified to use the new `getClassInfo` method to get the `ClassInfo` for the mutated class.


This patch should fix the error and allow the code to compile and run correctly.