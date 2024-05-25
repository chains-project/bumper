Here is a proposed patch for the failing client code:

```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```

This patch creates a new variable `classInfo` to store the result of `coverage.getClassInfo()`, and then uses this variable in the constructor call for `MutationTestSummaryData`. This avoids the need to call `getClassInfo()` multiple times, which may have been causing the symbol resolution error.

Note that this patch assumes that the `ClassInfo` class has not been removed or changed in a way that breaks compatibility. If that is not the case, a different approach may be necessary.