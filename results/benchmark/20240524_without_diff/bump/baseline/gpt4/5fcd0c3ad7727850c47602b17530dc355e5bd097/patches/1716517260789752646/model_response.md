```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder classInfoBuilder = new ClassInfoVisitor();
    ClassInfo classInfo = classInfoBuilder.getClassInfo(data.getMutatedClass(), null, 0L);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```