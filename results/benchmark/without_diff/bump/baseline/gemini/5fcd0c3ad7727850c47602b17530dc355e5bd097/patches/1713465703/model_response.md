```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    if (classInfo == null) {
      return new MutationTestSummaryData(data.getFileName(),
              data.getMutations(), Collections.emptyList());
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```