```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String mutatedClass = data.getMutatedClass();
    Collection<String> mutatedClasses = new HashSet<>();
    mutatedClasses.add(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(mutatedClasses));
  }
```