Here's the fixed version of the method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        coverage.getClassInfo(data.getMutatedClass()).getClassInfo());
}
```

The method `getClassInfo()` of `CoverageDatabase` has changed from returning a `Collection` to returning a `ClassInfo`. Therefore, you need to chain the `getClassInfo()` method again on the result of the first call.