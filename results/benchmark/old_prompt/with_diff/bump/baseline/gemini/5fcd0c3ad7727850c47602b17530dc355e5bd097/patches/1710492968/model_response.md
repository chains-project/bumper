```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> classInfo = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(data.getMutatedClass(), null, 0);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(),
        classInfoBuilder.create());
  }
```