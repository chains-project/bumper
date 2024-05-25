```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
      return new MutationTestSummaryData(data.getFileName(), data.getMutations(), null);
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```