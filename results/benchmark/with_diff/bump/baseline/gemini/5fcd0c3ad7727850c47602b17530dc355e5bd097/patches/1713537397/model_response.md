```java
private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = new ClassName(data.getFileName(), data.getMutatedClass());
    final byte[] classBytes = coverage.getClassByteCode(mutatedClass);
    final long checksum = coverage.getClassChecksum(mutatedClass);
    final ClassInfoBuilder classInfoBuilder = ClassInfoVisitor.getClassInfo(mutatedClass, classBytes, checksum);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfoBuilder.build());
  }
```