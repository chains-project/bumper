```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> mutatedClass = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfoBuilder =
        coverage.getClassInfoVisitor().getClassInfo(mutatedClass.iterator().next(), null, 0);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfoBuilder);
  }
```