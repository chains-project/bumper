```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Set<MutationResult> mutations = data.getMutations();
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(fileName, mutations, classInfo);
  }
```