```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> classNames = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfo = coverage.getClassInfo(data.getFileName(), classNames);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```