```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final String fileName = data.getFileName();
    final Set<ClassName> mutatedClass = Collections.singleton(data.getMutatedClass());
    final ClassInfoBuilder classInfo = coverage.getClassInfo(mutatedClass);
    return new MutationTestSummaryData(fileName, data.getMutations(), classInfo);
  }
```