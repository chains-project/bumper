```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> classNames = Collections.singleton(data.getMutatedClass());
    ClassInfo classInfo = coverage.getClassInfo(classNames).stream().findFirst().orElseThrow();
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```