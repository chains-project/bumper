```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = data.getMutatedClass();
    final ClassInfo classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```