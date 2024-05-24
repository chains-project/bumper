```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = new ClassName(data.getFileName());
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(mutatedClass, data.getClassBytes(), data.getTimestamp());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```