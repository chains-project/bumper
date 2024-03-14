```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(
        data.getMutatedClass(), new byte[0], 0L);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```