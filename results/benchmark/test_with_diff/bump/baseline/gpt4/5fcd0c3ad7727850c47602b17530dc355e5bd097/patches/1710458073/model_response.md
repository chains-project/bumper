```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = org.pitest.classinfo.ClassInfoVisitor.getClassInfo(data.getMutatedClass(), null, 0);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```