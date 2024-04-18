```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String fileName = data.getFileName();
    final List<MutationResult> mutations = data.getMutations();
    final Set<String> mutatedClasses = Collections.singleton(data.getMutatedClass());
    final ClassInfo classInfo = coverage.getClassInfo(mutatedClasses);
    return new MutationTestSummaryData(fileName, mutations, classInfo);
  }
```