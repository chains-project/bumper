```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> classes = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(data.getMutatedClass(), data.getBytes(), data.getTimestamp());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
  }
```