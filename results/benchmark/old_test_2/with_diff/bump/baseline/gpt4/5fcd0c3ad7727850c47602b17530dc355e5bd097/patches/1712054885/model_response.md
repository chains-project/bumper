```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClassName = data.getMutatedClass();
    byte[] bytes = new byte[0]; // replace with actual byte array if available
    long timestamp = System.currentTimeMillis(); // replace with actual timestamp if available
    ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClassName, bytes, timestamp);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```