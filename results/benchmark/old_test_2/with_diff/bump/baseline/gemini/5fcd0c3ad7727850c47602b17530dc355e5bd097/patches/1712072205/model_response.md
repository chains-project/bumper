```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName className = new ClassName(data.getFileName());
    final ClassInfoBuilder classInfoBuilder =
        coverage.getClassInfo(className, data.getMutatedClass(), data.getMutations());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder);
  }
```