```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final List<ClassInfo> classInfos = new ArrayList<>();
    classInfos.add(coverage.getClassInfo(Collections.singleton(data.getMutatedClass())));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfos);
  }
```