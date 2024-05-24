```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoBuilder builder = new ClassInfoVisitor();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), builder.getClassInfo(data.getMutatedClass(), null, 0L));
  }
```