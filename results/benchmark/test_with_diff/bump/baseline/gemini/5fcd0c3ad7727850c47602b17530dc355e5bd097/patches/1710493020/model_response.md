```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = new ClassName(data.getMutatedClass());
    final ClassInfoBuilder classInfoBuilder =
        ClassInfoVisitor.getClassInfo(mutatedClass, data.getByteCode(), data.getCreationTime());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder);
  }
```