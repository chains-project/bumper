```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String mutatedClass = data.getMutatedClass();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(mutatedClass)));
  }
```