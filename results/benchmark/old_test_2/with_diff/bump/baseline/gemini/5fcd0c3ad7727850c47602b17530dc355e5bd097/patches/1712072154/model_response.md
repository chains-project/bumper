```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> set = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder classInfo = coverage.getClassInfoVisitor().getClassInfo(set.iterator().next(), null, 0);
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
  }
```