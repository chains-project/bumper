```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
      classInfo = ClassInfo.EMPTY_CLASS_INFO;
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```