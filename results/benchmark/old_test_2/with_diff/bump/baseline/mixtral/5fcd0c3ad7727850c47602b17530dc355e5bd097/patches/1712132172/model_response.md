Based on the error message and the changes in the library version, it seems that the `getClassInfo` method in `CoverageDatabase` now expects a single `ClassName` instead of a collection. Here's a possible patch for the `createSummaryData` method:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```

In this patch, we first extract the `mutatedClass` from the `ClassMutationResults` object, and then use it to get the `ClassInfo` from the `CoverageDatabase`. We then pass this `ClassInfo` object to the `MutationTestSummaryData` constructor instead of the result of `coverage.getClassInfo(Collections.singleton(data.getMutatedClass()))`. This should fix the compilation error.