```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String mutatedClass = data.getMutatedClass();
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(mutatedClass));
    if (classInfo == null) {
      classInfo = coverage.getClassInfo(Collections.singleton(mutatedClass));
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```