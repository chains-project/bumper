```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<String> mutatedClasses = new HashSet<>();
    mutatedClasses.add(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(mutatedClasses));
}
```