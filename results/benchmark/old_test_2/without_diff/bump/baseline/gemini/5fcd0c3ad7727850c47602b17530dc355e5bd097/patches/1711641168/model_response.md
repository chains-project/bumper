```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String mutatedClass = data.getMutatedClass();
    final ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(mutatedClass));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```