```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String fileName = data.getFileName();
    final List<MutationResult> mutations = data.getMutations();
    final Collection<ClassInfo> classInfos =
        coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(fileName, mutations, classInfos);
  }
```