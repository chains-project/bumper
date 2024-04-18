Here's the proposed patch for the failing method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```

In this patch, I created a temporary variable `classInfo` to store the result of `coverage.getClassInfo(Collections.singleton(data.getMutatedClass()))` and passed it as the third argument to the `MutationTestSummaryData` constructor. This makes the code more readable and easier to understand. However, the main purpose of this patch is to avoid the error message related to the missing symbol.