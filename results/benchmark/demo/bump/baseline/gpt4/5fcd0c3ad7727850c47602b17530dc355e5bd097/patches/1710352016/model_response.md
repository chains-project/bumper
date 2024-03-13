```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String fileName = data.getFileName();
    Collection<MutationResult> mutations = data.getMutations();
    String mutatedClass = data.getMutatedClass();
    Collection<String> mutatedClasses = new ArrayList<>();
    mutatedClasses.add(mutatedClass);
    ClassInfo classInfo = coverage.getClassInfo(mutatedClasses);
    return new MutationTestSummaryData(fileName, mutations, classInfo);
  }
```