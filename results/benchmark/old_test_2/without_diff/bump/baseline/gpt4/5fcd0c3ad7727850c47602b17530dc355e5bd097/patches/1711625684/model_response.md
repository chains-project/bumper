```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassInfo> classInfoSet = new HashSet<>();
    classInfoSet.add(coverage.getClassInfo(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoSet);
  }
```