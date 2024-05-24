```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final List<ClassName> classes = Collections.singletonList(data.getMutatedClass());
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(classes);
    final List<ClassInfo> classInfos = classInfoBuilder.build();
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfos.get(0));
  }
```