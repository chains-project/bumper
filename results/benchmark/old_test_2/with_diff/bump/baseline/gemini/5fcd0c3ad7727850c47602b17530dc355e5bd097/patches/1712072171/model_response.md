```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfoVisitor visitor = new ClassInfoVisitor();
    byte[] bytes = coverage.getBytecode(data.getMutatedClass());
    coverage.visitClass(data.getMutatedClass(), bytes, visitor);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), visitor.getClassInfo());
  }
```