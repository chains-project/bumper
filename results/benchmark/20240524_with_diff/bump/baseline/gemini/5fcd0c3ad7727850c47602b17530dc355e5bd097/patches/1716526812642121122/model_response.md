```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final Set<ClassName> classes = Collections.singleton(data.getMutatedClass());
    final ClassInfoVisitor visitor = new ClassInfoVisitor();
    coverage.visitClassInfo(classes, visitor);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), visitor.getClassInfo());
  }
```