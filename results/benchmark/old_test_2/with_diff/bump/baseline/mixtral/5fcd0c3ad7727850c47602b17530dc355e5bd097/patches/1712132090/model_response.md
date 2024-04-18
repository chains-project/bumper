Based on the error message and the library changes, it seems that the `getClassInfo` method in `CoverageDatabase` now expects a single `ClassName` instead of a collection. Here's a possible patch for the `createSummaryData` method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClassName = data.getMutatedClass();
    org.pitest.classinfo.ClassInfo classInfo = coverage.getClassInfo(mutatedClassName);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

In this patch, we extract the mutated class name from `data` and use it to get the `ClassInfo` from `coverage`. We then pass the `ClassInfo` to the `MutationTestSummaryData` constructor instead of the result of `coverage.getClassInfo(Collections.singleton(data.getMutatedClass()))`. This should fix the compilation error.