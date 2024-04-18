```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    List<ClassInfo> classInfoList = new ArrayList<>();
    classInfoList.add(coverage.getClassInfo(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoList);
  }
```