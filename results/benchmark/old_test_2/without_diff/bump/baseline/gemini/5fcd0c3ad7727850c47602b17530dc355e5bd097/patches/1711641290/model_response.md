```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<String> mutatedClasses =
        data.getMutations().stream().map(Mutation::getMutatedClass).collect(Collectors.toSet());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(mutatedClasses));
  }
```