Here's the proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```
This patch creates a new variable `classInfo` to store the result of `coverage.getClassInfo()` and uses it in the constructor of `MutationTestSummaryData`. This should resolve the "cannot find symbol" error.