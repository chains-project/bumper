Here's the proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    CoverageClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```

In this patch, I created a new variable `classInfo` to store the result of `coverage.getClassInfo()` and passed it as an argument to `MutationTestSummaryData`. This change should resolve the "cannot find symbol" error.