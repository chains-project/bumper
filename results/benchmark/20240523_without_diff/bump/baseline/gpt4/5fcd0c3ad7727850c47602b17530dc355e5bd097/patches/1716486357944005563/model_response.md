```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
  Set<String> mutatedClassSet = new HashSet<>();
  mutatedClassSet.add(data.getMutatedClass());
  return new MutationTestSummaryData(data.getFileName(),
      data.getMutations(), coverage.getClassInfo(mutatedClassSet));
}
```