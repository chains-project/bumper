```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> mutatedClass = Collections.singleton(data.getMutatedClass());
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfoBuilder(mutatedClass);
    final ClassInfo classInfo = classInfoBuilder.getClassInfo(data.getFileName(), data.getMutations());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```