```java
  private MutationTestSummaryData createSummaryData(
      final CoverageDatabase coverage, final ClassMutationResults data) {
    final ClassName mutatedClass = data.getMutatedClass();
    final byte[] bytecode = data.getBytecode();
    final long checksum = data.getChecksum();
    final ClassInfoBuilder classInfoBuilder = coverage.getClassInfoBuilder();
    final ClassInfo classInfo = classInfoBuilder.getClassInfo(mutatedClass, bytecode, checksum);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), classInfo);
  }
```