```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    Set<ClassName> classes = Collections.singleton(data.getMutatedClass());
    ClassInfoBuilder infoBuilder = coverage.getClassInfoVisitor().getClassInfo(classes.iterator().next(), null, 0);
    for (ClassName c : classes) {
      infoBuilder.visit(c, coverage.getCoverageData(c).getCoverage());
    }
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), infoBuilder.build());
  }
```