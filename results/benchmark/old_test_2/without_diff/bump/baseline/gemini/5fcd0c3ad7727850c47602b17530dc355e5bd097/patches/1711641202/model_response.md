```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Collection<ClassInfo> classInfos =
        coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfos);
  }
```