```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Collection<MutationDetails> mutations = data.getMutations();
    Collection<ClassInfo> classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(fileName, mutations, classInfo);
  }
```