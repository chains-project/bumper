```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> mutatedClasses = Collections.singleton(data.getMutatedClass());
    final ClassInfo classInfo = coverage.getClassInfo(mutatedClasses);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```