```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassInfo> classInfoSet = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    ClassInfo classInfo = classInfoSet.isEmpty() ? null : classInfoSet.iterator().next();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```