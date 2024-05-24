```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] emptyByteArray = new byte[0];
    long zeroLong = 0L;
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, emptyByteArray, zeroLong);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```