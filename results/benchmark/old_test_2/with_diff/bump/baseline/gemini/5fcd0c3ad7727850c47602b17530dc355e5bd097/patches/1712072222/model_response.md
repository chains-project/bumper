```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = ClassName.fromString(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(mutatedClass)));
  }
```