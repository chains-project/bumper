```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> set = Collections.singleton(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(set));
  }
```