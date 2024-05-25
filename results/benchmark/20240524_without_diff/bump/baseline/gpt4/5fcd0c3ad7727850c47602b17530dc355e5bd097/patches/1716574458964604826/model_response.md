```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Collection<String> mutatedClasses = new ArrayList<>();
    mutatedClasses.add(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(mutatedClasses));
  }
```