```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    String mutatedClass = data.getMutatedClass();
    Set<String> mutatedClassSet = new HashSet<>();
    mutatedClassSet.add(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(mutatedClassSet));
  }
```