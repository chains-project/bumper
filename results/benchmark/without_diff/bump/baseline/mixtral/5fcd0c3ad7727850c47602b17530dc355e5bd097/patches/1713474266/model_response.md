Here's a proposed patch for the given client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    CoverageClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch removes the call to `getClassInfo` on the `coverage` object and assigns the result to a local variable `classInfo`. This change should resolve the "cannot find symbol" error.