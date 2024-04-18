Here's a proposed patch for the given client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```

The patch modifies the code to store the result of `coverage.getClassInfo` in a local variable `classInfo`, which is then used when creating the `MutationTestSummaryData` object. This change should resolve the "cannot find symbol" error.