```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Collection<MutationDetails> mutations = data.getMutations();
    ClassInfo classInfo = coverage.getClassInfo(data.getMutatedClass());
    return new MutationTestSummaryData(fileName, mutations, classInfo);
}
```