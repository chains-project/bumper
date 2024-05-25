```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Collection<MutationDetails> mutations = data.getMutations();
    String mutatedClass = data.getMutatedClass();
    Collection<ClassInfo> classInfos = coverage.getClassInfo(Collections.singleton(mutatedClass));

    return new MutationTestSummaryData(fileName, mutations, classInfos);
  }
```