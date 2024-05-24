```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Collection<MutationResult> mutations = data.getMutations();
    String mutatedClass = data.getMutatedClass();
    ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(fileName, mutations, classInfo);
  }
```