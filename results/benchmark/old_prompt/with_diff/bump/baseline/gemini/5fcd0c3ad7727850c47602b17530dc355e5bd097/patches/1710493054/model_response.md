```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Collection<ClassName> classNames = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfoBuilder = coverage.getClassInfo(classNames.iterator().next(), data.getMutatedClassBytes(), data.getMutatedClassTime());
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder.build());
  }
```