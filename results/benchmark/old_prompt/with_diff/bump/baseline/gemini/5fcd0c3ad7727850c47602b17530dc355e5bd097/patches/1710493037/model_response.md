```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> mutatedClasses = Collections.singleton(data.getMutatedClass());
    final ClassInfoBuilder classInfoBuilder =
        ClassInfoVisitor.getClassInfo(data.getMutatedClass(), data.getBytecode(), data.getMutationId());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(classInfoBuilder.build()));
  }
```