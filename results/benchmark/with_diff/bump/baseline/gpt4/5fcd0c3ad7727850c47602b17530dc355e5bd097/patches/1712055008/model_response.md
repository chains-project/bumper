```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName className = data.getMutatedClass();
    byte[] emptyByteArray = new byte[0];
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(className, emptyByteArray, 0L);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```