```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Map<String, ClassInfo> classInfos = new HashMap<>();
    classInfos.put(data.getMutatedClass(), coverage.getClassInfo(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfos);
  }
```