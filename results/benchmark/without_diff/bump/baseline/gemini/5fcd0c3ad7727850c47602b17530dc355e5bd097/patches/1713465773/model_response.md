```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<String> classes = Collections.singleton(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(classes));
  }
```